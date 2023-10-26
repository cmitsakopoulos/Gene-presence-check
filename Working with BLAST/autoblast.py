def runblast(outputpath, querypath, databasedirectory, strainnamedatabase):
 import os
 import subprocess
 from nameIDdict import idname
 from querylengthname import getlength
 queryname, sequencelength = getlength(querypath)
 generateIDs = idname(strainnamedatabase)  
 for key, value in generateIDs.items():
  outputfile = os.path.join(outputpath, f"{key}_result{queryname}.txt")
  cmd = ['blastn', '-query', querypath, '-db', value, '-outfmt', '6', '-evalue', '1e-45', '-out', outputfile]
  subprocess.run(cmd, check=True, cwd= databasedirectory)
  