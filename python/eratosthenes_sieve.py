
LENGTH = 100

primes = [1]*LENGTH


def sieve(primes, length):
	primes[0] = 0
	primes[1] = 0
	i = 2
	while i*i<=length:
		if primes[i]:
			for j in range(i*2,length,i):
				primes[j] = 0
		i+=1


if __name__ == "__main__":
	sieve(primes, LENGTH)
	for i in range(0,len(primes)):
		if primes[i]:
			print(i)