#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/21/2018
# Descr. : Counting user Clicks by URL

import sys
import fileinput
import platform

# Checks which platform in order to select fileinput correctly.
if platform.system() == "Windows":
    inputdata = fileinput.input()
else:
    inputdata = sys.stdin
    
# Defines variables
last_url        = None
last_user       = ""
current_count   = 0

    
for line in inputdata:
    try:
        sURL, sUser, click = line.strip().split('\t')
        # Check if currente URL is not "None".
        if not last_url:
            last_url    = sURL
            last_user   = sUser 

        # If URL and User are the same as the last so add 1 to counter    
        if sURL == last_url and sUser == last_user:
            current_count += 1
        else:
            # Else print the url, user and counter.
            print ('%s\t%s\t%d' % (last_url, last_user, current_count))
            last_url        = sURL
            last_user       = sUser
            current_count   = 1

    except ValueError as e:
        continue

#if current_count > 1:
print ('%s\t%s\t%d' % (sURL, sUser, current_count))
