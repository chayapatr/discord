#!/bin/bash
rm ./DONTFUCKINGTOUCHTHIS -rf > /dev/null
rm ./grader/out > /dev/null
rm ./grader/code.py > /dev/null
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf > /dev/null