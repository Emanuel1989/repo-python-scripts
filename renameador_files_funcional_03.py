import glob
import os
import sys

#Python 3
## renameador_files_funciona_03 version 1.2-desa

print("Este script utiliza Python3")

ext_var = input("Con que extension desea trabajar? (txt, java, xml, etc): ")
deletos_var = input("Termino a reeplazar: ")
newterm_var = input("Nuevo termino: ")
contador = 0

#print(ext_var + "A")
#print(deletos_var + "B")
#print(newterm_var + "C")

for f in glob.glob('*.'+ext_var):
    new_filename = f.replace(deletos_var,newterm_var)
    #new_filename = "kml_" + new_filename
    os.rename(f,new_filename)
    contador+=1
    print("Archivo modificado: "+f)

print("Total de archivos renombrados: "+str(contador))    
