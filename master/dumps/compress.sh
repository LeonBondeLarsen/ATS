#!/bin/bash
_path=$1
_dir=$(dirname $_path)
_filename=$(basename $_path)
_basename=$(echo $_filename | cut -d'.' -f1)
_extension=$(echo $_filename | cut -d'.' -f2)

mencoder -oac pcm -ovc lavc $_path -o ${_dir}/${_basename}c.$_extension
