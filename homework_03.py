alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

for symbol in alice_in_wonderland:
    if symbol == "'":
        print(symbol)

print(alice_in_wonderland)

#4
square_black_sea = 436402
square_azov_sea= 37800
total_square = square_black_sea + square_azov_sea
print('Спільна площа морів:', total_square)

#5
total_warehouse =375291
first_second_warehouse =250449
second_third_warehouse=222950

warehouse_1 = total_warehouse-second_third_warehouse
warehouse_2 = first_second_warehouse-warehouse_1
warehouse_3 = total_warehouse-warehouse_1-warehouse_2
print('Склад 1:', warehouse_1)
print('Склад 2:', warehouse_2)
print('Склад 3:', warehouse_3)



#6
monthly_payment = 1179
total_months = 1.5 * 12
computer_cost = monthly_payment * total_months
print('Вартість комп’ютера:', computer_cost)

#7
#Знайди остачу від діленя чисел:
#a) 8019 : 8     d) 7248 : 6
#b) 9907 : 9     e) 7128 : 5
#c) 2789 : 5     f) 19224 : 9
#обычный способ
first = 8019 % 8
second = 9907 % 9
third = 2789 % 5
fourth = 7248 % 6
fifth = 7128 % 5
sixth = 19224 % 9

#через функцию 
def calcul_division_of_numbers(a,b):
    return a%b
print('Остача від ділення 8019 : 8:', calcul_division_of_numbers(8019, 8))
print('Остача від ділення 9907 : 9:', calcul_division_of_numbers(9907, 9))
print('Остача від ділення 2789 : 5:', calcul_division_of_numbers(2789, 5))
print('Остача від ділення 7248 : 6:', calcul_division_of_numbers(7248, 6))
print('Остача від ділення 7128 : 5:', calcul_division_of_numbers(7128, 5))
print('Остача від ділення 19224 : 9:', calcul_division_of_numbers(19224, 9))

#8
#обычный способ

#pizza_large= 4 * 274
#pizza_medium= 2 * 218
#juice= 4 * 35
#cake= 1 * 350
#water= 3 * 21
#total_cost = pizza_large + pizza_medium + juice + cake + water
##print(total_cost)

#через функцию 
#def total_price_calculation(quantity, price):
    #return quantity * price

#pizza_large= total_price_calculation(4, 274)
#pizza_medium= total_price_calculation(2, 218)
#juice= total_price_calculation(4, 35)
#cake= total_price_calculation(1, 350)
#water= total_price_calculation(3, 21)
#total_cost = pizza_large + pizza_medium + juice + cake + water
#print(total_cost)

birthday_order={"pizza_large": 4, "pizza_medium": 2, "juice": 4, "cake": 1, "water": 3}

def total_price_calculation():
    total_cost=0
    for item in birthday_order:
        if item == "pizza_large":
            total_cost += birthday_order[item] * 274
        if item == "pizza_medium":
            total_cost += birthday_order[item] * 218
        if item == "juice":
            total_cost += birthday_order[item] * 35
        if item == "cake":
            total_cost += birthday_order[item] * 350
        if item == "water":
            total_cost += birthday_order[item] * 21
    return total_cost
total_cost = total_price_calculation()
print('Загальна вартість замовлення:', total_cost)


#9
total_photo = 232
photos_per_page=8
#needed_pages = total_photo // photos_per_page
#print('Необхідна кількість сторінок:', needed_pages)

def calculate_neded_pages(total, page):
    return total//page
needed_pages = calculate_neded_pages(total_photo, photos_per_page)
print('Необхідна кількість сторінок:', needed_pages)

#10

distance = 1600
fuel_consumption_per_100km = 9
tank_capacity = 48

#Сколько бензина понадобится?
total_fuel_needed = (distance / 100) * fuel_consumption_per_100km

#Сколько раз нужно заехать на заправку?
refueling_stops = total_fuel_needed / tank_capacity

print('Потребуется бензина:', total_fuel_needed, 'литров')
print('Необходимо заехать на заправку:', round(refueling_stops), 'раз')