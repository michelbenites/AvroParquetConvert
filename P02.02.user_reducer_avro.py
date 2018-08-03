#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/16/2018
# Descr. : Counting unique user by url

import sys
import fileinput
import platform

last_url        = None
last_user       = ""
current_count   = 1

# Checks which platform is being in use.
if platform.system() == "Windows":
    inputdata = fileinput.input()
else:
    inputdata = sys.stdin

# Loop in the log file    
for line in inputdata:
    try:
        # Gets url, user from file
        sURL, sUser, count = line.strip().split('\t')
        # Check if last URL is not "None".
        if not last_url:
            last_url    = sURL
            last_user   = sUser 
            

        # If URL is the same and the user is different add 1 to counter    
        if sURL == last_url:
            if sUser != last_user:
                current_count += int(count)
                last_user      = sUser
                 
        # If the URL has changed print the last URL and the counter.        
        else:
            print ('%s\t%d' % (last_url, current_count))
            last_url        = sURL
            last_user       = sUser
            current_count   = 1

            
    except ValueError as e:
        continue

#if current_count > 1:
print ("%s\t%d" % (sURL, current_count))
