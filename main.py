with open('input.txt', 'r') as f:
	string = f.read()
with open('key.txt', 'r') as f:
	key = f.read()
	key = int(key)
def crypt(string, key):
	l1 = []
	s = ''
	for i in string:
		l1.append(i)
	for i in range(len(l1)):
		l1[i] = chr(ord(l1[i]) + key)
	for i in l1:
		s+=i
	return s	
def decrypt(string, key):
	l1 = []
	s = ''
	for i in string:
		l1.append(i)
	for i in range(len(l1)):
		l1[i] = chr(ord(l1[i]) - key)
	for i in l1:
		s+=i
	return s
try:	
	ch = int(input('1 - Crypt, 2 - Decrypt\n'))
except ValueError:
	print('Write the number of action!')
else:	
	if ch == 1: 
		with open('output.txt', 'w') as f:
			f.write(crypt(string, key))
	elif ch == 2: 
		with open('output.txt', 'w') as f:
			f.write(decrypt(string, key))	
	else:
		raise Exception('Unsupported action')			