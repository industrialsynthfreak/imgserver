#!/usr/bin/env bash

filename=$1
system=uname

if [ system="Darwin" ]; then
    imagesnap "$filename"
elif [ system="Linux" ] || [ system="GNU" ]; then
    echo
else
    echo
fi
