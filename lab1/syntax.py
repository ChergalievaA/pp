#ex1
print("Hello,World!")
#ex2
if 5>2
  print("YES")
#ex3.1
  #This is a comment
#3.2
  """
  This is a comment
  writhen in
  more than just one line
  """ 
  #ex4.1
  carned="Volvo"
  #ex4.2
  x=50
  #ex4.3
  x=5
  y=10
  print(x+y)
  #ex4.4
  x=5
  y=10
  z=x+y
  print(x+y)
  #ex4.5
  x,y,z="Orange","Banana","Cherry"
  #ex4.6
  x=y=z="Orange"
  #ex4.7
  def myfunc():
    global x
x="fantastic"
#ex5.1
x=5
print(type(x))
int
#ex5.2
x="Hello World"
print(type(x))
str
#ex5.3
x=20.5
print(type(x))
float
#ex5.4
x=["apple","banana","cherry"]
print(type(x))
list
#ex5.5
x=("apple","banana","cherry")
print(type(x))
tuple
#ex5.6
x={"name":"John","age":36}
print(type(x))
dict
#ex5.7
x=True
print(type(x))
bool
#ex6.1
x=5
x=float(x)
#ex6.2
x=5.5
x=int(x)
#ex6.3
x=5
x=complex(x)
#ex7.1
x="Hello World"
print(len(x))
#ex7.2
txt="Hello World"
x=txt[0]
#ex7.3
txt="Hello World"
x=txt[2:5]
#ex7.4
txt="Hello World"
x=txt.strip()
#ex7.5
txt="Hello World"
txt=txt.upper()
#ex7.6
txt="Hello World"
txt=txt.lower()
#ex7.7
txt="Hello World"
txt=txt.replace("H","J")
#ex7.8
age=36
txt="My name is John, I am {}"
print(txt.formate(age))