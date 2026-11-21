#1
def multiplication_table(number):
  multiplier = 1
  while multiplier*number < 25: 
   result=multiplier*number
   print(str(number) + 'x'+ str(multiplier)+ '='+ str(result))
   multiplier += 1

multiplication_table(3)

#2
def sum_calculation(n1,n2):
   result = n1+n2
   print(result)
sum_calculation(3,7)

#3
num_list=[1,2,3,4,5,6,7,8,9,]

def num_list_calc(test_list):
    result= sum(test_list)/len(test_list)
    print(result) 
num_list_calc(num_list)

#4

def revert_function(agr):
  result= str(agr)
  print(''.join(reversed(result)))

revert_function('Test')
revert_function(34678)

#5
word_list=['Liza', 'Test', 'Hello World!', 'Some Text with ! ! !', 'The Longest word in this List']

def longest_word(test_word_list):
  longest_word = test_word_list[0]
  for word in test_word_list:
   if len(longest_word) < len(word):
     longest_word = word
  print(longest_word)

longest_word(word_list)

#6
#str1 = "Hello, world!"
#str2 = "world"
str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"

def find_substring(str1, str2):
    result = str1.find(str2)
    #print(result)
    return result

print(find_substring(str1, str2))

#7
def multiplication_table_01(number):
    # Инициализация счетчика
    multiplier = 1
    results=[]
    # Цикл
    while multiplier * number < 25:
        result = multiplier * number
        result = str(number) + 'x' + str(multiplier) + '=' + str(result)
        results.append(result)
        multiplier += 1

    return results

print(multiplication_table_01(3))

#8 
def sum_calculation(n1,n2):
   #start calculation
   result = n1+n2
   return result
print(sum_calculation(1,12))

#9
def longest_word_01(test_word_list):
  # A variable that stores the first word from the list. 
  longest_word = test_word_list[0]
  #A loop in which words from a list are compared with the variable
  for word in test_word_list:
   if len(longest_word) < len(word):
     #If a word from the list is longer than the variable, the variable is overwritten and the comparison continues.
     longest_word = word
  return longest_word
print(longest_word_01(word_list))

#10
def num_list_calc_01(test_list):
    #strart calculation
    result= sum(test_list)/len(test_list)
    return result
print(num_list_calc_01(num_list))