#!/usr/bin/env python

import sys
import os

# SYSTEM PARAMETERS
count_params = len(sys.argv)-1

if count_params > 1:
    function = sys.argv[2]

    if count_params > 2:

        if function == 'create-app':
            app_name = sys.argv[3]

            os.system('gatsby new '+app_name)

            os.chdir("./"+app_name)
            os.system('npm install --save node-sass gatsby-plugin-sass')

            print('new gatsby website '+reducerFileName+' created successfully!')

        else:
            print('no react function '+function+' found')
    else:
        print('params for function '+function+' missing')
else:
    print('no function called')
