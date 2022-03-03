from math import sqrt


def prime_checker(number):
  if number <= 1:
    print(f"{number} is not a prime number.")
    return
  
  for i in range(2,int(sqrt(number)) +1):
    if number % i == 0:
      print(f"{number} is not a prime number.")
      return
      
  print(f"{number} is a prime number.")  




prime_checker(1)
prime_checker(2)
prime_checker(3)
prime_checker(4)
prime_checker(5)
prime_checker(6)
prime_checker(7)

print(int(sqrt(100))+ 1)
