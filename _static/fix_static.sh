#!/bin/sh

# run this script to avoid spectre from messing up lists in markdown
sed -i 's/inside//g' spectre.min.css
