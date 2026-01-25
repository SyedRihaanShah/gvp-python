#Inbuilt math functions 

print(max(1,56,23,65,32))
print(min(1,56,23,65,32))

print(abs(-753))

print(pow(2,3)) #or print(2 ** 3 ) 

#using math module we can use more math functions 
import math

print(math.sqrt(64))#gives the square root of the given number
print(math.ceil(8.3))#rounds the number upwards
print(math.floor(1.5))#rounds the number downwards

print(math.pi)#prints pi value 

angle = 60
angle_radians = math.radians(angle)
print(math.cos(angle_radians)) # here angle must be given in radidans 