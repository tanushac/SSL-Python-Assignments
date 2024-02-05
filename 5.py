"""Created by Tanusha Choudhary
Python program to convert binary, octal, and hexadecimal strings to decimal numbers and displaying the results. List comprehension is used . """ 
binstr = ["111", "1010", "1110", "1001", "111011"] 
octalstr = ["111", "222", "333", "444", "555"] 
hexastr = ["1AA", "BF", "4CE", "57D", "3A8"] 
decibin = [int(binary, 2) for binary in binstr] 
decioctal = [int(octal, 8) for octal in octalstr] 
decihexa = [int(hexadecimal, 16) for hexadecimal in hexastr] 
print("Binary to Decimal:", decibin) 
print("Octal to Decimal:", decioctal) 
print("Hexadecimal to Decimal:", decihexa)
