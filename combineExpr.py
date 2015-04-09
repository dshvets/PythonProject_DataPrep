import re 
import glob 

allFiles = []
for fileName in glob.iglob('data/*.txt'):
    allFiles.append(fileName)

#new csv file for writing expression data to
newFile = open("exprMatrix.csv","w")
newFile.write("SampleID,RHOC,RNF207,FASLG,CACNA1S,MPZ,C1orf35,C1QA,RUNX3,RFX5,MKNK1,C1QC,SPRR2D,LAMC2,DENND2C")

genes = ["RHOC","RNF207","FASLG","CACNA1S","MPZ","C1orf35","C1QA","RUNX3","RFX5","MKNK1","C1QC","SPRR2D","LAMC2","DENND2C"]

for filename in allFiles:
    data = open(filename, "r")
    firstLine = data.readline()
    matchID = re.search("(TCGA-[0-9A-Z][0-9A-Z]-[0-9][0-9][0-9][0-9]-[0-9][0-9])",firstLine)
    sampleID = matchID.group()
    newFile.write("\n")
    newFile.write(sampleID)
    for line in data:
        if not line.startswith("Hybrid") or line.startswith("Composite"):
            array=line.split()
            gene = array[0]
            if gene in genes:
                try:
                    expr = array[1]
                    newFile.write(","+str(expr))
                except:
                    continue


newFile.close()
