import json
import os
from json import JSONDecodeError

from jinja2 import Environment, FileSystemLoader


class CloudFormationTemplate:
    """
    Class Responsible for rendering a template
    """

    def __init__(self, template_dir='cloudformation', variables_dir='variables', json_indent=2):
        self.template_dir = template_dir
        self.variables_dir = variables_dir
        self.json_indent = json_indent

        self._env = None
        self._variables = None

    @property
    def env(self):
        if not self._env:
            self._env = Environment(
                loader=FileSystemLoader([self.base_dir, self.template_dir], )
            )
        return self._env

    @property
    def base_dir(self):
        """return directory path to macros"""
        return os.path.join(os.path.dirname(__file__), 'base_templates')

    @property
    def variables(self):
        if not self._variables:
            self._variables = {}

            file_names = os.listdir(self.variables_dir)
            for file_name in file_names:
                file_path = os.path.join(self.variables_dir, file_name)
                with open(file_path, 'r') as f:
                    variable_value = json.load(f)
                    variable_name = file_name.replace('.json', '')
                    self._variables[variable_name] = variable_value

        return self._variables

    def render_template(self, template_name):
        """
        Render and return provided template
        """
        template = self.env.get_template(template_name)
        rendered_template = template.render(**self.variables)
        return rendered_template

    def generate_json(self, template_name):
        """
        Save json file in current directory
        """
        try:
            template = self.render_template(template_name=template_name)
            json_template = json.loads(template)
        except JSONDecodeError as e:
            # save raw template as there was an issue with saving json
            with open(template_name.replace('.template', '-error.json'), 'w') as f:
                f.write(template)
            raise e
        else:
            with open(template_name.replace('.template', '.json'), 'w') as f:
                json.dump(json_template, f, indent=self.json_indent)