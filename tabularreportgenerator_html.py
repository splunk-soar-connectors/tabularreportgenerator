from pathlib import Path

from jinja2 import Template, Environment, FileSystemLoader
from tabularreportgenerator_types import Report


def load_template(path: Path) -> Template:
    env = Environment(loader=FileSystemLoader(path.parent))
    template = env.get_template(path.name)

    return template


def make_html(report: Report, template: Template) -> str:
    return template.render(**report.dict())
