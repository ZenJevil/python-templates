import os
import sys

templateFile = sys.argv[1]

if templateFile.endswith(".template"):
    with open(templateFile, 'r+') as template:
        templateContents = template.read()
        template.close()

    fileName = templateFile.strip('.template')

    file = open('generatedTemplate.py', 'w+')

    file.write(templateContents)
