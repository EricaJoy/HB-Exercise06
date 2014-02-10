# Open a file named on the command line
# Read line by line if possible to avoid dealing with terrible new lines
# Split the file into words by spaces
# Count each occurence of each word in the dictionary
#  by creating a key for each word, then incrementing the value
# If word isn't in the dictionary, add into

inputfile = open('inputfile.txt')
inputlist = []

for line in inputfile:
    inputlist.extend(line.split(' ')) 

# Counts the words!
wordcount = {}
for word in inputlist:
    word = word.strip()
    if wordcount.get(word):
        wordcount[word] += 1
    else:
        wordcount[word] = 1
for key, value in wordcount.iteritems():
    print key, value