#!/usr/bin/env python

import sys
import os

# SYSTEM PARAMETERS
count_params = len(sys.argv)-1

if count_params > 1:
    function = sys.argv[2]

    if count_params > 2:

        if function == 'create-reducer':
            reducerFileName = sys.argv[3]

            sep = ""
            reducerName = sep.join(list(map(lambda text: text.capitalize(), reducerFileName.split('-'))))
            templatesFolder = os.path.dirname(os.path.realpath(__file__))+'\\templates\\'

            os.chdir("./src/redux")
            os.mkdir(reducerName)
            os.chdir(reducerName)

            f = open(templatesFolder+"reducer.txt", "r")
            reducerTemplate = f.read()
            f.close()

            f = open(templatesFolder+"actions.txt", "r")
            actionsTemplate = f.read()
            f.close()

            f = open(templatesFolder+"types.txt", "r")
            typesTemplate = f.read()
            f.close()

            reducerTemplate = reducerTemplate.replace('%-REDUCER_FILE_NAME-%', reducerFileName)
            reducerTemplate = reducerTemplate.replace('%-REDUCER_NAME-%', reducerName)

            actionsTemplate = actionsTemplate.replace('%-REDUCER_FILE_NAME-%', reducerFileName)


            f = open(reducerFileName+".reducer.js", "a")
            f.write(reducerTemplate)
            f.close()

            f = open(reducerFileName+".actions.js", "a")
            f.write(actionsTemplate)
            f.close()

            f = open(reducerFileName+".types.js", "a")
            f.write(typesTemplate)
            f.close()

            f = open(reducerFileName+".utils.js", "a")
            f.write("")
            f.close()

            print('redux reducer '+reducerFileName+' created successfully!')

        else:
            print('no react function '+function+' found')
    else:
        print('params for function '+function+' missing')
else:
    print('no function called')
