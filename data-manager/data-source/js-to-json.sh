#!/bin/sh

# WARNING: This script will give you cancer
# No, seriously. 
# We use Tommy's Teambuilder as source of our data. They have prepared
# JavaScript objects with information about all Pokemon, Moves and
# Pokemon-Moves maps. The problem is, JavaScript object is close to
# JSON, but not quite there. No JSON library in Python could read
# these files as-is.
# Since reading internal JavaScript objects is not task commonly
# solved by languages other than JavaScript, we resort to use
# NodeJS (!) to read object from file, serialize it as JSON and
# write it back.
# And since NodeJS expects certain structure from its modules,
# we rewrite files before processing them.

if [ "$1" = "-f" ] || [ "$1" = "--force" ]; then
	FORCE=1
fi

for filename in pokedex-sumo.js moves-sumo.js learnsets-sumo.js; do
	if [ ! -e "$filename" ] || [ ! -z "$FORCE" ]; then
		wget "http://pyrotoz.com/${filename}" -O "${filename}"
	fi
	sed -i -e '1 s:.*= {:exports.data = {:' "$filename"
	output_filename="${filename}on"
	nodejs --use_strict -e 'const fs = require("fs");
		var data = require("./'$filename'");
		fs.writeFileSync("'$output_filename'", JSON.stringify(data));'
done
