# yuokada.github.com

## github pages

Install uv:

```shell
$ curl -Ls https://astral.sh/uv/install.sh | sh
```

Install project dependencies:

```shell
$ uv sync
```

This project uses [MyST-Parser](https://myst-parser.readthedocs.io/) so you can write documentation in Markdown.

## Getting started

```
$ git clone --recurse-submodules git@github.com:yuokada/yuokada.github.com.git gh-pages
```

## Plus

[watchdog · PyPI](https://pypi.org/project/watchdog/)

```
# Install watchdog
$ uv sync --extra dev

# Monitor *.rst and *.md files and update html files
$ watchmedo shell-command --patterns="*.rst;*.md" --recursive --wait --command="make html"
```

--------

## Links

- [Sphinx Themes Gallery](https://sphinx-themes.org/)
