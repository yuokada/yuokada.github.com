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

## Getting started

```
$ git clone --recurse-submodules git@github.com:yuokada/yuokada.github.com.git gh-pages
```

## Plus

[watchdog · PyPI](https://pypi.org/project/watchdog/)

```
# Install watchdog
$ uv sync --extra dev

# Monitor *.rst files and update html files
$ watchmedo shell-command --patterns="*.rst" --recursive --wait --command="make html"
```

--------

## Links

- [Sphinx Themes Gallery](https://sphinx-themes.org/)
