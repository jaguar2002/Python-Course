def factorial(n):
	if n < 2:
		return 1
	return n * factorial(n-1)
	
print(factorial(50))

for x in range(1, 10, 3):
    print(x)
    
for x in range(10):
	#print(x)
	for y in range(x):
		print(y)
