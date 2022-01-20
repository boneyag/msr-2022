# Using the repository

## Directory structure
There three directories in this repo. 
1. `annotations` contains an excel file which consists of annotated data by each author. 
2. `dataPreparation` contain scripts and Json dumps to prepare the spreadsheet for annotations. Since we randomly select question IDs from Json, Django, and Regex you may not be able to reproduce work exactly. 
3. `stat` contains data files and scripts to calculate Fleiss Kappa scores and analyse other data.

A readme file in each directory contain additional information.
