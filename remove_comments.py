import glob
for filename in glob.glob('*.conf'):
    f = open(filename, 'r+')
    oldlines = f.readlines()
    f.seek(0)
    for line in oldlines:
        if line[:1]!='#':
            f.write(line)
    f.truncate()
    f.close()