from math import sqrt


iteration = [sqrt(2)]


for i in range(1000):
	next_val = sqrt(2-2*sqrt(1-(iteration[-1]**2)/4 ))
	iteration.append(next_val)

n = 4
for i in range(1001):
	iteration[i]*=n
	n*=2

for val in iteration[:20]:
	print(val/2)

