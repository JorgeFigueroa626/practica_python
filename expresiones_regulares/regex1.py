import re 

text= "The quick brown fox jumps over the lazy dog"

x= re.search("^The.*dog$", text)

if x:
    print("si")
else:
    print("no")