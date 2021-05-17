import io

import yaml


def _loads(s: str):
  fp = io.StringIO(s)
  return yaml.load(fp, Loader=yaml.FullLoader)


yaml.loads = _loads
yaml.dumps = yaml.dump
