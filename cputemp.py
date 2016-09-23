"""	Author: Annapoornima
	Purpose:This programs read the CPU temperature at a particular time,
	and displays a plot of the temperature over time
"""
#import modules required for timestamping and putting the program to sleep
from datetime import datetime, timedelta
from time import sleep

#importing the module for plotting
import matplotlib.pyplot as plt

temp_data=0
x=[datetime.now() + timedelta(seconds=-i) for i in range(50,0,-10)]
y=[temp_data+i for i in range(len(x))]

#setting up the plot details
fig=plt.figure()

#adding a subplot here
ax=fig.add_subplot(111)
plt.title("Time Vs CPU temperature")
plt.xlabel("Time")
plt.ylabel("CPU temperature")
ax.plot(x,y)

plt.gcf().autofmt_xdate()

fig.canvas.draw()
#e='y'
while True:

	#to read the temperature, this program accesses a file in read mode that contai$
	#file is /sys/class/thermal/thermal_zone0/temp

	f=open("/sys/class/thermal/thermal_zone0/temp", "r")

	#timestamp the data
	temp_time=datetime.now()

	#read the data in the file to a variable and divide by 1000 to get correct value
	temp_data=int(f.readlines()[0].strip())/1000
	x=x[1:]
	x.append(temp_time)
	y=y[1:]
	y.append(temp_data)

	plt.show(block=False)
	fig.canvas.draw()
	plt.gcf().autofmt_xdate()
	plt.plot(x,y)
	sleep(10)

print "Good Bye, Exiting the Program"
#close file after reading
f.close()
