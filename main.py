with open('input.txt', 'r') as f:
	string = f.read()
with open('key.txt', 'r') as f:
	key = f.read()
	key = int(key)
def crypt(string, key):
	s2 = ''
	for i in range(len(string)):
		s2 += chr(ord(string[i]) + key)
	return s2
def decrypt(string, key):
	s2 = ''
	for i in range(len(string)):
		s2 += chr(ord(string[i]) - key)
	return s2
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
		print('Unsupported action!')
