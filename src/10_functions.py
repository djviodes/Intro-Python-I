# Write a function is_even that will return true if the passed-in number is even.

def is_even(int):
    if int%2 == 0:
        return True
    elif int%2 != 0:
        return False

print(is_even(1))
print(is_even(2))
print(is_even(3))
print(is_even(4))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if num%2 == 0:
    print('Even!')
elif num%2 != 0:
    print('Odd...')

