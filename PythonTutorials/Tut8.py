mystr = "harry is a good boy"
# print(len(mystr))
# print(mystr[15:17])
# print(mystr[-4:-2])
# print(mystr[:])
# print(mystr[::-1])
# placing -1 in the last : of a string slicer effectively reverses the string.

print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","isnot"))