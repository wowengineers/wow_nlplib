c=raw_input("enter verb")
def make(c):
	if c.endswith("ie"):
		c=c.rstrip("ie")
		c=c+'ying'
	elif c.endswith("e"):
		c=c[:-1]
		c=c+'ing'
	elif c[-2]in 'aiou':
		c=c+c[-1]+'ing'

	print c

make(c)