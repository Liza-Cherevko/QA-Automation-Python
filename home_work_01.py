# task 01 == Виправте синтаксичні помилки
print("Hello", end = '')
print(" world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
 print(f"{hello} {world}!")

 # task 03  == Вcтавте пропущену змінну у ф-цію print
 for letter in "Hello world!":
     print(letter)


# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
 apples = 2
 banana = None
def banana_calc():
  if apples == 2:
         print(apples * 4)
  else:
         print(banana)
banana_calc()


# task 05 == виправте назви змінних
first_side = 1
second_side = 2
third_side = 3
fourth_side = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = first_side + second_side+third_side+fourth_side
print(perimetery)

# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

apple_tree=4
pear_tree= apple_tree+5
plum_tree= apple_tree-2
total_tree= apple_tree+pear_tree+plum_tree
print(total_tree)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

temperature_before_dinner=5
temperature_after_dinner= temperature_before_dinner-10
temperature_evening = temperature_after_dinner+4
print(temperature_evening)


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

boys_in_group = 24
girls_in_group = boys_in_group//2
total_children = boys_in_group+girls_in_group
print(total_children)
current_count_in_group= total_children-3
print(current_count_in_group)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book_price= 8
second_book_price= 8+2
third_book_price= (first_book_price+second_book_price)//2
total_price=first_book_price+second_book_price+third_book_price
print(total_price)
