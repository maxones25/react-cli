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

            # os.system('npx create-react-app '+app_name)

            # os.chdir("./"+app_name)
            # os.system('npm i redux')
            # os.system('npm i react-redux')
            # os.system('npm i react-router-dom')
            # os.system('npm i node-sass')

            # os.chdir("./src")
            # os.mkdir("components")
            # os.mkdir("pages")
            # os.mkdir("redux")

        elif function == 'create-fun-comp':
            name = sys.argv[3]
            
            sep = ""
            componentDirname = sep.join(list(map(lambda text: text.capitalize(), name.split('-'))))
            os.chdir("./src/components")
            os.mkdir(componentDirname)

            componentName = name
            os.chdir("./"+componentDirname)

            templatesFolder = os.path.dirname(os.path.realpath(__file__))+'\\templates\\'
            f = open(templatesFolder+"function-component.txt", "r")
            componentTemplate = f.read()
            f.close()

            componentTemplate = componentTemplate.replace('%-STYLESHEET-%', name)
            componentTemplate = componentTemplate.replace('%-COMPONENT_NAME-%', componentDirname)
     
            f = open(name+".component.jsx", "a")
            f.write(componentTemplate)
            f.close()

            f = open(name+".styles.scss", "a")
            f.write("")
            f.close()

            print('function component '+name+' created successfully!')

        else:
            print('no react function '+function+' found')
    else:
        print('params for function '+function+' missing')
else:
    print('no function called')
