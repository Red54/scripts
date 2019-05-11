#!/bin/bash
pip3 list --outdated
git fetch
a=`git describe --tags`
b=`curl https://api.github.com/repos/Electron-Cash/Electron-Cash/releases/latest -s|jq .tag_name -r`
if [ "$a" == "$b" ]; then
./electron-cash
else
echo "The Version seems too old!"
echo -e "Current version: $a"
echo -e "Latest release:  $b"
fi
