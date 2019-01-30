import glob
lines_seen = set()  # holds lines already seen
outfile = open('../new_config.conf', "w")

for file in glob.glob('*.conf'):
    f = open(file, 'r')
    lines = f.readlines()

    for line in lines:
        newline = line.rstrip()
        if newline not in lines_seen:  # not a duplicate
                outfile.write(line)
                lines_seen.add(line.rstrip())
    f.close()

outfile.close()