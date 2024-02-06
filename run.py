#!/usr/bin/env python3

import subprocess
import argparse

# parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--typeprimitive", type=str)
ap.add_argument("--b", type=str)
args = ap.parse_args()

#string to bool
b = args.b.lower() == 'true'

list_commands = ""

def runCommand(command, stdOut=None, stdErr=None, comp=None):
    """
    Run command and update the attribute list_commands
    """
    global list_commands
    p = subprocess.run(command, stderr=stdErr, stdout=stdOut)
    
    # transform convert.sh in it classic prog command (equivalent)
    command_to_save = ' '.join(['"' + arg + '"' if ' ' in arg else arg
                for arg in command ])
    if comp is not None:
        command_to_save += comp
    list_commands +=  command_to_save + '\n'
    return command_to_save


with open('output.txt', 'w') as file:           

    command_args = ['dll_decomposition', '-v', '-d', args.typeprimitive ]

    if b:
        command_args += ['-b']

    command_args += ['input_0.png']

    runCommand(command_args, file, comp = " > output.txt" )

    with open('commands.txt', 'w') as file:           
        file.write(list_commands)
