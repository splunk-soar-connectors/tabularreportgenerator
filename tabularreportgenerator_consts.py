from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent.resolve() / "templates"
REPORT_TEMPLATE = TEMPLATES_DIR / Path("report.j2")
