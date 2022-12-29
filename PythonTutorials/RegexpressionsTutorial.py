import re
# findall
# search
# split
# sub
# finditer

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +91 (20) 7235 8281
Fax: +91 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
ar
arr
arrr
arrrr
ararar
ararararararararar
'''

#pattern = re.compile(r'tata')
#pattern = re.compile(r'.703')
#pattern = re.compile(r'^Tata') # ^ is used for starts with
#pattern = re.compile(r'com$') # $ is used for ends with
#pattern = re.compile(r'ar*') # match if there is a presence of 'a' and followed by  0 or more 'r'
#pattern = re.compile(r'ar+') # match if there is a presence of 'a' and followed by atleast 1 or more 'r'
#pattern = re.compile(r'ar{2}') # a and 2 r's
#pattern = re.compile(r'(ar){2}') #  2 ar's
# pattern = re.compile(r'(ar){2}|com') # returns matches where there are two ar's (or) com

# Special sequences
#pattern = re.compile(r'\ATata')
#pattern = re.compile(r'\bFax')
#pattern = re.compile(r'87\b')
#pattern = re.compile(r'\d{5}-\d{4}') # returns match, 5 digits followed by '-' 4 digits
#pattern = re.compile(r'\+91 .(\d{2}.) \d{4} \d{4}')
pattern = re.compile(r'\bView map')

matches = pattern.finditer((mystr))

for match in matches:
    print(match)

# n = int(input("Enter a number : "))
# for i in range(0,n):
#     print(i+1, end=" ")
#
# print('\n')
# n = [1,2,3,4,5,6,7,8,9,10]
# print(*n)

