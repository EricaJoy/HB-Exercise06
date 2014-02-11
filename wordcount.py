# Open a file named on the command line
# Read line by line if possible to avoid dealing with terrible new lines
# Split the file into words by spaces
# Count each occurence of each word in the dictionary
#  by creating a key for each word, then incrementing the value
# If word isn't in the dictionary, add into
import sys

# Get the file path from command line
thefile = sys.argv[1] 

# Open the file and read to var inputfile
f = open(thefile)
inputfile = f.read()

# split the text from inputfile into list inputlist
inputlist = inputfile.split()

# instantiate the wordlist list
wordlist = []

# split the values in inputlist on -- and store to list wordlist 
for line in inputlist:
    wordlist.extend(line.split('--')) 

# Counts the words!
wordcount = {}
for word in wordlist:
    word = word.strip('_-:;.,?!\'()" ').lower()
    if wordcount.get(word):
        wordcount[word] += 1
    else:
        wordcount[word] = 1

# Turn the wordcount dictionary into a list of tuples called countlist
countlist = wordcount.items()

# Sort the list of tuples by alpha
countlist.sort()

# Create reversed_list, swap the positions of key, value in countlist
reversed_list = []
for word, frequency in countlist:
    reversed_list.append((frequency, word))

# Sort the list by frequency and reverse it
reversed_list.sort()
reversed_list.reverse()

# Make things spew on the screen
for frequency, word in reversed_list:
    print word, frequency