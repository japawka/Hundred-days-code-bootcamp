# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#
# heights = 0
# for n in student_heights:
#     heights += n
# print(heights / len(student_heights))
#
#
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# print(f"The highest score in the class is: {max(student_scores)}")
#
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#
# print(f"The highest score in the class is: {highest_score}")
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for i in range(1, nr_letters +1):
    password.append(random.choice(letters))

for i in range(1, nr_symbols +1):
    password += random.choice(symbols)

for i in range(1, nr_numbers +1):
    password += random.choice(numbers)

print(password)
random.shuffle(password)
new_pass = ''
for p in password:
    new_pass += p
print(new_pass)



