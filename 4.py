""" Created by Tanusha Choudhary
Python program to convert binary, octal, and hexadecimal numbers to integers and displaying the results. This program defines lists of binary, octal, and hexadecimal numbers. It then converts these numbers to integers using the int() function with base 2 for binary, base 8 for octal, and base 16 for hexadecimal. Finally, it prints the resulting integer values. """ 

binary = ["1100", "101", "11001", "1001", "110"] 
intbinary = [int(binary, 2) for binary in binary] 
octal = ["541", "7665", "443", "343", "4354"] 
intoctal = [int(octal, 8) for octal in octal] 
hexa = ["45D", "65A", "46B", "89E", "3A8"] 
inthexa = [int(hexadecimal, 16) for hexadecimal in hexa]
print("Binary to Integer:", intbinary) 
print("Octal to Integer:", intoctal) 
print("Hexadecimal to Integer:", inthexa)
