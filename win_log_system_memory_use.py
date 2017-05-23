#! /usr/bin/env python

'''
Copyright (c) 2017 - Stephen Nolan


Log memory consumption on a win32 box

Produces output of the following format:

    ****[23 May 2017 - 10:51:22]****
    starting

    ****[23 May 2017 - 10:51:22]****
    Total Physical Memory:     16,327 MB
    Available Physical Memory: 4,404 MB
    Virtual Memory: Max Size:  32,652 MB
    Virtual Memory: Available: 20,045 MB
    Virtual Memory: In Use:    12,607 MB


    ****[23 May 2017 - 10:51:40]****
    Total Physical Memory:     16,327 MB
    Available Physical Memory: 4,330 MB
    Virtual Memory: Max Size:  32,652 MB
    Virtual Memory: Available: 19,974 MB
    Virtual Memory: In Use:    12,678 MB

    ...
    ...
    ...

'''

from __future__ import print_function
import subprocess
import time

# Configuration
DELAY = 5           # Delay, in seconds, between fetches of memory information


# Helper functions
def get_timestamp():
    return time.strftime('****[%d %b %Y - %H:%M:%S]****')

def get_win_memory_usage():
    return (subprocess.check_output('systeminfo | find "Memory"', shell=True)
            .decode('utf-8'))


# Runner
with open('win_log_system_memory_use_DATA.txt', 'a') as outfile:

    outfile.write(get_timestamp() + '\n' )
    outfile.write('****Starting****\n\n')
    outfile.flush()

    while (True):

         outfile.write(get_timestamp() + '\n' )
         outfile.write(get_win_memory_usage())
         outfile.flush()
     
         time.sleep(DELAY)
         outfile.write('\n\n')
