""" **Scenario:** Your company needs to learn about the files located on various machines. You have been asked to build a script that extract the 
information such as the name and size about the files in the current working directory and stores it in a list of dictionaries. The solution is to create a python  script that generates a list of dictionaries files in the working directory and print the list for further analysis."""

# !/usr/bin/env python 3
# Generate a list of files in the current working directory
# sort by file name and specify file size in bytes

import os
CurrentDir = os.getcwd()
Files = sorted(os.listdir(CurrentDir))

cwdDict = dict()
for info in Files:
  Stats = os.stat(Info)
  cwdDict(Info) = Stats

for item in cwdDict:
  print("{:40s} {:d} bytes".format(item.cwdDict[item].st_size))
  
  # The above python script returns all the files located in the current working directory, sorted by name and specifying the size of file in bytes.
  
  
