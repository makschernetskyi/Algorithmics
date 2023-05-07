# Algorithm to find out, if there is some substring(pattern) in the string(text)




def Rabin_Karp(text: str, pattern: str, base = 3, mod = 1000000000)->bool:
	pattern_len = len(pattern)
	text_len = len(text)

	if pattern_len >= text_len:
		return pattern == text

	def get_hash(substring):
		p = 1
		hashed = 0
		for i in range(len(substring)-1, -1, -1):
			hashed += (ord(substring[i])+1)*p
			p*=base
		return hashed%mod
	hash_l = 0
	hash_r = get_hash(text[:pattern_len])
	pattern_hash = get_hash(pattern)
	power_of_pattern = base**pattern_len

	for i in range(0, text_len-pattern_len):
		if (hash_r - hash_l*(power_of_pattern))%mod == pattern_hash:
			return True
		hash_r = (hash_r*base + ord(text[i+pattern_len])+1)%mod
		hash_l = (hash_l*base + ord(text[i])+1)%mod

	return False





def test(function, cases):
	for case in cases:
		if not function(case[0][0], case[0][1]) == case[1]:
			print(case, function(case[0][0], case[0][1]), "Oops!")
			return
		else:
			print('OK')
	print('OK')
	return

test_cases = [
	[['',''],True],
	[['a', 'a'],True],
	[['', 'a'],False],
	[['a', ''],True],
	[['abcdefghij', 'def'],True],
	[['  abcdef', 'cde'],True],
	[['abcdef', 'adf'],False],
	[['abc', 'def'],False],
	[['abc, defg', 'def'],True],
	[['djkfhjskdhfhsjkdfjhsdjkfsdfjksd dhsjkl nfd jhfkjlsdjkhfj kdhjk', 'dhsjkl'],True],
	[['fksdhfdsjkhfkjsdhfjkshdjfhdsjkfhjsdgfgkgfklglahgfkjghaskdf', 'psamfpsamdfpm'], False],
	[['abcdef', 'abcde'],True],
	[['abcdef', 'abcdf'],False]
]


if __name__ == "__main__":
	test(Rabin_Karp, test_cases)