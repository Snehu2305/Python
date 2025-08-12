n = int(input("Enter a number: "))

i = 1
fact = 1
s = 1.0

print("The sum is: ")
for i in range(1, n+1):
 
   fact = fact * i

   if fact != 0:
     s += 1.0 /fact
   else:
     s += 0

   i += i

print(s)