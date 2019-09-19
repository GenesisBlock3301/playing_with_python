#1st way:
def isString(string,substring):
	index = 0
	if substring in string:
		c = substring[0]
		for char in string:
			if char == c:
				if string[index:index+len(substring)] == substring:
					return index
			index+=1
	return -1
string = "Happy birth day"
substring = "ay"
print(isString(string,substring))

#2nd way

def find_sbst(st,sb):
	l_st = len(st)
	l_sb = len(sb)
	count = 0
	for index in range(l_st - l_sb + 1):
		if st[index:index+l_sb] == sb:
			return index

print(find_sbst("Sifat","at"))