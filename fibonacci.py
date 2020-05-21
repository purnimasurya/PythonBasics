n = int(input("Enter the number of terms : "))

# first two terms
n1, n2 = -1, 1

# check if the number of terms is valid
if n <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(0,n):
       n3 = n1 + n2
       print(n3)
       n1 = n2
       n2 = n3