def convert_n_from_one_to_another(num_str,base_1,base_2):

	if base_1 < 2 or base_2 >36:
		raise('not in base range')

	def num_to_digit(n):
		if n < 10:
			return str(n)
		else:
			return chr(n-10+ord('A'))

	decimal = 0
	power_base_1 = 1
	for i in range(len(num_str)-1, -1, -1):
		decimal += (ord(num_str[i])-ord('0'))*power_base_1
		power_base_1*=base_1
	result = ''
	while decimal:
		rem = int(decimal%base_2)
		result = num_to_digit(rem)+result
		decimal -= rem
		decimal /= base_2
	return result



if __name__ == "__main__":
	convert_n_from_one_to_another('101101',2, 16) # 1+4+8+32