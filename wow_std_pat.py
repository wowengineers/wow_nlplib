import re 
from collections import Counter
#tokenize function returns dictionary of tokens and their number
def wow_tokenize(string):
	wordList = re.sub("[.][^A-Za-z0-9]|[" "]|[,]|\.$", " ",  string).split()
	count=Counter(wordList)
	return count
#match_w function matches and returns different form of words with their counts
def wow_match_w(string,line):
	line=re.sub('\.','. ',line)
	line=wow_tokenize(line)
	i=0
	a=len(string)
	key_ls=[]
	str_ls=[]
	result={}
	for key in line.keys():
		len_key=len(key)
		if (len_key>=a):
			key_ls=[]
			ls=[]
			count=0
			for i in range(0,a):
				str_ls.append(string[i])
				key_ls.append(key[i])
			ls=key_ls	
			for i in range(0,a):
				if key_ls[0].lower()!=str_ls[0].lower():
					break
				if str_ls[i].lower()==key_ls[i].lower():
					count+=1
			per=(count/float(a))*100
			if(a>7):
				if per>=60:
					result[key]=line[key]

			else:
				if per>=55:
					result[key]=line[key]
		else:
			if a>7:
				avg_len=int(a*0.4)
			else:
				avg_len=int(a*0.7)
			if(len_key>=avg_len):
				key_ls=[]
				ls=[]
				count=0
				for i in range(0,avg_len):
					str_ls.append(string[i])
					key_ls.append(key[i])
				ls=key_ls	
				for i in range(0,avg_len):
					if key_ls[0].lower()!=str_ls[0].lower():
						break
					if str_ls[i].lower()==key_ls[i].lower():
						count+=1
				per=(count/float(avg_len))*100
				if len_key>6:
					if per>=60:
						result[key]=line[key]
				else:
					if per>=85:
						result[key]=line[key]
	return result					
#correct returns the string after removing extra spaces						
def wow_correct(c):
	s=""
	s= re.sub('\ +',' ',c)
	s=re.sub('\.','. ',s)
	s=re.sub('[^A-Za-z0-9" "]','',s)
	return s
#match_l returns lines matching with given pattern
def wow_match_l(string,line):
	string=wow_correct(string)
	line=wow_correct(line)
	matchObj = re.findall( string,line, re.M|re.I)
	b=len(re.findall( string,line, re.M|re.I))
	if matchObj:
		return matchObj,"occurences:", b
	else:
		return "No match!!"
	
	
#match funcion returns the matching pattern
def wow_match(string,line):
	string=string.strip()
	p=0
	for i in string:
		if i==" ":
			p=1
			break
	if p==0:
		word_num=wow_match_w(string,line)
		return word_num
	else:
		line_num=wow_match_l(string,line)
		return line_num
#check_file puts whole file in string variable
def wow_check_file(mfile):
	with open (mfile, "r") as myfile:
		data=myfile.read().replace('\n', '')
	return data
#segment function returns the sentences in string and their total count	
def wow_segment(string):
    wordList = re.split(r'(?<=[^A-Z].[.?!]) +(?=[A-Z])', string)
    length=len(wordList)
    return length,wordList
#file_str function matches the string over whole file
def wow_file_str(mfile,string):
	data=wow_check_file(mfile)
	return wow_match(string,data)
#file_seg returns list of sentences in file and their count
def wow_file_seg(mfile):
	data=wow_check_file(mfile)
	return wow_segment(data)

