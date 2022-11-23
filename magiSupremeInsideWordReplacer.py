#Python 2.7
## magiSupremeInsideWordReplacer version 1.9999-desa

#Editar:
#folder target newWord *.ext

import os, fnmatch

def findReplace(directory, find, replace, filePattern):
    contador = 0
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):

            filepath = os.path.join(path, filename)

            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)
                contador += 1
                print("Archivo leido: "+filepath)

    print("Total de archivos leidos: "+str(contador))

findReplace("folder", "friendly", "-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX-", "*.txt")
