import os
import sys

templateFile = sys.argv[1]
templateFileExtension = sys.argv[2]

if templateFile.endswith(".template"):
    with open(templateFile, 'r+') as template:
        templateContents = template.read()
        template.close()

    fileName = templateFile.strip('.template')

    file = open(f'generatedTemplate.{templateFileExtension}', 'w+')

    file.write(templateContents)
