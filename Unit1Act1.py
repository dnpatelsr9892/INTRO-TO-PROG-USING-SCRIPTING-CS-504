# 1. Write a statement that displays ‘Python is my favorite programming language’
print('Python is my favorite programming language')

# 2. Write a statement that displays:Most people think that Jordan is the “G.O.A.T.”
print('Most people think that Jordan is the "G.O.A.T."')
# or 
print("Most people think that Jordan is the \"G.O.A.T.\"")

# 3. Write a program to display the following information.
# John Doe
# 221 Danbury Road
# Wilton, CT 06897
# 
# johndoe@gmail.com
# 
# Literature
# 
# 617 426-9018

print('John Doe')
print('221 Danbury Road')
print('Wilton, CT 06897\n')
print('johndoe@gmail.com\n')
print('Literature\n')
print('617 426-9018')


# 4. Write a program to create 3 variables (x,y,z) with different numbers as values. Write aprogram to check which one is the biggest number and print out the result with amessage. (conditional statements, and keyword)

x = 6
y = 3 
z = 9
if x > y and x > z:
    print(f'x({x}) is biggest number')
if y > x and y > z:
    print(f'y({y}) is biggest number')
if z > x and z > y:
    print(f'z({z}) is biggest number')

print('Done!')
# 5. Write a program to create a variable with a value of 25. Create a loop that prints thesquare of the variable and changes the value of it by -2 every time it runs. Continue untilthe variable is not greater than 0 anymore. Print a message to indicate your programhas finished (Success!)

x = 25
while(x > 0):
    print('sq of '+ x + ' : ' + x**2)
    x = x - 2 
print('Done!')