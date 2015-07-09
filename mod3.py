def apos(string):
    import re
    if re.findall(r"[nN]['][tT]", string):
        string = re.sub("[nN]'[tT]", " not",  string).split()
        string=' '.join(string)
    if re.findall(r"['][rR][Ee]", string):
        string = re.sub("['][rR][Ee]", " are",  string).split()
        string=' '.join(string)
    if re.findall(r"['][mM]", string):
        string = re.sub("['][mM]", " am",  string).split()
        string=' '.join(string)
    if re.findall(r"['][lL][lL]", string):
        string = re.sub("['][lL][lL]", " will",  string).split()
        string=' '.join(string)
    if re.findall(r"['][dD]", string):
        string = re.sub("['][dD]", " would",  string).split()
        string=' '.join(string)
    return string
text=raw_input("Enter text")
print apos(text)

