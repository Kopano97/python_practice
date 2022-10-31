
my_string = input("Enter a string: ").lower()
my_string = my_string.replace(" ","")

if my_string == my_string[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome! ")    
    
