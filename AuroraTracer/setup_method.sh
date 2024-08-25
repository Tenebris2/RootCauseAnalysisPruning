#!/bin/bash

dir=$1

path="$HOME/Disk/Documents/RootCauseAnalysis/evaluation/pin-3.15-98253-gb56e429b1-gcc-linux/source/tools/AuroraTracer/"
cp ${dir} ${path}

cd $path 

make

cd $OLDPWD
