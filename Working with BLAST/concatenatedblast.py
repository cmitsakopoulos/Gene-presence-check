import sys
import time
from querylengthname import getlength
from makingblastdatabases import createdatabase
from autoblast import runblast
from readingblast import readresults
from calculatingblast import determine

barcodenamedatabaselocation = #Input raw path to txt file containing two tab separated columns, the strain barcodes on the left and the strain names on the right.
querysequencelocation = #Input raw path of query .fasta sequence youy want to run against your set of genome assemblies.
genomeassemblylocation = #Input raw path of the folder containing your genome assemblies, ensure that they end with .fasta, otherwise ammendements need to be made in the makeblastdatbases program, ro change .endswith from .fasta to .fna.
databasedesiredlocation = #Input raw  path of an empty folder in which you would want your databases to be collected in.
blastresultdesiredlocation = #Input raw path of of an empty folder in which the result.txt files of BLAST will be collected in.
commence = input("Type True or False, to respectively continue or abort with the program: ")

if commence == "True":
 print("Commencing query sequence analysis")
 queryname, querylength = getlength(querysequencelocation)
 print("Query sequence analysis complete")
 time.sleep(0.5)
 print("Commencing database creation")
 makedatabases = createdatabase(genomeassemblylocation, databasedesiredlocation)
 print("Databases created")
 time.sleep(0.5)
 print("Commencing blast searches")
 blastwork = runblast(blastresultdesiredlocation, querysequencelocation, databasedesiredlocation, barcodenamedatabaselocation)
 print("Blast search complete")
 time.sleep(0.5)
 print("Reading blast results")
 blastresults = readresults(barcodenamedatabaselocation, blastresultdesiredlocation)
 print("Blast results read")
 time.sleep(0.5)
 print("Calculating results, generating gene prsence list")
 final = determine(querysequencelocation, blastresultdesiredlocation, barcodenamedatabaselocation)
 print("Processing finished, program will exit, a csv file will be available")

else: 
 print("Program will now shut down")
 sys.exit()
