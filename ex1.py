def fahrenheit_to_celsius(temp):
    """ Converts Fahrenheit temperature to Celsius. 
        Formula is 5/9 of temp minus 32 """
    # Note that this line is not executed
    # end='' keeps print from starting a new line.
    newTemp = 5*(temp-32)/9
    print("The Fahrenheit temperature",temp,"is equivalent to",newTemp,end='')
    print(" degrees Celsius")
def celsius_to_fahrenheit(temp):
    """ Converts Celsius temperature to Fahrenheit . 
        The formula is (9/5) times temp plus 32.  """
    # Note that this line is not executed
    # end='' keeps print from starting a new line.
    newTemp = 9*temp/5 +32
    print("The Celsius temperature",temp,"is equivalent to",newTemp,end='')
    print(" degrees Fahrenheit")

def name():
    """ Input first and last name, combine to one string and print """
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    fullname = fname + " " + lname

    print("Your name is:", fullname)    

def name_city():
    """ Input first and last name, combine to one string and print """
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    city = input ("Enter your city: ")
    state = input ("Enter your state: ")
    fullname = fname + " " + lname

    print("Your name is:", fullname)
    print ("You live in: "+ city + ', '+ state)
def if_statement():
    """ Three slightly difference versions of if: if, if-else, if-elif-else"""
    x = 5
    y = 0
    z = 0
    if x > 0:
        print("x is positive")
        
    if y > 0:
        print("y is positive")
    else:
        print("y is not positive")
        
    # elif can be repeated as often as necessary    
    if z > 0:
        print("z is positive")
    elif z < 0:
        print("z is negative")
    else:
        print("z must be 0")
def area(type_, x):
    """ Computes the area of a square or circle. 
        type_ must be the string "circle or the string "square" 
        We use type_ here, because type is a Python keyword. """
    if type_ == "circle":
        area = 3.14*x**2
        print(area)
    elif type_ == "square":
        area = x**2
        print(area)
    else:
        print("I don't know that one.")
        
fahrenheit_to_celsius(56)
celsius_to_fahrenheit(20)
name()
name_city()
if_statement()
area("circle",1)
area("square",1)


