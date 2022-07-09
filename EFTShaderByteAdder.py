""" 
    script to read file size of all files 
    in a folder and put them in an array
    os is used to get file paths and their sizezs
    randbytes from random is used to add random bytes
    at the end of the file to bypass the frugal EFT anticheat
    made by Pieseu#4001
"""

import os
from random import randbytes


u = -1
arrayOfSizes = []
arrayOfReals = []
nameArray = []

# path of replaced files
path = "C:\\Users\\Pie\\Downloads\\EFT-Pak-ESP-1.0\\EFT-Pak-ESP-1.0\\prefabs\\"
appendPathforFake = "C:\\Users\\Pie\\Downloads\\EFT-Pak-ESP-1.0\\EFT-Pak-ESP-1.0\\prefabs\\"

# path of real files for comparison
appendPathforReal = "C:\\Users\\Pie\\Downloads\\EFT-Pak-ESP-1.0\\EFT-Pak-ESP-1.0\\realfiles\\"
realPath = "C:\\Users\\Pie\\Downloads\\EFT-Pak-ESP-1.0\\EFT-Pak-ESP-1.0\\realfiles\\"

dir_list = os.listdir(path) 

for i in dir_list:
    """
        appends full path to every file in array
        then checks size of each and appends them to array of arrayOfSizes
        to then be used for comparison on later loop
    """

    pathOfFile = appendPathforFake + i
    checkSize = os.stat(pathOfFile)
    arrayOfSizes.append(checkSize.st_size)
    nameArray.append(os.path.basename(i))


realDirList = os.listdir(realPath)
for x in realDirList:
    """
        appends full path to every file in array
        checks size of each and appends to array arrayOfReal
    """

    pathOfReal = appendPathforReal + x
    checkSizeReal = os.stat(pathOfReal)
    arrayOfReals.append(checkSizeReal.st_size)


for y in range(len(arrayOfReals)):
    difference = arrayOfReals[y] - arrayOfSizes[y]
    print("The file", nameArray[y], "needs", difference, "additional bytes")

def replaceShader(inputFile, originalShaderBytes):
    """
        not my code i really dont know what it does 
        it overwrites some bytes if they're missing
    """

    os.truncate(inputFile, originalShaderBytes)
    with open(inputFile, "ab") as f:
        f.write(randbytes(9999999))
    os.truncate(inputFile, originalShaderBytes)

for b in dir_list:
    u += 1  
    replaceShader(appendPathforFake + b, arrayOfReals[u])




