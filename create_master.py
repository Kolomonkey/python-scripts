import glob
import os
lines_seen = set()  # holds lines already seen
outfile = open('new_config.conf', "w")
duplicatesWrite = open('duplicates.txt', 'w')

firstFile = open(glob.glob('*.conf')[0], 'r')
firstLinesUntouched = firstFile.readlines()
firstLines = set()

for line in firstLinesUntouched:
        firstLines.add(line.rstrip())


for file in glob.glob('*.conf'):

    f = open(file, 'r')
    lines = f.readlines()

    for line in lines:
        newline = line.rstrip()
        if newline in firstLines:
                duplicatesWrite.write(newline)
                duplicatesWrite.write('\n')
    f.close()

duplicatesLinesFile = open('duplicates.txt', 'r')
duplicatesLines = duplicatesLinesFile.readlines()
numLines = sum(1 for line in duplicatesLines)
numberOfFiles = len(glob.glob('*.conf'))
for controlLine in duplicatesLines:
        count = 0
        for checkLine in duplicatesLines:
                if checkLine == controlLine:
                        count = count + 1
                if count == numberOfFiles and controlLine != '\n':
                        outfile.write(controlLine)
                        break

outfile.close()
duplicatesWrite.close()
duplicatesLinesFile.close()