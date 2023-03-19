from eratosthenes_sieve import sieve





def find_perfects(perfects, sieved, end):
	power = 1
	while (power-1)*(power//2) < end-1:
		if sieved[power-1]:
			perfects[(power-1)*(power//2)] = 1
		power*=2




if __name__ == "__main__":
	END = 1000
	LENGTH = END
	primes = [1]*LENGTH
	perfects = [0]*LENGTH
	sieve(primes, LENGTH)
	find_perfects(perfects, primes, END)
	for i in range(0,len(perfects)):
		if perfects[i]:
			print(i)

