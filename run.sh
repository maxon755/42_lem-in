#!/bin/sh

if [ $# -ne 1 ]; then
	echo "Usage: ./run [map]"
	exit 1
fi

if [ ! -e $1 ]; then
	echo "The file doesn't exist"
	exit 1
fi

if ./lem-in -e -p < $1 | tee temp; then
	./visual/visual.py < temp
fi

rm temp