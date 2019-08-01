from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="render-cloud-formation-template",
    version="1.5",
    author="Tomasz Roszko",
    author_email="tomaszroszko@tjsoftware.co",
    description="A simple python project that use power of Jinja2 for an easier cloudformation temlate generation",
    url="https://eu-central-1.console.aws.amazon.com/codesuite/codecommit/repositories/RenderCloudFormationTemplate/setup?region=eu-central-1",
    long_description=long_description,
    py_modules=['cloudformation_template'],
    scripts=['bin/generate-cloud-formation-template']
)
