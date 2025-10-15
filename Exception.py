# n = int(input('Enter a number: '))

# try:
#     ans = 10 / n
#     print('answer is: ', ans)

# except ZeroDivisionError:
#     print('you can not divide by zero')



class InvalidAgeException (Exception):
    pass

class InvalidValueException(Exception):
    pass

n = 18
try:
   num =  int(input('Enter a number: '))
   if num < 18 and num >= 0:
       raise InvalidAgeException
   elif num < 0:
       raise InvalidValueException
   else:
       print('Eligible to vote')
    
except InvalidAgeException:
    print('Exception occured: you can not vote')

except InvalidValueException:
    print("Exception occured: plz enter valid value")