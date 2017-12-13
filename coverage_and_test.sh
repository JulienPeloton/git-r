#!/bin/bash

## Script to measure the coverage of the test suite (via doctest).
## Launch it using ./coverage
## and open the html files under the folder htmlcov/
coverage run gitrconfig.py
coverage report gitrconfig.py
