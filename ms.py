#!/usr/bin/env python
import sys
import os

# SYSTEM PARAMETERS
count_params = len(sys.argv)-1

if count_params > 0:
    module = sys.argv[1]

    if module == 'react':
        import react.module

    if module == 'redux':
        import redux.module
        
    else:
        print(module+" not found")
        
else:
    print("no script found")
    