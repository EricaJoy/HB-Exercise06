# Open a file named on the command line
# Read line by line if possible to avoid dealing with terrible new lines
# Split the file into words by spaces
# Count each occurence of each word in the dictionary
#  by creating a key for each word, then incrementing the value
# If word isn't in the dictionary, add into


inputfile = """As I was going to St. Ives I met a man with seven wives Every wife had seven sacks Every sack had seven cats Every cat had seven kits Kits, cats, sacks, wives. How many were going to St. Ives?"""

inputlist = inputfile.split(' ')
wordcount = {}
for word in inputlist:
    if wordcount.get(word):
        wordcount[word] += 1
    else:
        wordcount[word] = 1
for key, value in wordcount.iteritems():
    print key, value