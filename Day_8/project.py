import string

alphabet = string.ascii_lowercase

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def get_alphabet_shifted(shift_amount):
  max_length = len(alphabet)
  
  if shift_amount < -max_length:
    shift_amount += max_length
      
  if shift_amount > max_length:
    shift_amount -= max_length
    
  shift_part = alphabet[:shift_amount]
  remaining_part = alphabet[shift_amount:]
  
  return remaining_part + shift_part

def parse_message(message, alphabet_shifted):
    text_shifted = ""

    for letter in message:
      current_index = alphabet.index(letter)
      text_shifted += alphabet_shifted[current_index]
    
    return text_shifted
      
def encrypt(message, shift_amount):  
  alphabet_shifted = get_alphabet_shifted(shift_amount)
  cipher_text = parse_message(message, alphabet_shifted)
  
  print(f"The encode text is {cipher_text}")

def decrypt(message, shift_amount):
  alphabet_shifted = get_alphabet_shifted(-shift_amount)
  plain_text =  parse_message(message, alphabet_shifted)
  
  print(f"The decode text is {plain_text}")

text = text.lower()

if(direction == "encode"):
  encrypt(text, shift)
else:
  decrypt(text, shift)
