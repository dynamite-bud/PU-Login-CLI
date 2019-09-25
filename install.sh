#!/bin/bash
count=1
pyV1=`python3 --version | cut --delimiter=" " --fields 2 | cut --delimiter="." --fields=1`
pyV2=`python3 --version | cut --delimiter=" " --fields 2 | cut --delimiter="." --fields=2`

if [ $pyV1 -ne 3 ] && [ $pyV2 -lt 6 ];then
	echo "[$count] Python Version $pyV1.$pyV2 not supported"
	exit -1
fi


currDir=`pwd`
file=".bash_aliases"
echo "[$count] Checking for .bash_aliases"
let "count++"


if [ -f ~/$file ];then
	echo "[$count] $file found"
	let "count++"
	echo "#The next two lines are for Pulogin" >> ~/$file
	echo "alias pulogin='python3 $currDir/pulogin.py'" >> ~/$file
	echo "alias pulogout='python3 $currDir/pulogout.py'" >> ~/$file
	echo "[$count] Successful! Now type pulogin for login and pulogout for logout in shell"
	source ~/.bashrc
	exit 0
else	
	echo "[$count] $file not found"
	let "count++"
	echo "[$count] Creating $file in ~/ directory"
	let "count++"
	touch ~/$file
	echo "#The next two lines are for Pulogin" >> ~/$file
	echo "alias pulogin='python3 $currDir/pulogin.py'" >> ~/$file
	echo "alias pulogout='python3 $currDir/pulogout.py'" >> ~/$file
	echo "[$count] Successful! Now type pulogin for login and pulogout for logout in shell"
	source ~/.bashrc
	exit 0
fi

