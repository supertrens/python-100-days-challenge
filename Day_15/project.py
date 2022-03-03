import os


ACCEPTED_COINS = [
  {"name": "quater", "value": 0.25},
  {"name": "dime", "value": 0.10},
  {"name": "nickle", "value": 0.05},
  {"name": "penny", "value": 0.01},
]

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
    
def show_coffee_menu():
  index = 0
  print("\t\tWhat would you like to drink?")
  
  for option in MENU:
    index += 1
    cost = MENU[option]['cost']
    print(f"\t\t\t{index}: {option.capitalize()} (${cost})")

def show_resources():
  for resource in resources:
    name = resource.capitalize()
    quantity = resources[resource]
    prefix =""
    
    if name == "Coffee":
      suffix = "g"
    elif name =="Money":
      suffix = ""
      prefix ="$"
    else:
      suffix ="ml"
      
    print(f"{name}: {prefix}{quantity}{suffix}")
    
def update_resource(used_resource):
  global resources
  ingredients = used_resource["ingredients"]

  for ingredient in ingredients:
   used_quantity = ingredients[ingredient]
   total_quantity = resources[ingredient]
   resources[ingredient] = total_quantity - used_quantity
  
  if('money' in resources):
    resources['money'] += used_resource["cost"]
  else: 
    resources['money'] = used_resource["cost"]
   
def check_purchase_status(cost, payment, product_name):
    change = payment - cost
    
    if(payment >= cost):
      if change > 0:
        print(f"you paid ${payment} for a ${cost} {product_name}. Here is ${change} in change.")
        
      print(f"Here is your drink. Enjoy!")
      return True
    else:
      print(f"you paid ${payment} for a ${cost} {product_name}. Missing ${change * -1} to complete the payment.")
      return False

def get_menu_selection():
  options = list(MENU)
  option_index = int(input("\nPlease PRESS the correspondant number to select: "))
  option_name = ''
  
  if(option_index < len(options)):
    option_name = options[option_index - 1 ]
    print(f"You have selected option: {option_index} ({option_name.capitalize()})")
    
  return option_name

def coin_converter(coin_count, value):
  return coin_count * value

def is_payment_completed(target_cost, current_change):
  return float(current_change) >= float(target_cost)

def handle_payment(target_cost):
  print("\nPlease insert coins.")
  current_payment = 0
  is_completed = False
  
  for coin in ACCEPTED_COINS:
    coin_value = float(coin["value"])
    coin_name = str(coin["name"]).capitalize()+'s'
    
    if(coin_name == "Pennys"):
      coin_name = "Pennies"
    
    coin_count = int(input(f"how many {coin_name}?: "))
    current_payment += coin_converter(coin_count, coin_value)
    is_completed = is_payment_completed(target_cost, current_payment)
    
    if is_completed:
      break
  
  return current_payment
 
def main():
  is_completed = True
  while is_completed:
    print("\n\n\n\t\tWhat would you like?")
    menu = int(input("""
        \t\t\t 1: see report
        \t\t\t 2: buy coffee
        \t\t\t
        """))
    clear_screen()
    
    if(menu == 1) :
      show_resources()
      
    if(menu == 2):
      show_coffee_menu()
      menu_selection = get_menu_selection()
      selected_option = MENU.get(menu_selection)
      
      if(selected_option):
        price = selected_option["cost"]
        received_payment = handle_payment(price)
        is_completed = check_purchase_status(price, received_payment, menu_selection)
        
        if(is_completed):
          update_resource(selected_option)
          
      else:
        print("Unavailable option")

# the program starts here
main()
