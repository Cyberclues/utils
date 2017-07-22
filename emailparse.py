from collections import defaultdict
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,help="File containing email addresses (1 per line)")

args = vars(ap.parse_args())
if args['file']:
    filename = args['file'].strip()

pairs = []

with open(filename,'r') as f:
    for line in f:
        thispair = line.strip().split('@')
        pairs.append(thispair)

d = defaultdict(list)
for k,v in pairs:
    d[v].append(k)

domCount = 0
tCount = 0
for x in d:
    print "[*] Email domain: %s" % x
    domCount += 1
    for y in d[x]:
        print "\t - %s" % y
        tCount += 1

print ""
print "[*] Total Domains: %d" % domCount
print "[*] Total Users: %d" % tCount
