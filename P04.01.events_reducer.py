#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/23/2018
# Descr. : Reducer url and day.

import sys
import fileinput
import platform

# Set the variables.
last_hour     = None
current_count = 0

# Checks which platform is in use.
if platform.system() == "Windows":
    inputdata = fileinput.input()
else:
    inputdata = sys.stdin
    
# Loop in the log file    
for line in inputdata:
    try:
        # Split the line to get hour, url and user
        surl, shour, count = line.strip().split('\t')
        # Check if currente URL is not "None".
        if not last_hour:
            last_hour = shour
            last_url  = surl
            
        # If hour, url and user are the same as the previous ones, so add 1 to counter 
        if shour == last_hour:
            current_count += 1
        else:
            # Else print the last values.
            print ('%s %s\t%s %s\t%s %d' % ('Url:',last_url, 'Date/Hour:', last_hour, 'count:', current_count))
            last_hour     = shour
            current_count = 1          
        
    except ValueError as e:
        continue

#if current_count > 1:
print ('%s %s\t%s %s\t%s %d' % ('Url:',last_url, 'Date/Hour:', last_hour, 'count:', current_count))            
