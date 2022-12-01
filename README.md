[![Hexlet Ltd. logo](https://raw.githubusercontent.com/Hexlet/assets/master/images/hexlet_logo128.png)](https://ru.hexlet.io/pages/about?utm_source=github&utm_medium=link&utm_campaign=python-package)

<h1 align="center">The Difference generation package</h1>

This is a hexlet courses educational project.
It shows difference between two files in json or yaml formats.
The output format of the difference between files is selected from three options, based on the user's preferences.

# The Difference generation package (gendiff-package)

[![Actions Status](https://github.com/Dmitriy-Parfimovich/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Dmitriy-Parfimovich/python-project-lvl2/actions)
![Workflow status](https://github.com/Dmitriy-Parfimovich/python-project-lvl2/actions/workflows/gendiff-check.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/d928ec050edd7bcaf754/maintainability)](https://codeclimate.com/github/Dmitriy-Parfimovich/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d928ec050edd7bcaf754/test_coverage)](https://codeclimate.com/github/Dmitriy-Parfimovich/python-project-lvl2/test_coverage)

## Description
The Difference generation package shows difference between two files in json or yaml formats. 
After installing the package, type in the command line (bash Linux):
- "gendiff -h" for help;
- "gendiff -f stylish /path/to/file/file1.json (or *.yaml) /path/to/file/file2.json (or *.yaml)" or only "gendiff /path/to/file/file1.json (or *.yaml) /path/to/file/file2.json (or *.yaml)" to use the "stylish" formatter, which generates the difference as a json structure;
- "gendiff -f plain /path/to/file/file1.json (or *.yaml) /path/to/file/file2.json (or *.yaml)" to use the "plain" formatter, which generates the difference in plain format, as if we combined the second file with the first;
- "gendiff -f json /path/to/file/file1.json (or *.yaml) /path/to/file/file2.json (or *.yaml)" to use the "json" formatter, which generates the difference as a json format for use in other programs.

## Instalation

_This is an educational project_

```sh
pip install <package>
```

## _The generate_diff module work (json):_
[![asciicast](https://asciinema.org/a/nO4uGqeFTexRbQfpKkLBTSdbQ.svg)](https://asciinema.org/a/nO4uGqeFTexRbQfpKkLBTSdbQ)

## _The generate_diff module work (yaml):_
[![asciicast](https://asciinema.org/a/BdYmPM61c4Q7L26pPeQmIHgpd.svg)](https://asciinema.org/a/BdYmPM61c4Q7L26pPeQmIHgpd)

## _The stylish module work:_
[![asciicast](https://asciinema.org/a/T1O2FXWIOKY2ahrelkZ0jREvk.svg)](https://asciinema.org/a/T1O2FXWIOKY2ahrelkZ0jREvk)

## _The plain module work:_
[![asciicast](https://asciinema.org/a/70n5Jtkk6LeMdFOrAkOxvs1La.svg)](https://asciinema.org/a/70n5Jtkk6LeMdFOrAkOxvs1La)

## _The json_output module work:_
[![asciicast](https://asciinema.org/a/b8EX8o3ggcJMCuqOvDn1OV9O9.svg)](https://asciinema.org/a/b8EX8o3ggcJMCuqOvDn1OV9O9)