h=int(input())
m=int(input())
hour=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
mi=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                   	"eleven", "twelve", "thirteen", "fourteen", "fifteen",
                   	"sixteen", "seventeen", "eighteen", "nineteen", "twenty",
                   	"twenty one", "twenty two", "twenty three", "twenty four", "twenty five",
                   	"twenty six", "twenty seven", "twenty eight", "twenty nine"]
if (h>=0 and h<12) and (m>=0 and m<60):
	if m==0:
    	h=hour[h-1]
    	print("%s o' clock"%h)
	elif m==1:
    	h=hour[h-1]
    	print("one minute past %s"%h)
	elif m==10:
    	h=hour[h-1]
    	print("ten minute past %s"%h)
	elif m==15:
    	h=hour[h-1]
    	print("quarter past %s"%h)
	elif m==30:
    	h=hour[h-1]
    	print("half past %s"%h)
	elif m==40:
    	h=hour[h-1+1]
    	print("twenty minutes to %s"%h)
	elif m==45:
    	h=hour[h-1+1]
    	print("quarter to %s"%h)
	elif m==47:
    	h=hour[h-1+1]
    	print("thirteen minutes to %s"%h)
	elif m<30:
    	h=hour[h-1]
    	m=mi[m-1]
    	print("%s minutes past %s"%(m,h))
	elif m>30:
    	h=hour[h-1+1]
    	m=mi[60-m-1]
    	print("%s minutes to %s"%(m,h))


