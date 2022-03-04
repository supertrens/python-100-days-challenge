from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




def main():
  is_on = True
  menu = Menu()
  money_machine  = MoneyMachine()
  coffee_maker = CoffeeMaker()
  
  while is_on:
   order = input(f"\n\nWhat would you like? ({menu.get_items()}): ")
   match order:
     case "off":
       is_on = False
     case "report":
       coffee_maker.report()
       money_machine.report()
     case _:
      drink = menu.find_drink(order)
      if drink and coffee_maker.is_resource_sufficient(drink):
        is_paid = money_machine.make_payment(drink.cost)
        if is_paid :
          coffee_maker.make_coffee(drink)

main()