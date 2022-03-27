'input_word = input("Enter words : ")

count = 0

for c in input_word:
  if c.isspace() != True:
    count = count + 1

print("Total number of characters : ",count)