# ИНСТРУКЦИЯ:
# в командной строке используй числа от 1 до 9, а так же слова "pay" и "clean" 

import json

with open('online_shop_task/good_list.json', 'r') as file:
    goods = json.load(file)

cart = []
sum = 0
IsActiveSession = True
value = None

def show_price_list(goods): # показывает юзеру товары в наличии
    for el in goods:
         print(f"(№{el['number']}) {el['name']} - {el['cost']}")
    print ("\t")

def value_check(value): # проверка введенного значения на соответствие списку товаров
    for good in goods:
        if good["number"] == value:
            return True
    return False

def clean(cart, sum): # удаление товаров из корзины и обнуление счетчика
    cart = []
    sum = 0
    print ("\t")
    print("Cart is cleaned, current sum is:", sum)
    return(cart, sum)

def pay(cart, sum): # функция красиво выводит на экран корзину и стоимость, а также завершает прогу
    print ("\t")
    for i, item in enumerate(cart):
        if i != len(cart) - 1:
            print(item + ', ', end='')  
        else:  
            print(item)  
    print('Cost of the cart is:', sum)
    IsActiveSession = False
    return IsActiveSession

def add_in_cart(sum, goods, value): # добавление товара в корзину, подсчет суммы
    global good_name
    for good in goods:
        if value == good["number"]:
            cart.append(good["name"])
            good_name = (good["name"])
            sum += good["cost"]
            return(cart, sum) 
    
show_price_list(goods)

while IsActiveSession == True: # алгоритм работы
    value = input('Enter number of good: ')
    isGood = value_check(value)
    if isGood == True:
        cart, sum = add_in_cart(sum, goods, value)
        print('You add the', good_name, 'Sum is', sum)
    elif isGood == False and value.lower() == 'pay':
        IsActiveSession = pay(cart, sum)
    elif isGood == False and value.lower() == 'clean':
        cart, sum = clean(cart, sum)
    else:
        continue  