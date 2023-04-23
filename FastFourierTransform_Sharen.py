import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
from  scipy import signal

#Sharen Rajenthiran
#A19SC0373

#Tasks:
#1) Plot Bonus.csv data in time domain
#2) Plot Bonus.csv data in frequency domain using Fast Fourier Transform(FFT)


#save data in folder
#convert csv to numpy file
#load the original CSV file
load_file = np.genfromtxt("Bonus.csv", delimiter = ',', dtype = str)
# print(load_file)

#save the CVS file to NPY file
np.save("BonusN", load_file)
#test if npy is valid

file = np.load("BonusN.npy")
# print("Original file: ",load_file,"\nConverted file: ",file)  #tested and ok
# print(np.shape(file),np.shape(load_file))   #tested and ok


#extract time and amplitude data

data = np.load("BonusN.npy")

#store time data into time variable and amplitude data into y variable

data = np.transpose(data)     #transpose data
data = np.array(data, dtype ='float')        #convert strings to array

t = data[0]       #data[0] for time
y_t = data[1]       #data[1] for amplitude


#time resolution

t_0 = data[0][0]
t_1 = data[0][1]
t_2 = data[0][2]
t_3 = data[0][3]

t_res = t_2 - t_1

# print(str(t_2-t_1),str(t_3-t_2))   #check resolution

#sampling frequency

fsam = 1/t_res

# print(fsam)

#create frequency array

f = np.linspace(0,fsam,len(t))



#fast fourier transform

y_f = np.fft.fft(y_t)


#plots

#_____1st design___________

# plt.subplot(3,1,1)
# plt.grid()
# plt.xlabel("Time")
# plt.ylabel("Amplitude")
# plt.plot(t,y_t)
# plt.subplot(3,1,2)
# plt.grid()
# plt.xlabel("Frequency")
# plt.ylabel("Amplitude")
# plt.plot(abs(y_f))
# plt.subplot(3,1,3)
# plt.grid()
# plt.xlabel("Frequency")
# plt.ylabel("Amplitude")
# # plt.xlim([-0.2,(fsam/2)])
# plt.plot(f,abs(y_f))

#______2nd design and final______________

plt.figure()

plt.plot(t,y_t, color="red")
plt.title("Amplitude versus Time")
plt.xlabel("Time (a.u.)")
plt.ylabel("Amplitude (a.u.)")
plt.legend(["Time Space"], loc="upper right")
plt.grid()

plt.figure()

plt.plot(f,abs(y_f), color="green")
plt.title("Amplitude versus Frequency")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (a.u.)")
plt.legend(["Frequency Space"], loc="center")
plt.grid()



fig, (ax1,ax2) = plt.subplots(2,1)
ax1.plot(t,y_t,color="red",label="Time Space")
ax1.set_xlabel("Time (a.u.)")
ax1.set_ylabel("Amplitude (a.u.)")
ax1.legend(loc="upper right")
ax1.grid()

ax2.plot(f,abs(y_f),color="green", label="Frequency Space")
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Amplitude (a.u.)")
ax2.legend(loc="center")
ax2.grid()

# ax3.plot(f,abs(y_f),color="blue", label="Frequency Space with Nyquist frequency")
# ax3.set_xlabel("Frequency (Hz)")
# ax3.set_ylabel("Amplitude (a.u.)")
# ax3.legend(loc="upper right")




plt.tight_layout()


plt.show()





