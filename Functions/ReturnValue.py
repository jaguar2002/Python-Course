def area_triangle(base,height):
	return (base*height)/2
print(area_triangle(10,5))

def convert_seconds(seconds):
	hours = seconds//3600
	minutes = (seconds - hours * 3600) // 600
	remaining_seconds = seconds - hours * 3600 - minutes * 60
	return hours,minutes,remaining_seconds
	
hours,minutes,seconds = convert_seconds(5000)
print(hours,minutes,seconds)
