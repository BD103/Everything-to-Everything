import click

from .core import convert, detect_type


@click.command()
@click.argument("filename", type=click.Path(exists=True, dir_okay=False))
@click.argument("output", type=click.Path(dir_okay=False))
def ete(filename, output):
  with open(output, "wt") as fp:
    fp.write(convert(filename, detect_type(output)))


if __name__ == "__main__":
  ete()
