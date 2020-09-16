#!/bin/bash
set -eu

if pytest; 
then 
    git commit -am "${1}"
fi