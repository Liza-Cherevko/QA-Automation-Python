#Блок A. LIST — 4 задания
#Задание 1. Создание и индексы
fruits = ["apple", "banana", "orange", "kiwi", "mango"]
print(fruits[0])
print(fruits[-1])
print(fruits[3])
print(fruits[3:])
fruits.reverse()
print(fruits)

#Задание 2. Изменение списка
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.insert(1,15)
numbers.pop(3)
numbers[0]=100
print(len(numbers))


#Задание 3. Работа с циклом и условиями
numbers_list = [12, 5, 8, 21, 4, 17, 30, 9]
even_numbers = []
odd_numbers = []

for i in numbers_list:
    if i %2 ==0:
        even_numbers.append(i)
    elif i %2 !=0 :
        odd_numbers.append(i)

print(even_numbers)
print( odd_numbers)

#Задание 4. Сортировка и срезы

scores = [45, 90, 12, 78, 100, 56, 34, 88, 67, 91]
scores.sort(reverse=True)

print(scores)
print(scores[:5])
print(scores[-3])
print(max(scores))
print(min(scores))

print(sum(scores)/len(scores))


#Блок B. TUPLE — 4 задания
#Задание 5. Основы кортежа
my_tuple = ("Python", "Java", "JavaScript", "C++", "C#")
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[:3])
print(len(my_tuple))
print("Python" in my_tuple )
#Задание 6. Распаковка
user = ("Liza", 25, "QA", "Ukraine")
user1,user2, *other=user
print(user1)
print(user2)
print(other)

#Задание 7. Методы кортежа
numbers_count = (1, 2, 3, 2, 5, 2, 7, 3, 9)
print(numbers_count.count(2))
print(numbers_count.index(7))
print(numbers_count.index(3))
print(len(numbers_count))

#Задание 8. Работа с вложенными кортежами

students = (
    ("Liza", 90),
    ("Masha", 75),
    ("Dasha", 100),
    ("Anna", 85)
)

for student in students:
    if student[1]>80:
     print( student[0], student[1])
print(max(students, key=lambda student: student[1]))


#Блок D. SET — 4 задания
#Задание 13. Убираем дубликаты
numberss = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
numberss = set(numberss)
numberss.add(7)
numberss.remove(3)
print(numberss)

#Задание 14. Методы Set
languages = {"Python", "Java", "JavaScript"}

languages.add('C++')
languages.update('C#')
print("Python" in languages)
languages.discard('Java')
print(len(languages))
#Задание 15. Операции с множествами
students_python = {"Liza", "Masha", "Dasha", "Anna"}
students_java = {"Masha", "Anna", "Kate", "Sasha"}

cupple= students_python | students_java
rusult = students_python & students_java
print(cupple)
print(rusult)


#Блок C. DICT — 4 задания

person = {
    "name": "Liza",
    "age": 25,
    "city": "Dnipro",
    "profession": "QA"
}

person.update({'language': 'Python'})
person['age']=26
person.pop('city')
print(person.items())
print(person.get('name'))
print(person.get('age'))

students = {
    "Liza": 95,
    "Masha": 70,
    "Dasha": 88,
    "Anna": 60,
    "Kate": 100
}
passed_students = {}
for mark in students.items():
   if mark[1]>80:passed_students[mark[0]]=mark[1]
print(passed_students)

products = {
    "laptop": {
        "price": 1200,
        "rating": 4.8,
        "stock": 5
    },
    "phone": {
        "price": 800,
        "rating": 4.5,
        "stock": 10
    },
    "tablet": {
        "price": 500,
        "rating": 4.9,
        "stock": 0
    },
    "monitor": {
        "price": 300,
        "rating": 4.2,
        "stock": 7
    }
}
available_products = []
for name, info in products.items():
   #print(name, info['price'])
   if info['stock']>0: available_products.append((name, info))
   available_products.sort(key=lambda stock: stock[1]['price'])
print(available_products)
