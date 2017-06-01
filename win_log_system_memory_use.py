#! /usr/bin/env python3

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
import argparse
import subprocess
import time


# Helper functions
def parse_arguments():

    # Create the parser
    parser = argparse.ArgumentParser(
            prog = 'win_log_system_memory_use.py',
            description = 'Log system-wide memory usage on a Windows machine',
            epilog = 'https://github.com/snolan1/windows_log_system_memory\n',
            prefix_chars = '-/',
            allow_abbrev = False)

    # Define arguments
    # NOTE: allow foward slash flags to be used as per DOS conventions
    parser.add_argument('-d', '--delay', '/d', dest='delay', type=int, 
            default=10, help='delay in seconds')
    parser.add_argument('-f', '--file', '/f', dest='output_file', 
            default='win_mem_use.txt', 
            help='Name of file in current directory to be written'
            ' out to')

    # Let ArgumentParser parse the args
    args = parser.parse_args()

    argument_dict = {}
    argument_dict['delay'] = args.delay
    argument_dict['output_file'] = args.output_file

    return argument_dict


def get_timestamp():

    return time.strftime('****[%d %b %Y - %H:%M:%S]****')


def get_win_memory_usage():

    return (subprocess.check_output('systeminfo | find "Memory"', shell=True)
            .decode('utf-8'))


    # Runner
if __name__ == '__main__':

    # Gather args
    program_arguments = parse_arguments()
    delay = program_arguments['delay']
    outfile = program_arguments['output_file']

    with open(outfile, 'a') as outfile:

        outfile.write(get_timestamp() + '\n' )
        outfile.write('****Starting****\n\n')
        outfile.flush()

        while (True):

            outfile.write(get_timestamp() + '\n' )
            outfile.write(get_win_memory_usage())
            outfile.flush()

            time.sleep(delay)
            outfile.write('\n\n')








# with open('win_log_system_memory_use_DATA.txt', 'a') as outfile:
# 
#     outfile.write(get_timestamp() + '\n' )
#     outfile.write('****Starting****\n\n')
#     outfile.flush()
# 
#     while (True):
# 
#          outfile.write(get_timestamp() + '\n' )
#          outfile.write(get_win_memory_usage())
#          outfile.flush()
#      
#          time.sleep(DELAY)
#          outfile.write('\n\n')
