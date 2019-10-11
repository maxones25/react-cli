#!/usr/bin/env python
import sys
import os

# SYSTEM PARAMETERS
count_params = len(sys.argv)-1

if count_params == 0:
    print("no script found")
else:
    module = sys.argv[1]

    if module == 'react':
        import react.module
        
    else:
        print(module+" not found")
    