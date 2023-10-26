#This program reads indexes with the presupposition that the BLAST query has been formatted with: outfmt 6. 
import os
from nameIDdict import idname

def readresults(idnamedir, assemblyresultsdir):
    namesbarcodedict = idname(idnamedir)
    results = {}
    filesindir = os.listdir(assemblyresultsdir)
    for file in filesindir:
        extendeddir = os.path.join(assemblyresultsdir, file)
        for key, value in namesbarcodedict.items():
            if key in file:  
                with open(extendeddir) as result:
                     for line in result:
                         linesplit = line.split('\t')
                         results[key] = linesplit
    return results







