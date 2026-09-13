#Generate n random numbers and save them to numbers
import random

n = int(input("How many numbers? "))

with open("numbers", "w", encoding="utf-8") as file:
    for i in range(n):
        number = random.randint(-100, 100)
        file.write(f"{number}\n")
        
#Count negative numbers in numbers
with open("numbers", "r", encoding="utf-8") as file:
    numbers = [int(number) for number in file.read().split()]

negative = 0

for number in numbers:
    if number < 0:
        negative += 1

print("Negative numbers:", negative)

#Copy all even numbers to even
with open("numbers", "r", encoding="utf-8") as file:
    numbers = [int(number) for number in file.read().split()]

with open("even", "w", encoding="utf-8") as file:
    for number in numbers:
        if number % 2 == 0:
            file.write(f"{number}\n")

#Copy all odd numbers 
with open("numbers", "r", encoding="utf-8") as file:
    numbers = [int(number) for number in file.read().split()]

with open("odd", "w", encoding="utf-8") as file:
    for number in numbers:
        if number % 2 != 0:
            file.write(f"{number}\n")
            
#count prime numbers in the file
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


with open("numbers", "r", encoding="utf-8") as file:
    numbers = [int(number) for number in file.read().split()]

count = 0

for number in numbers:
    if is_prime(number):
        count += 1

print("Prime numbers:", count)

#count how many times each number occurred
with open("numbers", "r", encoding="utf-8") as file:
    numbers = [int(number) for number in file.read().split()]

counts = {}

for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

with open("repetitions", "w", encoding="utf-8") as file:
    for number in counts:
        file.write(f"{number} - {counts[number]}\n")
        
        #homework
        import datetime

note = input("Enter your note: ")

date = datetime.datetime.now()

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write(f"{date.strftime('%c')} - {note}\n")

print("Note saved!")
