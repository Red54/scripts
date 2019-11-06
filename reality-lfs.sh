#!/bin/bash
cmd='git lfs migrate import --exclude-ref=lfs -I documentation/rug/3DScenes/Projector.pz3'
for branch in $(git branch --format='%(refname:lstrip=2)'); do
	if [[ $(git log $branch -- documentation/rug/3DScenes/Projector.pz3) ]]; then
		cmd="$cmd --include-ref=$branch"
	fi
done
echo $cmd
