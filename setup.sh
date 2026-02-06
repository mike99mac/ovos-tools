#!/bin/bash
#
# setup.sh - Install ovos-tools scripts in ./usr/local/sbin to the real /usr/local/sbin
# 
#+--------------------------------------------------------------------------+
# copy all files from the git clone to /usr/local/sbin
echo "Copying all scripts to /usr/local/sbin ..."
cmd="sudo cp usr/local/sbin/* /usr/local/sbin/"
$cmd
rc=$?
if [ "$rc" != 0 ]; then                  # error
  echo "ERROR: command $cmd returned $rc" 
  exit 2
fi
cmd="sudo chown $USER:$USER /usr/local/sbin/*"
$cmd
rc=$?
if [ "$rc" != 0 ]; then                  # error
  echo "ERROR: command $cmd returned $rc" 
  exit 3
fi
echo "Success! /usr/local/sbin/ directory:"
ls -l /usr/local/sbin/
