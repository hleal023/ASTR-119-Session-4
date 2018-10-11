import numpy as np

x = 1.0						#define floats
y = 2.0

#exp and logs
print(np.exp(x))			#e^x
print(np.log(x))			#ln x
print(np.log10(x))			#log_10 x
print(np.log2(x))			#log_2 x

#min/max/misc
print(np.fabs(x))			#abs value as a float
print(np.fmin(x,y))			#min of x and y
print(np.fmax(x,y))			#max of x and y

#populate arrays
n = 100								#define an int
z = np.arrange(n,dtype=float)	#get an array [0.0,n-1]
z *= 2.0*np.pi /float(n-1		#z = z [0,2*pi]
sin_z = np.sin(z)				#get an array sin(z)

#interpolation 
print(np.interp(0.75,z,sin_z))	#interpolate sin(0.75)
print(np.sin(0.75))