# Everything to Everything (ETE)

ETE is a simple CLI program that converts data types to other data types. It currently supports [Toml](https://pypi.org/project/toml/), [Yaml](https://pypi.org/project/PyYAML/), and [Json](https://www.json.org/).

## Install

To use, first install:

```console
pip install -U ete
```

Or use [Poetry](https://python-poetry.org):

```console
poetry add ete
```

## Use

ETE is purely command line, and there is no great API yet.

```console
ete --help
```

ETE converts files to different types of files. Try writing a Toml file like this:

```toml
# Named test.toml
[table]
message = true
```

Then run:

```console
ete test.toml test.json
```

Congratulations! You've just experienced the ease of this conversion tool.

## Contribute

```console
git clone https://github.com/BD103/Everything-to-Everything.git
poetry lock
poetry install
```

> I use [Poetry](https://python-poetry.org), so you may have to download it as well.