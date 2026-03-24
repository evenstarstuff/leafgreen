#!/usr/bin/env python3

from pathlib import Path

import yaml
from ryland import Ryland

ROOT_DIR = Path(__file__).parent.parent
OUTPUT_DIR = ROOT_DIR / "site"
TEMPLATE_DIR = ROOT_DIR / "templates"
PANTRY_DIR = ROOT_DIR / "pantry"
DATA_DIR = ROOT_DIR / "data"

ryland = Ryland(output_dir=OUTPUT_DIR, template_dir=TEMPLATE_DIR)

ryland.clear_output()

trainer = yaml.safe_load(open(DATA_DIR / "trainer.yaml"))

## style

ryland.copy_to_output(PANTRY_DIR / "style.css")
ryland.add_hash("style.css")

## home page

ryland.render_template("home.html", "index.html", {
    "trainer": trainer,
})
