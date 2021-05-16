# While Loops

i = 1
while i < 10:
    print("i is equal to " + str(i))
    i += 1

print("Finished with loop as i is equal to 10")

word = "python"
guess = ""
attempts = 0

while guess != word and attempts < 10:
    guess = input("Guess a word: ")
    attempts += 1

if guess == word and attempts > 1:
    print("Correct! it took you " + str(attempts) + " attempts to guess " + word)
elif guess == word and attempts == 1:
    print("Correct! it took you " + str(attempts) + " attempt to guess " + word)
else:
    print("You failed to guess the word in 10 attempts")

# For loop

letters = "Python"
print("Demonstrating for loop to spell out Python")
for letter in letters:
    print(letter)

operating_systems = ["Linux", "Windows", "Unix"]
print("Each OS in list")
for operating_system in operating_systems:
    print(operating_system)

# 3 elements in the the operating_systems list
print("Another way to print each OS in list")
for index in range(len(operating_systems)):
    print(operating_systems[index])