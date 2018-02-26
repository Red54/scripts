#!/bin/bash
pip3 list --format=legacy --outdated
git fetch
a=`git describe --tags`
b=`curl https://api.github.com/repos/fyookball/electrum/releases/latest -s|jq .name -r`
if [ $a == $b ]; then
./electron-cash
else
echo "The Version seems too old!"
echo -e "Current version: $a"
echo -e "Latest release:  $b"
fi
