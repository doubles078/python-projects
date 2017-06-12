
def BMI(height,weight) : 
	THE = float(weight / (height * height)) * 703
	return THE

height = float(raw_input("What's your height in inches? "))
weight = float(raw_input("What's your weight in pounds? "))
		
print BMI(height,weight)

THE = BMI(height,weight)

if THE > 25:
	print "You need less cake!" 
elif THE > 15:
	print "You are soooooo healthy!"
elif THE > 0: 
	print "The cake is a lie."