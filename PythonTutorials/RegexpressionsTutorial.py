import re
# findall
# search
# split
# sub
# finditer

# mystr = '''Tata Limited
# Dr. David Landsman, executive director
# 18, Grosvenor Place
# London SW1X 7HSc
# Phone: +91 (20) 7235 8281
# Fax: +91 (20) 7235 8727
# Email: tata@tata.co.uk
# Website: www.europe.tata.com
# Directions: View map
#
# Tata Sons, North America
# 1700 North Moore St, Suite 1520
# Arlington, VA 22209-1911
# USA
# Phone: +1 (703) 243 9787
# Fax: +1 (703) 243 9791
# 66-66
# 455-4545
# Email: northamerica@tata.com
# Website: www.northamerica.tata.com
# ar
# arr
# arrr
# arrrr
# ararar
# ararararararararar
# '''

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
# pattern = re.compile(r'\bView map')
#
# matches = pattern.finditer((mystr))
#
# for match in matches:
#     print(match)

# n = int(input("Enter a number : "))
# for i in range(0,n):
#     print(i+1, end=" ")
#
# print('\n')
# n = [1,2,3,4,5,6,7,8,9,10]
# print(*n)

str = '''Verify the input field accepts a valid email address. Some examples:
example@email.com
example.first.middle.lastname@email.com
example@subdomain.email.com
example+firstname+lastname@email.com
example@234.234.234.234
example@[234.234.234.234]
“example”@email.com
0987654321@example.com
example@email-one.com
_______@email.com
example@email.name
example@email.museum
example@email.co.jp
example.firstname-lastname@email.com
Valid Email Addresses that appear at glance to be invalid
extremely.”odd\ unusual”@example.com
extremely.unusual.”@”.unusual.com@example.com
very.”(),:;<>[]”.VERY.”very@\“very”.unusual@strange.email.example.com
Verify email id can contain a dot in the address field.
Verify email id can contain a dot in the subdomain field.
Verify email id can contain a plus sign.
Verify email id can contain an IP address in square bracket.
Verify email id can contain quotes.
Verify email id can contain digits.
Verify email id can contain an underscore.
Verify email id with a valid top-level domain name is valid.
Verify top-level domain can contain a dot.
Verify email id with a dash is considered valid
 app-z@gmail.com
app-z@gm-ail.com
'''

# pattern = re.compile(r'[\w.]+[@][\w.]+')
# match = pattern.findall(str)
# for matches in match:
#     print(matches)
# + indicates the 1 or more than 1 occurance of [0-9a-zA-Z._+%]
emails = re.findall(r"[0-9a-zA-Z._+%-]+@[0-9a-zA-Z._+%-]+[.][0-9a-zA-Z.]+",str)
print(emails)
for email in emails:
    print(email)

# \w = a-zA-Z0-9_
# \S = returns a match when the string doesn't have a whitespace.
thisis_validpattern = re.findall(r'\w+@\S+\w',str)