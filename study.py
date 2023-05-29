#let's start python
print("hello python")
#this hash for comment a line.
"""
this multiple quotes add
before a comment many lines
""" 
a = "Twitter"
print(a)
#double quotes are the same as single quotes:
a = 'Twitter'
print(a)
h = 18
g = "Rajneesh Maurya"
print(type(h))
print(type(g))
t = str("Twitter")
b = int(18)
z = float(18.5)

print(t)
print(b)
print(z)

variable = "Rajneesh Maurya" #camel case
var_iable = "Rajneesh Maurya" 
_var_iab_le = "Rajneesh Maurya" #snake case
vari = "Rajneesh Maurya"
VaRiAble = "Rajneesh Maurya" #pascal case
variable2 = "Rajneesh Maurya"

# Day 32 Loop Set
Devset = {"kunal", "francesco", "aniket"}

for x in Devset:
  print(x)


print(variable)
print(var_iable)
print(_var_iab_le)
print(vari)
print(VaRiAble)
print(variable2)


a, b, c = "KunalKushwaha","IshanSharma","RajneeshMaurya"

print(a)
print(b)
print(c)

h = o = w = "ContentCreators"

print(h)
print(o)
print(w)

Twitterstars = ["KunalKushwaha","IshanSharma","RajneeshMaurya"]
t, w, s = Twitterstars

print(t)
print(w)
print(s)


#we can add string + string 
a = "Python "
b = "is "
c = "vibe"
print(a + b + c)


#we can't use it name + age.Combination of string and number python will give an error
age = 18
name = "Rajneesh Maurya"
print(name, age)

t = "love"

def myfunc():
  global t
  t = "life"

myfunc()

print("Python is " + t)

y = "love"

def myfunc():
  print("Python is " + y)
  
myfunc()  

#assign the values and print the data type
a = 5 
b = "Hello World"	
c = 20	
d = 20.5		
e = 1j	
f = ["apple", "banana", "cherry"]		
g = ("apple", "banana", "cherry")		
h = range(6)		
i = {"name" : "John", "age" : 36}		
j = {"apple", "banana", "cherry"}	
k = frozenset({"apple", "banana", "cherry"})	
l = True		
m = b"Hello"		
n = bytearray(5)		
o = memoryview(bytes(5))		
p = None

print(type(a)) 
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))
print(type(o))
print(type(p)) 

#day 7 
#Numbers in python.
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))


#Day 8 Python Casting
x = str("s1")  
y = int(2.8)
z = float(1)
print(x)
print(y)
print(z)


#Day 9 Python Strings
txt = "The best things in life for mine i.e. Python!"
print("JavaScript" not in txt)
print(len(txt))
text ="The best things in life for mine i.e. Python!"
print("Python" in text)
print(len(text))
str='''
S
T
A
R
'''
print(str)
a = """
s
t
a
r
"""
print(a)
print(a[3])

#Day 10 Python Slicing Strings

a = "Hello, World!"
print(a[0:5])

b = "Hello, World!"
print(b[-6:-1])


# Day 11 Python Modify Strings
y = "Hello, Python"
print(y.replace("H" , "M")) # replace the alphabet

x = " Python is love "
print(x.strip())    #remove whtie space

z = "Python is love"
print(z.lower())  #lower case

t = "Python is love"
print(t.upper())  # upper case

r = "Rajneesh, Maurya"
h = r.split(",") # split the words
print(h)


#Day 12 Python Concatenation string
a = "Rajneesh"
b = "Maurya"
c = a + b
print(c)


a = "Rajneesh"
b = "Maurya"
c = a + " " + b
print(c)

# Day 13 Python Format strings
age = "18"
txt = "This is Rajneesh Maurya, and I'm {} now"
print(txt.format(age))

#Day 14 Python Escape Characters
txt = "Life is \"Open Source\" and heart is Python."
print(txt) 

txt = "Hello World \\ (Python is Life)." #\\ backslash
print(txt) 

txt = "Hello\nWorld!" #\n New Line
print(txt) 

txt = "Hello\rWorld!" #\r Carriage Return
print(txt) 

txt = "Hello\tWorld!" #\r Tab
print(txt) 

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 
 
# Day 15 Python Strings Method
txt = "   "

x = txt.isspace()

print(x)

txt = "Open-source"

x = txt.isascii()

print(x)

txt = "Python is love & HTML + CSS is life"

x = txt.count("is")

print(x)

txt = "Rajneesh Maurya"

x = txt.center(50)

print(x)

# Day 16 Python Booleans
# Using if condition to check the number's
a = 18
b = 19

if a==b :
  print("Both are equal")
else:
  print("Both are not equal")

# Some Values are False
print(bool(False))

print(bool(None))

print(bool(0))

print(bool(""))

print(bool(()))

print(bool([]))

print(bool({}))


# Day 17 Python Operators
x = 8
y = 9
print(x + y) #Addition
x = 18
y = 12
print(x - y)  #Subtraction
x = 6
y = 3
print(x * y) #Multiplication
x = 54
y = 3
print(x / y) #Division
x = 10
y = 4
print(x % y) #Modulus
x = 5
y = 2
print(x ** y) #Exponentiation
x = 18
y = 4
print(x // y) #Floor division


# Day 18 Python Lists
mylist = ["Rajneesh", "Ishan", "Kunal"] 

print(type(mylist))

thislist = ["kunal", "ishan", "kunal", "ishan", "rajneesh"]

print(thislist)

thislist = ["youtube", "github", "twitter"]
print(thislist)

thislist = list(("Twitter", "LinkedIn", "Github"))
print(thislist)

thislist = ["eat", "code", "repeat"]
print(len(thislist))

list1 = ["study", "notes", "implement"]
list2 = [5, 6, 8, 7, 9]
list3 = [False, True, True]

print(list1)
print(list2)
print(list3)

list1 = ["twt", 18, True, 19, "git"]

print(list1)

# Day 19 Python Tuples
thistuple = tuple(("rajneesh", "kunal", "ishan"))
print(len(thistuple))
thistuple = ("rajneesh", "kunal", "ishan")
print(thistuple)
thistuple = ("study", "notes", "implement")
print(thistuple)
thistuple = tuple(("Twitter","LinkedIn","Github"))
print(thistuple)
mytuple = ("Twitter","LinkedIn","Github")

print(type(mytuple))
tuple1 = ("twt", 18, True, 19, "git")

print(tuple1)
tuple1 = ("Twitter","LinkedIn","Github")
tuple2 = (1, 7, 9, 10, 13)
tuple3 = (True, False, True)

print(tuple1)
print(tuple2)
print(tuple3)
thistuple = ("Profiles",)
print(type(thistuple))

#NOT a tuple
thistuple = ("Influencer")
print(type(thistuple))

# DAY 20 Python Access Tuple Items
brotuple = ("kunal", "ishan")
if "kunal" in brotuple:
 print("Yes, 'kunal' is in the bro tuple")
 
lifetuple = ('o','p','e','n')
print(lifetuple[0:])
 
linetuple = ('s', 'o','u','r','c','e')
print(linetuple[0:])

contributortuple = ("kunal", "madza", "madhu", "francesco")
print(contributortuple[0:4])

foodtuple = ("cake", "fruits", "juice")
print(foodtuple[-1])

moodtuple = ("study", "code", "repeat")
print(moodtuple[1])


# Day 21 Update Tuple 
contributortuple = ("kunal", "madza", "madhu")
y = ("aniket",)
contributortuple += y

print(contributortuple)

foodtuple = ("oats", "juice", "pizza")
y = list(foodtuple)
y.remove("pizza")
foodtuple = tuple(y)

print(foodtuple)

brotuple = ("kunal", "aniket")
y = list(brotuple)
y.append("ishan")
brotuple =tuple(y)

print(brotuple)

daily = ("practice", "study", "code")
random = list(daily)
random[1] = "question"
daily = tuple(random)

print(daily)


# DAY 22 Unpack Tuples
opensource = ("kunal","ishika","madhu", "aniket", "francesco")

(DevRel,WebDev, *DevAdv) = opensource

print(DevRel)
print(WebDev)
print(DevAdv)

contributor = ("kunal", "aniket", "ishika")

(DevRel,WebDev,DevAdv)= contributor

print(DevRel)
print(WebDev)
print(DevAdv)

Devs= ("kunal","madhu", "aniket", "francesco","ishika")

(DevRel,*DevAdv,WebDev) = Devs

print(DevRel)
print(DevAdv)
print(WebDev)

#Day 23 Made a Project 

# DAY 24 LOOP TUPLES
mylovetuple = ("lifeline",'O','P','E','N','S','O','U','R','C','E')
i = 1
while i < len(mylovetuple):
  print(mylovetuple[i])
  i = i + 1

#Day 25 Join Tuples
# join twp tuples
name = ("kunal", "aniket" , "francesco")
kfollowers = (177, 4.2, 164)

result = name + kfollowers
print(result)

# multiply tuple
lifeline = ("Open Source", "is", "love")
resulttuple = lifeline  * 2

print(resulttuple)

# DAY 26 PYTHON TUPLE METHOD
numbertuple = (6, 7, 5, 9, 6, 4, 7, 3, 8, 6)

x = numbertuple.count(7)

print(x)

numbertuple = (6, 7, 5, 9, 6, 4, 7, 3, 8, 6)

x = numbertuple.index(7)

print(x)

# Day 27 Python Sets
myset = {"kunal", "francesco", "aniket"}
print(type(set))

DEvOps = set(("kunal", "francesco", "aniket"))
print(DEvOps)

# Day 28 Python Access Set Item 
Devset = {"kunal", "francesco", "aniket"}

for x in Devset:
  print(x)
  
  
Devset = {"kunal","francesco","aniket"}

print("francesco" in Devset)

# today git pratice
# Day 29 ADD SETS
Devset = {"kunal", "francesco", "aniket"}

Devset.add("madhu")

print(Devset)

Devset = {"kunal", "francesco", "aniket"}
Dev = {"madza", "madhu", "ishika"}

Devset.update(Dev)

print(Devset)

Devset = {"kunal", "francesco", "aniket"}

Devlist = ["madza", "madhu"]

Devset.update(Devlist)

print(Devset)

# Day 30 Python Remove Add Item
devset = {"kunal", "francesco", "madza"}

devset.remove("francesco")

print(devset)

devset = {"kunal", "francesco", "madza"}

devset.clear()

print(devset)

devset = {"kunal", "francesco", "madza"}

devset.discard("francesco")

print(devset)

devset = {"kunal", "francesco", "madza"}

x = devset.pop()

print(x)

print(devset)

# Day 31 Make a project on know you zodiac sign

# DAY 32 Python Loop Sets
Devset = {"francesco","aniket","kunal"}

for x in Devset:
  print(x)


# Day 33 Python Join Sets
Devset1 = {"Rel","Adv","Ops"}
Devset2 = {1,2,3}

Devset3 = Devset1.union(Devset2)
print(Devset3)

Devset1 = {"Rel","Adv","Ops"}
Devset2 = {1,2,3}

Devset1.update(Devset2)
print(Devset1)

d = {"kunal", "francesco", "aniket"}
e = {"ishika", "madza", "aniket"}

v = d.intersection(e)

print(v)

d = {"kunal", "francesco", "aniket"}
e = {"ishika", "madza", "aniket"}

v.symmetric_difference_update(e)

print(d)

d = {"kunal", "francesco", "aniket"}
e = {"ishika", "madza", "aniket"}

v = d.symmetric_difference(e)
print(d) 

# DAY 34 Python Dictionaries
Devdict =	{
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "LinkedIn": "Rajneesh Maurya"
}
print(Devdict)

Devdict =	{
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "LinkedIn": "Rajneesh Maurya"
}
print(Devdict["Twitter"])

Devdict =	{
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "start":2022,
  "start":2023 
}
print(Devdict)

Devdict = {
  "Name": "Kunal",
  "DevRel": True,
  "Type": "Remote",
  "Platform": ["Twitter", "LinkedIn", "Github"]
}

print(Devdict)

Devdict = dict(name = "Francesco", profession="DevAdv", Type = "Remote")

print(Devdict) 


 











        



