# Render Cloud Formation Template

A simple python project that use power of Jinja2 for an easier cloudformation temlate generation.

### Install

`pip install git+ssh://git-codecommit.eu-central-1.amazonaws.com/v1/repos/RenderCloudFormationTemplate`

### Command Line Help

```bash
generate-cloud-formation-template --help
usage: generate-cloud-formation-template [-h] [--template_dir TEMPLATE_DIR]
                                         --template_name TEMPLATE_NAME
                                         [--variables_dir VARIABLES_DIR]

Generate Template command.

optional arguments:
  -h, --help            show this help message and exit
  --template_dir TEMPLATE_DIR
                        Dir with cloudformation templates
  --template_name TEMPLATE_NAME
                        Template name to render
  --variables_dir VARIABLES_DIR
                        Dir with variables files
```

### TEMPLATE_DIR
It's a directory with Jinia2 templates. Example of template file
`blueriders_aws.template`
```jinja2
{% extends "base.template" %}

{% block content %}
    "Resources": {
    {#  Create basic groups in a company  #}
    {% for group in groups %}
        "{{ group.resource_name }}": {% include "iam/group.json" %},
    {% endfor %}
        {# Create general policy for all employees #}
        "BRSMembersPolicy": {% include "iam/members_policy.template" %},
        "BRSDevOpsPolicy": {% include "iam/devops_policy.json" %},
    {% for user in users %}
        "Developer{{ user.first_name }}{{ user.last_name }}": {% include "iam/user.template" %},
    {% endfor %}
    {% for repository in repositories %}
        "Repository{{ repository.name }}": {% include "codecommit/repository.json" %},
        "Repository{{ repository.name }}Policy": {% include "iam/repository_policy.template" %}{{ "," if not loop.last }}
    {% endfor %}
    }
{% endblock %}
```

`base.template`
```jinja2
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "AWS Setup for BlueRider.Software for Roles, Groups, Policies and Users",
  {% block content %}{% endblock %}
}
```

### Variables Dir
Directory with a json files where all the variables are stored. Variables are used automaticaly during
template rendering. 

Example: `groups.json`
```json
[
  {
    "resource_name": "DevelopersGroup",
    "name": "BRS-Developers"
  },
  {
    "resource_name": "DevOpsGroup",
    "name": "BRS-DevOps"
  }
]
```
In Jinija2 template variable `groups` going to be avaialble and can be used, for example:
```jinja2
    "Groups": [
      {% for group in groups %}
      {"Ref":  "{{ group.resource_name }}"}{{ "," if not loop.last }}
      {% endfor %}
    ],
```

### Command Line Usage

```bash
generate-cloud-formation-template --template_name=blueriders_aws.template
```

Command going to produce `blueriders_aws.json` file if rendered template is a valid json. 
(Command do not check if json is valid cloud formation template. 
Use `aws cloudformation validate-template --template-body file://blueriders_aws.json` to check that. 

Command going to produce `blueriders_aws-error.json` file if rendered template is not a valid json.