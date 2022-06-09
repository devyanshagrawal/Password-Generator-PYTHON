import random


print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numb = int(input("How many numbers would you like?\n"))

# l_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

l_let = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]

l_num = [str(i) for i in range(0, 10)]

l_sym = ['!', '@', '#', '$', '%', '*']

password = []

for let in range(num_letters):
    password.append(random.choice(l_let))

for sym in range(num_symbols):
    password.append(random.choice(l_sym)) 

for num in range(num_numb):
    password.append(random.choice(l_num))    

random.shuffle(password)
str1 = ''
print(f'Your generated password is: {str1.join(password)}')


