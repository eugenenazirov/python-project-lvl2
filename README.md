###### Hexlet tests and linter status:
[![Actions Status](https://github.com/eugenenazirov/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/eugenenazirov/python-project-lvl2/actions)
[![Linter (flake8)](https://github.com/eugenenazirov/python-project-lvl2/actions/workflows/linter.yml/badge.svg?event=push)](https://github.com/eugenenazirov/python-project-lvl2/actions/workflows/linter.yml)
[![Auto-Tests (pytest)](https://github.com/eugenenazirov/python-project-lvl2/actions/workflows/tests.yml/badge.svg?event=push)](https://github.com/eugenenazirov/python-project-lvl2/actions/workflows/tests.yml)

###### Code Coverage by codeclimate
[![Test Coverage](https://api.codeclimate.com/v1/badges/20ba8352a3dd94528a80/test_coverage)](https://codeclimate.com/github/eugenenazirov/python-project-lvl2/test_coverage)

---

# Generate Diff
The cli tool for generating difference between two files. Almost like `git diff`.
Supports .json and .yaml files.
Output formats: stylish (default), plain & json.

Requirements: 
- Python ^3.10,
- pip ^22.1

Install the package with `pip install` and `*repository cloning https link*`.


### Demo
Plain .json files
https://asciinema.org/a/509502

Plain .yaml files
https://asciinema.org/a/510950

Nested .json and .yaml files (recursive diff)
https://asciinema.org/a/513886

Plain output format for nested .json and .yaml
https://asciinema.org/a/513898

Json output format for nested .json and .yaml
https://asciinema.org/a/514127
