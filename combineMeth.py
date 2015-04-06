import re 
import glob 

#Loops through all files in dir and saves names
allFiles = []

for fileName in glob.iglob('data/*.txt'):
    allFiles.append(fileName)

#new file that all data will be written to
newFile = open("methylMatrix.csv","w")
newFile.write("SampleID,RHOC,RNF207,FASLG,CACNA1S,MPZ,C1orf35,C1QA,RUNX3,RFX5,MKNK1,C1QC,SPRR2D,LAMC2,DENND2C")

#list of all desired genes
genes = ["RHOC","RNF207","FASLG","CACNA1S","MPZ","C1orf35","C1QA","RUNX3","RFX5","MKNK1","C1QC","SPRR2D","LAMC2","DENND2C"]

for filename in allFiles:
    dictionary = {"RHOC":[],"RNF207":[],"FASLG":[],"CACNA1S":[],"MPZ":[],"C1orf35":[],"C1QA":[],"RUNX3":[],"RFX5":[],"MKNK1":[],"C1QC":[],"SPRR2D":[],"LAMC2":[],"DENND2C":[]}
    data = open(filename, "r")
    firstLine = data.readline()
    matchID = re.search("(TCGA-A(A|[0-9])-[0-9][0-9][0-9][0-9]-[0-9][0-9])",firstLine)
    sampleID = matchID.group()
    for line in data:
        if line.startswith("cg"):
            array = line.split()
            gene = array[2]
            betaValue = array[1]
            if gene in genes and betaValue != "NA":
                dictionary[gene].append(betaValue)
    
    newFile.write("\n")
    newFile.write(sampleID)

    for key, value in dictionary.items():
        beta = map(float,value)
        avgBeta = sum(beta)/float(len(beta))
        newFile.write(","+str(avgBeta))


newFile.close()
