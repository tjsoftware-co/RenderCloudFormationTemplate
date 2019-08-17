from distutils.core import setup

files = ["base_templates/*", "base_templates/macros/*"]

setup(
    name="render-cloud-formation-template",
    version="2.19",
    author="Tomasz Roszko",
    author_email="tomaszroszko@tjsoftware.co",
    description="A simple python project that use power of Jinja2 for an easier cloudformation temlate generation",
    url="https://github.com/tjsoftware-co/RenderCloudFormationTemplate.git",
    packages = ["cloudformation_template"],
    package_data = {"cloudformation_template" : files },
    scripts=["bin/generate-cloud-formation-template"]
)
