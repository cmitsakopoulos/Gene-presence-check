def createdatabase(genomedirectory, databasedirectory):
  import os
  import subprocess 
  genomefiles = [x for x in os.listdir(genomedirectory) if x.endswith('.fasta')]
  for file in genomefiles: #Will create paths and names for the later command functions
    inputpath = os.path.join(genomedirectory, file)
    filename = os.path.splitext(file)[0]
    outputname = os.path.join(databasedirectory, filename)
    cmd = ['makeblastdb', '-in', inputpath, '-dbtype', 'nucl', '-out', outputname]
    subprocess.run(cmd, check=True)