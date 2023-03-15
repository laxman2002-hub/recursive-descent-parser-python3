f = open('input.txt','r')
s = f.readline().strip().split()
n = len(s)
global p
p = 0

def A1():
	global p
	start = p

	p = start
	if p<n and "id"==s[p]:
		p+=1
		if (A1_()):
			return 1

	p = start
	return 0

def A1_():
	global p
	start = p

	p = start
	if p<n and "+"==s[p]:
		p+=1
		if (A1()):
			if (A1_()):
				return 1

	p = start
	if p<n and "*"==s[p]:
		p+=1
		if (A1()):
			if (A1_()):
				return 1

	p = start
	return 1
	return 0

isAccepted = A1()
if isAccepted and p==n:
	print('string '+ ' '.join(s) +' is Accepted')
else:
	print('string '+ ' '.join(s) +' is Rejected')
