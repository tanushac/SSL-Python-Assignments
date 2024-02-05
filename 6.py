""" Created by Tanusha Choudhary
Python program to convert decimal numbers to binary, octal, and hexadecimal representations and displaying the results. """ 
decimal = ["50", "24", "45", "89", "43"] 
binary_representation = [bin(int(deci))[2:] for deci in decimal] 
octal_representation = [oct(int(deci))[2:] for deci in decimal] 
hexa_representation = [hex(int(deci))[2:] for deci in decimal] 
print("Binary representation:", binary_representation) 
print("Octal representation:", octal_representation) 
print("Hexadecimal representation:", hexa_representation)
