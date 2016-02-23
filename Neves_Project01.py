#Jessica Neves - Lab 1

#Section 2.2
print("2.2 - Build a right pyramid\n")

#User input variables
building_block = str(input("Type a character to build your pyramid with: "))
level = int(input("Enter the number of levels you want in your pyramid: "))

number_blocks = 1 + level#Added 1 so range stops at the user's desired level
for row in range(1, number_blocks):
    print(row * building_block)#Repeats the building block in each level

input("\nPress any key to continue.\n")



#Section 2.3
#THIS CODE DOES NOT ACCOUNT FOR BUILDING BLOCKS OF MORE THAN 1 CHARACTER
print("2.3 - Build a centered pyramid (Not corrected for more than one "
      "character)\n")

#User input variables
building_block = str(input("Type a character to build your pyramid with: "))
level = int(input("Enter the number of levels you want in your pyramid: "))

space = " "
number_blocks = (level*2)#Creates pyramid base
top_fill = level - 1#space around the block at the top of the pyramid

#for loop: Start= 1, Step= 2 for odd numbers in levels
for pyramid in range(1, number_blocks, 2):
    print((top_fill*space)+(pyramid*building_block)+(top_fill*space))
    top_fill -= 1#decrement space from top to bottom
    
input("\nPress any key to continue.\n")

#THIS CODE ACCOUNTS FOR BUILDING BLOCKS OF MORE THAN 1 CHARACTER
print("2.3 - Build a centered pyramid (Corrected for more than one "
      "character)\n")
building_block = str(input("Type a character to build your pyramid with: "))
level = int(input("Enter the number of levels you want in your pyramid: "))

number_blocks = (level*2)#This makes the base of the pyramid
space = " "*len(building_block)#space needs to be same size as building block
fill = level - 1 #Space around the block at the top of the pyramid
for pyramid in range(1, number_blocks, 2):
    print((fill*space)+(pyramid*building_block)+(fill*space))
    fill -= 1#gives pyramid shape

input("\nPress any key to continue.\n")


#Section 3.1
print("3.1 - Build a rotated parabola\n")
#User input for range
x_range = int(input("Enter a value for your range: "))
if x_range < 0:#want x to be positive
    x_range = x_range*-1

#initial x value for equation
x = x_range

#Symbols
plot_point = "."
space = " "

for parabola in range(-x, x+1):
    y = int((x**2)/4)#can't concatenate strings with floats
    x -= 1#by decrementing, x values will loop from x to -x
    print(y*space + plot_point)
        
input("\nPress any key to continue.\n")        
    

#Section 3.2
#Description
print("3.2 - Build a parabola right side up.\n")
print("A parabola is a 'U' shaped graph of the function f(x) = x^2.")
print("\nIn this function's basic form, f(x) will always be positive since any "
      "negative \nvalue multiplied by itself will always yield a positive "
      "value. The function can \nbe modified with multiplication, division, "
      "addition, and subrtraction.\n")

print("The graph displayed can be altered as follows:\n- Addition or subraction"
      " will shift the graph up or down.\n- Multiplication by a positive value"
      " will make the graph more narrow.\n- Division by a positive value will "
      "make the graph wider.\n- Alternatively, multiplication or division by a "
      "negative value will mirror the \n  graph across the x-axis.")
print("\nThis program is designed to show you how the width of a parabola can be "
      "scaled \nto be wider or narrower.")

print("\nThis program will start by asking you for a number to use as your "
      "range of \nx-values. You need only type one number at either end of "
      "your range. For \nexample, if you type either -15 or 15, your range will "
      "be [-15, 15]. This \nprogram uses the absolute value to create the "
      "parabola.\n")

#collects user input for range
abs_value = int(input("Enter a number to use as your range: ")) 
if abs_value < 0:
    abs_value = abs_value*-1
x = abs_value

#collects user input for parabola width   
scale = " "
while (scale != "wide") and (scale != "narrow"):
    scale = input("Would you like the parabola to be 'wide' or 'narrow'? ")
    scale = scale.lower()
if scale == "wide":
    operator = "/"
if scale == "narrow":
    operator = "*"

#collects user input for scaling factor
factor = int(input("By what factor? Type a number: "))
if factor < 0:#make positive to avoid translating parabola across x-axis
    factor = factor*-1
if operator == "/":
    scaling_factor = 1/factor
if operator == "*":
    scaling_factor = 1*factor

#Symbols
plot_point = "*"
space = " "
new_line = "\n"

#initial values
curve = 0
inner_space = (x*2)-1

#parabola for loop
for parabola in range(x, -1, -1):
    y_int = int((x**2)*scaling_factor)
    y_values = (x**2)*scaling_factor#true value
        
    if y_values > 0:
        y = y_int
        print(curve*space + plot_point + inner_space*space + plot_point)
        x -= 1
        y_int = int((x**2)*scaling_factor)
        print(new_line*(y-y_int-1))#to accurately space each set of points
        curve += 1#creates curve along margin
        inner_space -= 2#controls tapering between points
          
    if y_values == 0:#prints one point at the bottom of the parabola
        print(curve*space + plot_point)
        print("|"*(abs_value*2+1))#prints tick marks for x-axis
        print(curve*space + "0")#shows location of x = 0
    

input("\nPress any key to continue.\n")



#Section 3.3
print("3.3 - Build a circle\n")

#User input for radius
radius = int(input("Enter a number to be the radius of your circle: "))

#Variables
plot_point = "."
space = " "
x_max = radius
x = radius
pi = (3.14159265)

for circle in range(x, -x-1, -1):
    y_int = int((x**2)/pi)#can't multiply strings and floats
    y_max = int((x_max**2)/pi)
    x -= 1

    if y_int == 0:#Creates spacing at diameter
        print(plot_point + (y_max*2)*space + plot_point)
        
    elif y_int == y_max:#Appears at top/bottom of circle
        print(((x_max*2)+1)*space)
    
    else:#Creates shaping everywhere else in cirlce
        print(((y_int)*space) + plot_point +
              ((y_max - y_int)*2*space + plot_point))

input("\nPress any key to exit.")
