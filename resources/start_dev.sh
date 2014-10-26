#!/bin/bash

# the fproj, sproj, etc are aliases and are set in ~/.bash_profile like so:
#
# alias aproj="cd /home/nick/dev/django/projects/aerial-solutions/aersol"
# alias sproj="cd /home/nick/dev/django/projects/serupbot/serupbot"
# 
# this illustrates one project using a non-default settings file...
#
# run this script like this:
# source start_dev.sh <project_name>

# eg:
# source start_dev.sh aesrol

# first command line argument
project=$1

echo "starting apache and mysql..."

# add your path here (to your lamp startu script)
# this command is optional if starting pure Django dev environment
# it's useful if needing an app like phpMyAdmin for SQL admin
bash /home/nick/dev/lamp/ctlscript.sh start

echo "determining project and working directories..."

if [ "${project}" == "aersol" ];
then
    echo "project is ${project} ... using alias aproj..."
    aproj
    settings="${project}.settings.local"

elif [ "${project}" == "serupbot" ];
then
    echo "project is ${project} ... using alias sproj..."
    sproj
    settings=""
    
fi

function start_server {

    if [ "${settings}" != "" ];
    then
        args="--settings=${settings}"
        echo "args for ${project} are ${args}"

    else
        args=""
        echo "args for ${project} are ${args}"
    fi

    workon "${project}"
    
    echo "working on ${project}"
    echo "starting server..."
    
    python manage.py runserver $args
}

start_server

unset project
unset args
unset settings
