fname = input("Enter file name: ")
fhandle = open(fname)
wordsinline = list()
time = list()
hours = list()

# Creating a list of time stamps
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From '):
        wordsinline = line.split()
        time.append(wordsinline[5])

# Creating a list of the hours in the time stamp
for bigtime in time:
    x = bigtime.split(':')
    hours.append(x[0])

# Create histogram
histogram = {}
for key in hours:
    histogram[key] = histogram.get(key,0) + 1

# Print out the tuples sorted by hour
for k,v in sorted(histogram.items()):
    print(k,v)
