#3
lst1= ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
def new_list_creation():
    new_list=[]
    for i in lst1:
        if isinstance(i, str):
         new_list.append(i)
    print(new_list)

new_list_creation()