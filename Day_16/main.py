from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




def main():
  new_order = True
  menu = Menu()
  money_machine  = MoneyMachine()
  coffee_maker = CoffeeMaker()
  
  while new_order:
   order = input(f"\n\nWhat would you like? ({menu.get_items()}): ")
   match order:
     case "off":
       new_order = False
     case "report":
       money_machine.report()
     case _:
      drink = menu.find_drink(order)
      if drink and coffee_maker.is_resource_sufficient(drink):
        is_paid = money_machine.make_payment(drink.cost)
        if is_paid :
          coffee_maker.make_coffee(drink)

main()