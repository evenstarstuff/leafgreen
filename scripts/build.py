#!/usr/bin/env python3

import os
from pathlib import Path

import yaml
from ryland import Ryland

import shutil
from os import makedirs

ROOT_DIR = Path(__file__).parent.parent
OUTPUT_DIR = ROOT_DIR / "site"
TEMPLATE_DIR = ROOT_DIR / "templates"
PANTRY_DIR = ROOT_DIR / "pantry"
DATA_DIR = ROOT_DIR / "data"

url_root = os.environ.get("URL_ROOT", "/")
ryland = Ryland(output_dir=OUTPUT_DIR, template_dir=TEMPLATE_DIR, url_root=url_root)

ryland.clear_output()

trainer = yaml.safe_load(open(DATA_DIR / "trainer.yaml"))
postcards = yaml.safe_load(open(DATA_DIR / "postcards.yaml"))

## style

ryland.copy_to_output(PANTRY_DIR / "style.css")
ryland.add_hash("style.css")

## sprites

makedirs(OUTPUT_DIR / "sprites", exist_ok=True)

for sprite in (ROOT_DIR / "sprites").glob("*.*"):
    shutil.copy(sprite, OUTPUT_DIR / "sprites" / sprite.name)

## locations

makedirs(OUTPUT_DIR / "locations", exist_ok=True)

for location in (ROOT_DIR / "locations").glob("*.*"):
    shutil.copy(location, OUTPUT_DIR / "locations" / location.name)

## home page

ryland.render_template("home.html", "index.html", {
    "trainer": trainer,
})

## postcards page

ryland.render_template("postcards.html", "postcards/index.html", {
    "postcards": postcards,
})
