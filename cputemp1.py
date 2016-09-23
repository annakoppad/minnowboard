"""	Author: Annapoornima
	Purpose:This programs read the CPU temperature at a particular time,
	and displays a plot of the temperature over time
"""
#import modules required for timestamping and putting the program to sleep
from datetime import datetime, timedelta
from time import sleep

#importing the module for plotting
import matplotlib.pyplot as plt

#to read the temperature, this program accesses a file in read mode that contains the temperature data
#file is /sys/class/thermal/thermal_zone0/temp

#f=open("/sys/class/thermal/thermal_zone0/temp", "r")

#read the data in the file to a variable
#temp_data=int(f.readlines()[0].strip())/1000

#close file after reading
#f.close()

#timestamp the data
#cur_temp_time=datetime.now()
#next_half_hour=cur_temp_time+timedelta(hours=.5)
temp_data=0
x=[datetime.now() + timedelta(minutes=-i) for i in range(5,0,-1)]
y=[temp_data+i for i in range(len(x))]

#temp_t=cur_temp_time.strftime("%d:%m:%Y %H:%M:%S")
#print temp_t

#print temp data for verification
#print "here",temp_time

#setting up the plot details
fig=plt.figure()

#adding a subplot here
ax=fig.add_subplot(111)
plt.title("Time Vs CPU temperature")
#plt.axis([0,100,cur_temp_time, next_half_hour])
plt.xlabel("Time")
plt.ylabel("CPU temperature")
ax.plot(x,y)
#plt.xticks(x, labels, rotation='vertical')

plt.gcf().autofmt_xdate()

#Originally I did this to achieve the plot
#plt.plot(x,y) #commenting as a sub plot is being added
#ax.plot(x,y)

#draw and how the plot
#plt.show(block=False)

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
	labels=x
#	li.set_xdata(x)
#	li.set_ydata(y)
#	plt.xticks(x,labels, rotation='vertical')
	plt.show(block=False)
#	li.set_ydata(y)
	fig.canvas.draw()
	plt.gcf().autofmt_xdate()
	plt.plot(x,y)
	sleep(60)
#	e=raw_input("Enter y to continue: ")



print "Good Bye, Exiting the Program"
#close file after reading
f.close()
