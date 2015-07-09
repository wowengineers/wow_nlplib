def tokenize(string):
    import re
    from collections import Counter
    wordList = re.sub("[.][^A-Za-z0-9]|[" "]|[,]|\.$", " ",  string).split()
    count=Counter(wordList)
    return count
text=raw_input("Enter text")
print tokenize(text)

