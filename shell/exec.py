#!/bin/bash python3

import subprocess
import os

def cmd(cmd, start_session=False):
    if start_session:
        os.system(cmd)
        return (None, None, None)
    else:
        pipes = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        std_out, std_err = pipes.communicate()
        return (pipes.returncode != 0, std_out.strip(), std_err.strip())