from datetime import datetime, timedelta
from time import sleep
import matplotlib.pyplot as plt

temp_data=0
x=[datetime.now() + timedelta(hours=-i) for i in range(5)]
y=[temp_data+i for i in range(len(x))]
plt.figure() ###### Create figure
while True:

    f=open("/sys/class/thermal/thermal_zone0/temp", "r")

    #timestamp the data
    temp_time=datetime.now()

    #read the data in the file to a variable and divide by 1000 to get correct value
    temp_data=int(f.readlines()[0].strip())/1000
    x=x[1:]
    x.append(temp_time)
    y=y[1:]
    y.append(temp_data)
    plt.hold(True) ##### Hold it.
    plt.gcf().autofmt_xdate()
    plt.plot(x,y)
    plt.show()
    sleep(5)


print "Good Bye, Exiting the Program"

#close file after reading
f.close()
