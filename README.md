# Render Cloud Formation Template

A simple python project that use power of Jinja2 for an easier cloudformation temlate generation.

### Install

`pip install -e git+https://github.com/tjsoftware-co/RenderCloudFormationTemplate.git@v1.0#egg=render-cloud-formation-template`
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

### Files Dir
Directory with files that are going to added be add into template context as:
```json
{
  "files_dir": {
    "file_name": "base64",
    "file_name2": "base64"
  }
}
```
This is usefull to put files into s3 bucket using cloudfront and `AWS::S3::Object` and `"Transform": "S3Objects"`
Example use:
```jinja2
{
  "Type": "AWS::S3::Object",
  "Properties": {
    "Target": {
      "Bucket": {
        "Ref": "BRSStandardBucket",
        "Key": ".pylintrc"
      }
    },
    "Base64Body": "{{ files.pylint }}"
  }
}
```


### Command Line Usage

```bash
generate-cloud-formation-template --template_name=blueriders_aws.template
```

Command going to produce `blueriders_aws.json` file if rendered template is a valid json. 
(Command do not check if json is valid cloud formation template. 
Use `aws cloudformation validate-template --template-body file://blueriders_aws.json` to check that. 

Command going to produce `blueriders_aws-error.json` file if rendered template is not a valid json.


###Macros

Macros can be used to build CloudFormation templates easy and fast.
Available macros and their usage:

####CodeCommit

* CodeCommit Repository

```jinja2
{% extends "base.template" %}

{% import "macros/codecommit.template" as codecommit %}

{% block content %}
    "Resources": {
        "Repository1": {{ codecommit.repository(name=repositories.Repository1.name, description=repositories.Repository1.description) }}
    }
{% endblock %}
```

####IAM

* Role with assigned policy

```jinja2
{% extends "base.template" %}

{% import "macros/iam.template" as iam %}

{% block content %}
    "Resources": {
        "Role1": {{ iam.role(name="Role1", services=["codepipeline.amazonaws.com", "codebuild.amazonaws.com"], actions=["cloudformation:*", "s3:*"]) }}
    }
{% endblock %}
```

####S3

* Bucket with default settings

```jinja2
{% extends "base.template" %}

{% import "macros/s3.template" as s3 %}

{% block content %}
    "Resources": {
        "Bucket1": {{ s3.bucket(name="bucket1") }}
    }
{% endblock %}
```

####CodeBuild

* CodeBuild Project use in codepipeline artifact.
```jinja2
{% extends "base.template" %}

{% import "macros/codebuild.template" as codebuild %}

{% block content %}
    "Resources": {
        "Build1": {{ codebuild.codepipeline_build(name="Build1", role="RoleRef", description="Build Description") }}
    }
{% endblock %}
```

####CodePipeline

* Pipeline for CI / CD for CloudFormation templates
```jinja2
{% extends "base.template" %}

{% import "macros/codepipeline.template" as codepipeline %}

{% block content %}
    "Resources": {
        "Build1": {{ codepipeline.cloudformation_pipeline(name="Pipeline1", role="Role1", repository="MyRepo", s3="ArtiactStore", branch="master") }}
    }
{% endblock %}
``` 