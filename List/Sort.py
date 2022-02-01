def bubble_sort(a):
	for i in range(0,len(a)):
		for j in range(0,i):
			temp = 0
			if(a[i] < a[j]):
				temp = a[i]
				a[i] = a[j]
				a[j] = temp
	for i in range(0,len(a)):
		print(a[i])
		
a = []
n = input("enter the length of the array")

for i in range(n):
	input_number = int(input(" "))
	a.append(input_number)

bubble_sort(a)
	
