import sys

# 1. Attempt to open a file
name = input("Enter a name of an existing text file: ").strip()
try:
    infile = open(name)
except (FileNotFoundError, IsADirectoryError):
    print("Cannot open file {}".format(name))
    sys.exit()

# 2. Read the file and eliminate the dups
words = set() # Keep the vocabulary in a set
text = []
for line in infile:
    for word in line.split():
        if word.upper() not in words: # A new word!
            words.add(word.upper())
            text.append(word)
    text.append("\n") # To preserve the line structure

# 3. Write text to another file
ofilename = "nodups-{}".format(name)
try:
    with open(ofilename, "w") as outfile:
        outfile.write(" ".join(text))
except (FileNotFoundError, IsADirectoryError):
    print("Cannot open file {}".format(ofilename))
    sys.exit()
