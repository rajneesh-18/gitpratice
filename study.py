#let's start python
print("hello python")
#this hash for comment a line.
"""
this multiple quotes add
before a comment many lines
""" 
s = "Twitter"
print(s)
#double quotes are the same as single quotes:
s = 'Twitter'
print(s)
a = 18
n = "Rajneesh Maurya"
print(type(a))
print(type(n))
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
starlist = ["Rajneesh", "Ishan", "Kunal"] 

print(type(starlist))

starlist = ["kunal", "ishan", "kunal", "ishan", "rajneesh"]

print(starlist)

sociallist = ["youtube", "github", "twitter"]
print(sociallist)

favlist = list(("Twitter", "LinkedIn", "Github"))
print(favlist)

routinelist = ["eat", "code", "repeat"]
print(len(routinelist))

list1 = ["study", "notes", "implement"]
list2 = [5, 6, 8, 7, 9]
list3 = [False, True, True]

print(list1)
print(list2)
print(list3)

list1 = ["twt", 18, True, 19, "git"]

print(list1)

# Day 19 Python Tuples
startuple = tuple(("rajneesh", "kunal", "ishan"))
print(len(startuple))
startuple = ("rajneesh", "kunal", "ishan")
print(startuple)
dailytuple = ("study", "notes", "implement")
print(dailytuple)
favtuple = tuple(("Twitter","LinkedIn","Github"))
print(favtuple)
favtuple = ("Twitter","LinkedIn","Github")

print(type(favtuple))
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

# Day 35 Python Access Dictionary Items
Devdict =	{
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "Follower's": 57
}
x = Devdict.get("Twitter")
print(x)

Devdict = {
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "Follower's": 57
}

x = Devdict.keys()

print(x)

Devdict = {
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "Follower's": 57
}

x = Devdict.values()

print(x)

Devdict = {
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "Follower's": 57
}

x = Devdict.items()

print(x)

# DAY 36 Change Dictionary
#WITHOUT USING UPDATE METHOD
Devdict =	{
  "name": "Rajneesh",
  "twitter": "@rajneeshstwt",
  "follower's": 50
}

Devdict["follower's"] = 51

print(Devdict)

# HERE USING UPDATE METHOD
Devdict =	{
  "name": "Rajneesh",
  "twitter": "@rajneeshstwt",
  "follower's": 50
}

Devdict.update({"follower's":51})

print(Devdict)
 
# Day 37 Python Add Dictionary
#Without using update() method
Devdict =	{
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "Follower's": 57
}
Devdict["Github"] = "rajneesh-18"
print(Devdict)

#With using update() method
Devdict =	{
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "Follower's": 57
}
Devdict.update({"Github": "rajneesh-18"})

print(Devdict)

# Day 38 Python Dictionary Remove Items
# Using 4 methods to remove any item
Devdict =	{
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "Follower's": 58
}  
Devdict.pop("Twitter")
print(Devdict)


Devdict =	{
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "Follower's": 58
}
Devdict.popitem()
print(Devdict)


Devdict =	{
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "Follower's": 58
}
del Devdict["Twitter"]
print(Devdict)

Devdict =	{
  "Name": "Rajneesh",
  "Twitter": "@rajneeshstwt",
  "Follower's": 58
}
Devdict.clear()
print(Devdict)

# Day 39 Loop Dictionaries
Devdict =	{
  "name": "Rajneesh Maurya",
  "twitter": "@rajneeshstwt",
  "follower's": 60
}
for x in Devdict.values():
  print(x)

Devdict =	{
  "name": "Rajneesh Maurya",
  "twitter": "@rajneeshstwt",
  "follower's": 60
}  
for x in Devdict.keys():
  print(x)

Devdict =	{
  "name": "Rajneesh Maurya",
  "twitter": "@rajneeshstwt",
  "follower's": 60
}
for x, y in Devdict.items():
  print(x, y)

# Day 40 Copy Dictionary
# Using copy() 
Devdict = {
  "Name": "Rajneesh Mauyra",
  "Username": "@rajneeshstwt",
  "Follower's": 62
}
Opsdict = Devdict.copy()
print(Opsdict)

# Using dict()
Devdict = {
  "Name": "Rajneesh Mauyra",
  "Username": "@rajneeshstwt",
  "Follower's": 62
}
Opsdict = dict(Devdict)
print(Opsdict)

# DAY 41 Made a project "Predicting Game"

# DAY 42 Nested Dictionary
mydata = {
  "user1" : {
    "name" : "Kunal",
    "year" : 19
  },
  "user2" : {
    "name" : "Rajneesh",
    "year" : 18
  },
  "user3" : {
    "name" : "Vipin",
    "year" : 22
  }
}

print(mydata)

user1 = {
    "name" : "Kunal",
    "year" : 19
},
user2 = {
    "name" : "Rajneesh",
    "year" : 18
},
user3 = {
    "name" : "Vipin",
    "year" : 22
}

mydata = {
  "user1" : user1,
  "user2" : user2,
  "user3" : user3
}

print(mydata)

# Day 43 Python If Else 
k = 19
r = 18
if r > k:
  print("r is greater than k")
elif k == r:
  print("k and r are equal")
else:
  print("k is greater than r")

# Day 44 Python While loop
x = 1
while x < 6:
  print(x)
  if (x == 3):
    break
  x += 1

x = 0
while x < 6:
  x += 1
  if x == 3:
    continue
  print(x)
  
x = 1
while x < 6:
  print(x)
  x += 1
else:
  print("x is less than 6")
  
# Day 45 Python For loop
dev = ["madhu", "francesco", "kunal"]
for x in dev:
  print(x) 
  if x == "kunal":
    break
    
dev = ["kunal", "francesco", "madza"]
for x in dev:
  if x == "francesco":
    continue
  print(x) 
# DAY 46 Python condition and function by using for loop

# with using range()
for x in range(6):
  print(x) 
  
#with using else   
for x in range(6):
  print(x)
else:
  print("Completed")
# Day 47 Python Functions
def my_function():
  print("Welcome folks on my twitter handle")

my_function()

def my_function(fname):
  print( "DevOps & Twitter Star :")
  print(fname)

my_function("Kunal Kushwaha")
my_function("Francesco ciulla")
my_function("Pradumna Saraf")

def my_function(*OS):
  print("I usually go with " + OS[1])

my_function("Windows", "Linux", "iOS")

def my_function(Dev3, Dev2,Dev1):
  print("Twitter Star's:")
  print(Dev3)
  print(Dev2)
  print(Dev1)
  

my_function(Dev1 = "Aniket", Dev2 = "Francesco", Dev3 = "Kunal")

def my_function(**district):
  print("My District is " + district["dname"])

my_function(sname = "Uttar Pradesh", dname = "Varanasi")

def my_function(country = "Toronto"):
  print("I'm from " + country)

my_function("Italy")
my_function("India")
my_function()
my_function("London")

# Day 48 Some Methods in Functions & Recursion
# Some other examples
def Name(Dev):
  for x in Dev:
    print(x)

DevOps=["kunal", "francesco", "madhu"]

Name(DevOps)

def my_function(x):
  return 18 * x

print(my_function(4))
print(my_function(6))
print(my_function(8))

def function():
  pass
  
def fact(n):
    if n == 0:  #factorial of 0 is 1
        return 1
    else:
        return n * fact(n-1)  #call

# Using factorial function
print(fact(12))

# Day 49 Python Lambda
x = lambda a, b: a * b
print(x(18, 12))

x = lambda a, b, c: a + b + c
print(x(9, 5, 8))

x = lambda a: a + 12
print(x(18))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(4)

print(mydoubler(13))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(6)

print(mytripler(17))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(8)
mytripler = myfunc(9)

print(mydoubler(15)) 
print(mytripler(19))
        
# Day 50 Python Arrays
Devs= ["Frontend", "Backend", "Full stack"]

x = len(Devs)

print(x)

Devs= ["Frontend", "Backend", "Full stack"]

x = Devs[0]

print(x)

Devs= ["Frontend", "Backend", "Full stack"]

for x in Devs:
  print(x)

# Using pop for remove
Devs= ["Frontend", "Backend", "Full stack"]

Devs.pop(1)

print(Devs)

# Using remove for remove
Devs= ["Frontend", "Backend", "Full stack"]

Devs.remove("Full stack")

print(Devs)

Devs= ["Frontend", "Backend", "Full stack"]

Devs.append("MERN")

print(Devs)

# Day 51 Made a project game "rock paper scissors" with the help of if-elif-else statement and def,import.
# Day 52 Made a project "temperature converter" with the help of if-elif-else statement and def.
# Day 53 Made a project "Tech Quiz Test" with the help of class, __init__ function,for loop,if-elif-else statement.
# Day 54 Made a project "Greeting of Day" with the help of __init__ function,import,def,if-elif-else statement.  
# Day 55 Made a project "Daily Routine" with the help of __init__ function,class,list,def,if-elif-else statement.    
# Day 56 Python Classes
class Person:
  def __init__(self, name, profession):
    self.name = name
    self.prof = profession

p1 = Person("Francesco Ciulla", "DevAdv")

print(p1.name)
print(p1.prof)

class Person:
  def __init__(self, name, profession):
    self.name = name
    self.prof = profession

  def __str__(self):
    return f"{self.name}({self.prof})"

p1 = Person("Kunal Kushwaha", "DevRel")

print(p1)

# Day 57 Python Objects
# Using self as a parameter
class Person:
  def __init__(self, name, prof):
    self.name = name
    self.prof = prof

  def myfunc(self):
    print("Hello I'm" + self.name)

p1 = Person("Rajneesh Maurya", "Cool")
p1.myfunc()

# Using parameter which I Like that's why it's name is self 
class Person:
  def __init__(intro, name, prof):
    intro.name = name
    intro.prof = prof
    
  def myfunc(abc):
   print ("Morning I'm " + abc.name)

p1 = Person("Rajneesh Maurya","Cool")
p1.myfunc()

# Using parameter which I Like that's why it's name is self 
class Person:
  def __init__(intro, name, prof):
    intro.name = name
    intro.prof = prof
    
  def myfunc(abc):
   print ("This is " + abc.name)

p1 = Person("Rajneesh Maurya","Cool")
p1.myfunc()

# DAY 58 PYTHON INHERITANCE
# With __init__ function
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Rajneesh", "Maurya")
x.printname()

# With super() function
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Rajneesh", "Maurya")
x.printname()

# Day 59 Python Iterator
# Example of Iterable
mystr = "Kunal"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# Example of Iterator
mytuple = ("Kunal", "Francesco", "Madza")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Day 60 Python Loop through the iterator
# Create an iterator
my_list = ["f", "r", "a", "n", "c", "e", "s", "c", "o"]
my_iterator = iter(my_list)

# Loop through the iterator
for item in my_iterator:
    print(item)

# Create an iterator
my_list = ["k", "u", "n", "a", "l"]
my_iterator = iter(my_list)

# Loop through the iterator
for item in my_iterator:
    print(item)
  
# Day 61 Python Create an Iterator
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            item = self.data[self.index]
            self.index += 1
            return item

# Usage:
dev_list = ["kunal","francesco","madza","madhu","aniket"]
my_iterator = MyIterator(dev_list)
for item in my_iterator:
    print(item)

#Day 62 Python StopIteration
class MyNum:
  def __iter__(self):
    self.a = 20
    return self

  def __next__(self):
    if self.a <= 30:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNum()
myiter = iter(myclass)

for x in myiter:
  print(x)

# Day 63 Python Function Polymorphism

x = "Hello Twitter!"

print(len(x))

devtuple = ("kunal", "francesco", "madza")

print(len(devtuple))

mydict = {
  "company": "Twitter",
  "role": "Content Creator",
  "age": 18
}

print(len(mydict))

# Day 64 Python Class Polymorphism
class ProgrammingLanguage:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        pass

class Python(ProgrammingLanguage):
    def display_info(self):
        print(f"{self.name} is a popular programming language for web development")

class JavaScript(ProgrammingLanguage):
    def display_info(self):
        print(f"{self.name} is a versatile programming language")

class Java(ProgrammingLanguage):
    def display_info(self):
        print(f"{self.name} is a widely-used programming language")

def get_language_info(language):
    language.display_info()

python = Python("Python")
javascript = JavaScript("JavaScript")
java = Java("Java")

get_language_info(python)       # Python is a popular programming language for web development.
get_language_info(javascript)   # JavaScript is a versatile programming
get_language_info(java)         # Java is a widely-used programming language 

# Day 65 Python Class Polymorphism
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Create instances of different shapes
rectangle = Rectangle(6, 13)
circle = Circle(4)

# Calculate and print the areas
print("Area of the rectangle:", rectangle.area())  # Output will be: 78
print("Area of the circle:", circle.area())  # Output will be:50.24
x = 10  # global variable

# Day 66 Python Global Scope
def func():
    print(x)  # accessing global variable

func()  # Output will be 10

# Day 67 Python Global Scope
def myfunc():
  x = "Rajneesh Maurya"
  print(x)

myfunc()

# Day 68 Python Module 
# Here you see How to use Module
import math

# Calculate the square root of a number
number = 16
square_root = math.sqrt(number)
print("Square root of", number, "is", square_root)

# DAY 69 PYTHON VARIABLE IN MODULE

# DAY 70 Python Naming & Re-Naming in Module
# Original module: my_module.py

def greet(name):
    print(f"Hello, {name}!")

def calculate_square(number):
    return number ** 2
# Renamed module: utilities.py

def greet(name):
    print(f"Hello, {name}!")

def calculate_square(number):
    return number ** 2
# main.py

import utilities

utilities.greet("John")
result = utilities.calculate_square(5)
print(result)

# Day 71 Python DateTime

import datetime

# Get the current date
current_date = datetime.date.today()
print("Current date:", current_date)

# Create a specific date
specific_date = datetime.date(2023, 7, 5)
print("Specific date:", specific_date)

# Calculate the difference between two dates
difference = specific_date - current_date
print("Difference in days:", difference.days)



