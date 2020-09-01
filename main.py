
def crypt(string, key):
	res = ''
	for i in range(len(string)):
		res += chr(ord(string[i]) + key)
	return res
def decrypt(string, key):
	res = ''
	for i in range(len(string)):
		res += chr(ord(string[i]) - key)
	return res
while True:
	try:
		ch = int(input('1 - Crypt, 2 - Decrypt\n'))
	except ValueError:
		print('Write the number of action!')
	else:
		if ch == 1:
			s = input('Write your text:\n')
			key = int(input('Write your key:\n'))
			print('Result: ' + crypt(s, key))
		elif ch == 2:
			s = input('Write your text:\n')
			key = int(input('Write your key:\n'))
			print('Result: ' + decrypt(s, key))
		else:
			print('Action not found!')
