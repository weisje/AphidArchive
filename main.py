#(26/08/2021 -JW)
#**IMPORT BLOCK**(26/08/2021 -JW)
import os
import datetime

#**LAMBDA BLOCK**(26/08/2021 -JW)
pathLambda = lambda varA, varB : os.path.join(varA, varB)

#**FUNCTION BLOCK**(26/08/2021 -JW)
def timeConvert(epochTime):
    inputTime = epochTime
    outputTime = datetime.datetime.fromtimestamp(inputTime)
    return outputTime

def main():
    inputFilePath = #Insert path to be crawled as quoted string(26/08/2021 -JW)
    outputFileName = #Insert filename to have data outputted to(26/08/2021 -JW)
    outputFilePath = #Insert filepath without filename for data to be outputted to(26/08/2021 -JW)
    outputFullFile = outputFilePath + outputFileName
    counter = 0

    editMode = "a"

    fileOpen = open(outputFullFile, editMode)

    for (dirpath, dirname, filenames) in os.walk(inputFilePath):
        if(counter%500 == 0):
            print(counter)
        try:
            for f in filenames:
                fFilePath = pathLambda(dirpath, f)
                fileStatsObj = os.stat(fFilePath)
                timeOfAccess = timeConvert(fileStatsObj[7])
                timeOfMod = timeConvert(fileStatsObj[8])
                timeOfCreate = timeConvert(fileStatsObj[9])
                fileOpen.write("FILE" + "," + '\"' + fFilePath + '\"' + "," + '\"' + str(f) + '\"' + "," + str(fileStatsObj[0]) + "," + str(fileStatsObj[1]) + "," + str(fileStatsObj[2]) + "," + str(fileStatsObj[3]) + "," + str(fileStatsObj[4]) + "," + str(fileStatsObj[5]) + "," + str(fileStatsObj[6]) + "," + str(timeOfAccess ) + "," + str(timeOfMod) + "," + str(timeOfCreate) + "\n")
            for d in dirname:
                dFilePath = pathLambda(dirpath, d)
                fileStatsObj = os.stat(dFilePath)
                timeOfAccess = timeConvert(fileStatsObj[7])
                timeOfMod = timeConvert(fileStatsObj[8])
                timeOfCreate = timeConvert(fileStatsObj[9])
                fileOpen.write("DIRECTORY" + "," + '\"' + dFilePath + '\"' + "," + '\"\"' + "," + str(fileStatsObj[0]) + "," + str(fileStatsObj[1]) + "," + str(fileStatsObj[2]) + "," + str(fileStatsObj[3]) + "," + str(fileStatsObj[4]) + "," + str(fileStatsObj[5]) + "," + str(fileStatsObj[6]) + "," + str(timeOfAccess) + "," + str(timeOfMod) + "," + str(timeOfCreate) + "\n")
        except:
            continue
        counter +=1

if __name__ == '__main__':
    main()
