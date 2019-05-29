#!/bin/bash

FILENAME="/home/rudra/Documents/Portal Login_files/data.txt"
function file_exists(){
	local check=$1
	if [[ -f ${FILENAME} ]]
	then
    		if [[ -s ${FILENAME} ]]
    		then
			echo 1	
    		else
			echo 0
    		fi
	else
    		echo -1
	fi

}

check=$(file_exists)

case $check in
	1)
		cat

function login(){};

