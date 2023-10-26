import sys
import time
from querylengthname import getlength
from makingblastdatabases import createdatabase
from autoblast import runblast
from readingblast import readresults
from calculatingblast import determine

barcodenamedatabaselocation = r"C:\Users\mitsa\Desktop\Dissertation\IDname.txt" #input("Input the raw path of your bacterial strain, name and barcode tsv.txt file.: ")
querysequencelocation = r"C:\Users\mitsa\Desktop\Dissertation\ASSEMBLIESGENES\T3SS SELECT\XopX.fna" #input("Input the raw path of your query sequence.: ")
genomeassemblylocation = r"C:\Users\mitsa\Desktop\Dissertation\ASSEMBLIESGENES\PhytoBacIdent" #input("Input the raw path of your folder containing your .fasta genome assemblies.: ")
databasedesiredlocation = r"C:\Users\mitsa\Desktop\Databases" #input("Input your desired raw path of the folder in which your databases should be generated: ")
blastresultdesiredlocation = r"C:\Users\mitsa\Desktop\QueryResults" #input("Input the desired raw of the folder in which the BLAST results will be printed out in: ")
commence = input("Type True or False, to respectively abort or continue with the program: ")

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
 print("Goodbye")
 sys.exit()