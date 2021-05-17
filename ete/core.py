import json

import toml
from .remap.yaml import yaml

types = [
  "json",
  "toml",
  "yaml"
]

_types = {
  "json": json,
  "toml": toml,
  "yaml": yaml
}


def detect_type(filename):
  if filename.endswith(".json"):
    return "json"
  elif filename.endswith(".toml"):
    return "toml"
  elif filename.endswith(".yaml") or filename.endswith(".yml"):
    return "yaml"
  else:
    return None


def convert(filename, langauge):
  file_type = detect_type(filename)

  if file_type is None:
    exit(1)

  method = _types[file_type]

  with open(filename, "rt") as fp:
    file_dict = method.load(fp)

  return _types[langauge].dumps(file_dict)
