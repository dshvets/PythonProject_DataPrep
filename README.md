# PythonProject_DataPrep
Python for preparing TCGA data for analysis. 

Summary: 

combineMeth.py and combineExpr.py can be used to combine expression and methylation data downloaded from TCGA. Simply run the code in a directory containing all of the TCGA data in a separate folder called "data" (as written in the code). If you have a folder of a different name or you are not placing all the data in separate folder then you can change this accordingly in the code. 

Notes:

If you get the following error: "AttributeError: NoneType object has no attribute group", there is most likely an issue with the regular expression match because of differing TCGA data.  
