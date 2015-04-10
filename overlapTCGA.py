import pandas

#Open two files that need columns to match and overlap 
fileExpr = open("transposed_exprMatrix.csv","r")
fileMeth = open("transposed_methylMatrix.csv","r")

#Get first line from Expression and save it to a list 
lineOneE = fileExpr.readline()
lineOneE = lineOneE.replace("SampleID,","")
expr_IDs = lineOneE.split(",")
expr_IDs.pop()

#Get first line from Methylation and save it to a list 
lineOneM = fileMeth.readline()
lineOneM = lineOneM.replace("SampleID,","")
meth_IDs = lineOneM.split(",")
meth_IDs.pop()

#Find common sample IDs in file1 and file2 
common =[]
for x in expr_IDs:
    if x in meth_IDs:
        common.append(x)

#Find index in file1 of common sampleIDs, save to list
expr_index = []
for i in common:
    if i in expr_IDs:
        index = expr_IDs.index(i)
        expr_index.append(index)

#Find index in file2 of common sampleIDs, save to list
meth_index = []
for i in common:
    if i in meth_IDs:
        index = meth_IDs.index(i)
        meth_index.append(index)

#Close files because they will be opened later with pandas utility
fileExpr.close()
fileMeth.close()

#Add index of 1 to each number to account for the removal of sample IDs earlier
expr_index = [x+1 for x in expr_index]
meth_index = [x+1 for x in meth_index]
#Add index of 0 to beginning of each list to account for inclusion of first row in new file
expr_index.insert(0,0)
meth_index.insert(0,0)

#open file again to read from it and to re-order the columns
file1 = pandas.read_csv("transposed_methylMatrix.csv")
file2 = pandas.read_csv("transposed_exprMatrix.csv")

#Use pandas to select the columns using the indexes in meth_index and expr_index and write them to new "overlap" files
result1 = file1.iloc[:,meth_index]
result2 = file2.iloc[:,expr_index]
result1.to_csv("overlapMethyl.csv")
result2.to_csv("overlapExpr.csv")

