#!/usr/bin/env bash

url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
output_path="projects/titanic/data/titanic.csv"
curl -o $output_path $url