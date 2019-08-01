import base64
import json
import os
from json import JSONDecodeError

from jinja2 import Environment, FileSystemLoader


class CloudFormationTemplate:
    """
    Class Responsible to render a cloud formation template
    """

    def __init__(self, template_dir='cloudformation', variables_dir='variables', files_dir='files', json_indent=2):
        self.template_dir = template_dir
        self.variables_dir = variables_dir
        self.json_indent = json_indent
        self.files_dir = files_dir

        self._env = None
        self._variables = None

    @property
    def env(self):
        if not self._env:
            self._env = Environment(
                loader=FileSystemLoader(self.template_dir, )
            )
        return self._env

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

    def get_files(self):
        """Read fiels from provided dir and put base64 of those files into dict 'file_name': 'base'"""
        files_dict = {}
        try:
            filenames = os.listdir(self.files_dir)
        except FileNotFoundError:
            return files_dict

        # get base64 of each of the file
        for filename in filenames:
            with open(os.path.join(self.files_dir, filename), 'rb') as f:
                data = f.read()
                encodedBytes = base64.b64encode(data.encode("utf-8"))
                files_dict[filename] = str(encodedBytes, "utf-8")
        return files_dict

    def render_template(self, template_name):
        """
        Render and return provided template
        """
        template = self.env.get_template(template_name)
        self.variables[self.files_dir] = self.get_files()
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
