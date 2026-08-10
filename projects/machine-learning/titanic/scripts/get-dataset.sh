#!/usr/bin/env bash

url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
output_path="projects/machine-learning/titanic/data/titanic.csv"
mkdir -p "$(dirname "$output_path")"
curl -o "$output_path" "$url"
