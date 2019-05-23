#!/bin/sh
pygmentize -O full,style=monokai -o flash.svg flash.py ; google-chrome flash.html
