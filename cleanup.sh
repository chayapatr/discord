#!/bin/bash
rm ./DONTFUCKINGTOUCHTHIS/*
rm ./DONTFUCKINGTOUCHTHIS/__pycache__/ -rf
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf