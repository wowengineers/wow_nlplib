def edit_dis(x,y):
	x_l=[]
	y_l=[]
	x_l.append("@")
	y_l.append("@")
	for m in x:
		x_l.append(m)
	for n in y:
		y_l.append(n)
	m=len(x_l)
	n=len(y_l)
	d=[]
	d.append([])
	d[0].append(0)
	for i in range(1,m):
		d.append([])
		d[i].append(i)
	for j in range(1,n):
		d[0].append(j)
	for i in range(1,m):
		for j in range(1,n):
			de=d[i-1][j]+1
			insert=d[i][j-1]+1
			if(x_l[i].lower()!=y_l[j].lower()):
				subs=d[i-1][j-1]+2
			else:
				subs=d[i-1][j-1]+0
			r=min(de,insert,subs)
			d[i].append(r)
	return d[n-1][m-1]

def weightd_edit_dis(x,y):
	delete={"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1,"k":1,"l":1,"m":1,"n":1,"o":1,"p":1,"q":1,
	"r":1,"s":1,"t":1,"u":1,"v":1,"w":1,"x":1,"y":1,"z":1}
	ins={"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1,"k":1,"l":1,"m":1,"n":1,"o":1,"p":1,"q":1,
	"r":1,"s":1,"t":1,"u":1,"v":1,"w":1,"x":1,"y":1,"z":1}
	alpha_no={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,
	"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
	sub=[]
	for i in range(26):
		sub.append([])
		for j in range(26):
			sub[i].append(2)
	x_l=[]
	y_l=[]
	x_l.append("@")
	y_l.append("@")
	for m in x:
		x_l.append(m)
	for n in y:
		y_l.append(n)
	m=len(x_l)
	n=len(y_l)
	d=[]
	d.append([])
	d[0].append(0)
	val=0
	val2=0
	for i in range(1,m):
		d.append([])
		val=d[i-1][0]
		val1=val+delete.get(x_l[i])
		d[i].append(val1)
	for j in range(1,n):
		val2=d[0][j-1]
		d[0].append(val2+ins.get(y_l[j]))

	for i in range(1,m):
		for j in range(1,n):
			de=d[i-1][j]+delete.get(x_l[i])
			insert=d[i][j-1]+ins.get(y_l[j])
			if(x_l[i].lower()!=y_l[j].lower()):
				subs=d[i-1][j-1]+sub[delete.get(x_l[i])][ins.get(y_l[j])]
			else:
				subs=d[i-1][j-1]+0
			r=min(de,insert,subs)
			d[i].append(r)
	return d[n-1][m-1]


