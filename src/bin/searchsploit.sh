#!/bin/bash
# exploitdb CLI search tool

csvpath=/pentest/exploitdb/files.csv

USAGE="Usage: `basename $0` [term1] [term2] [term3]\nExample: `basename $0` oracle windows local\n\nUse lower case in the search terms; second and third terms are optional.\n`basename $0` will search each line of the csv file left to right so order your search terms accordingly.\n(ie: 'oracle local' will yield better results than 'local oracle')"

if [ $# -eq 0 ]; then
	echo -e $USAGE >&2
	exit 1
fi


echo " Description                                                                 Path"
echo --------------------------------------------------------------------------- -------------------------

awk -F "\"*,\"*" '{printf "%-75s %s\n", $3, $2}' $csvpath | awk 'tolower($0) ~ /'$1'/ && /'$2'/ && /'$3'/' | sed s/platforms//

# You can change the identation on the path by changing the "75" above to something that suits your fancy
# (ie: screen columns) 75 columns seemed a good compromise, a few lines will get truncated, but hey...
# ideas and threats: nuno@freelancesamurai.com, backtrack forums or find me at freenode (sygo).
