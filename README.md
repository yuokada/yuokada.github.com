# yuokada.github.com

## github pages

```shell
$ poetry install
```

## Getting started

```
$ git clone --recurse-submodules git@github.com:yuokada/yuokada.github.com.git gh-pages
```

## Plus

[watchdog · PyPI](https://pypi.org/project/watchdog/)

```
# Install watchdog
$ poetry install --with dev

# Monitor *.rst files and update html files
$ watchmedo shell-command --patterns="*.rst" --recursive --wait --command="make html"
```

--------

## Links

- [Sphinx Themes Gallery](https://sphinx-themes.org/)
