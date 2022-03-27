num = int(input("Enter the value of n: "))
hold = num
sum = 0

if num <= 0: 
   print("Enter a whole positive integer!") 
else: 
   while num > 0:
        sum = sum + num
        num = num - 1;
    # displaying output
        print("Sum of first", hold, "positive integer is :", sum)