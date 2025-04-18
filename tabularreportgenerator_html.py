# Copyright (c) 2025 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, Template

from tabularreportgenerator_types import Report


def load_template(path: Path) -> Template:
    env = Environment(loader=FileSystemLoader(path.parent))
    template = env.get_template(path.name)

    return template


def make_html(report: Report, template: Template) -> str:
    return template.render(**report.dict())
