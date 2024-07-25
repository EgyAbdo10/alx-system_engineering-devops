#!/bin/sh
echo "name of the file" $0
echo "first arg:" $1
echo "second arg:" $2
echo "third arg:" $3
echo "string of all args*:" $*
echo "array of args:" $@
echo "number of args:" $#
echo "the last process's id:" $!
echo "shell process id:" $$
echo "command line args of the last command or the script name:" $_