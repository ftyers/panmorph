#!/bin/bash

# insert space before
# and after
# undo if these are inbetween numbers

# tokenize these at the beginning of word
# tokenize these at the end of word

# squash space
# insert the token boundary

sed -E 's/([^ \t])([-+“‘”"/()*?!;.:,])/\1 \2/g' | 
sed -E 's/([-+/“‘”"()*?!;.,:])([^ \t])/\1 \2/g' | 
sed -E 's/([0-9]) +([.,:]) +([0-9])/\1\2\3/g' | 

sed -E 's/([ \t])([`'\''])([^ \t])/\1\2 \3/g' | 
sed -E 's/([^ \t])(['\''’])([ \t])/\1 \2\3/g' | 


tr '\t' ' ' | tr ' ' '\n'