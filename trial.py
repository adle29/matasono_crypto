import string

def mc_part3():
	h = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
	hh = bytes.fromhex(h)

	k = 'X'
	for (a,b) in zip(hh,bytes(k*len(hh),'ascii')):
		print(hex(a), " ^ ", hex(b), a^b, chr(a^b))

mc_part3()
