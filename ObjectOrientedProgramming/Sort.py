def sort_(a):
	min_ = a[0]
	for i in  range(1,len(a)):
		if(a[i] < min_):
			min_ = a[i]
	print(min_)
		

numbers = [4,6,2,7,1]
sort_(numbers)
