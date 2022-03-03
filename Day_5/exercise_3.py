even_numbers = []

for number in range(1, 101):
  is_even = number % 2 == 0
  if(is_even):
    even_numbers.append(number)
    
print(sum(even_numbers))
  