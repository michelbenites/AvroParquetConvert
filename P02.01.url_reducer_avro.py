#!/usr/bin/python
# Author : Michel Benites Nascimento
# Date   : 02/21/2018
# Descr. : Counting unique URL

import sys

# Define variables.
last_url = None
current_count = 1

# Loop in the map file.
for line in sys.stdin:
    # Gets the URL from line        
    sURL = line.strip().split('\t')
        
    # Checks if last URL is valid (!= None).
    if last_url:
        # If current URL is not equal of previous one, so add 1 to counter
        if sURL != last_url and sURL != "":
            current_count += 1
         
    last_url = sURL
    
print ("%d" % (current_count))



##import sys
##import fileinput
##from json import loads
##
##last_url = None
##current_count = 1
##
### Loop in the map file.
##for logs in sys.stdin:
##
##    line = loads(logs)
##    #line = logs
##
##    #sURL = line.strip().split('\t')
##    
##    # Gets the URL from line        
##    sURL = line['url']
##        
##    # Checks if last URL is valid (!= None).
##    if last_url:
##        # If current URL is not equal of previous one, so add 1 to counter
##        if sURL != last_url and sURL != "":
##            current_count += 1
##         
##    last_url = sURL
##    
##print ("%d" % (current_count))


##import sys
##import fileinput
##import platform
##
### Checks which platform is being in use.
##if platform.system() == "Windows":
##    inputdata = fileinput.input()
##else:
##    inputdata = sys.stdin
##
##last_url = None
##current_count = 1
##
### Loop in the map file.
##for line in inputdata:
##    # Gets the URL from line        
##    sURL = line.strip().split('\t')
##        
##    # Checks if last URL is valid (!= None).
##    if last_url:
##        # If current URL is not equal of previous one, so add 1 to counter
##        if sURL != last_url and sURL != "":
##            current_count += 1
##         
##    last_url = sURL
##    
##print ("%d" % (current_count))
