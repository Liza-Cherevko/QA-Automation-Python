#2
def put_word_with_h():
    put_word = input()
    while not ('h'in put_word.lower()):
      print("Please, put the word with 'h'")
      put_word = input()
      if 'h' in put_word.lower():
        print('Thank you!')

put_word_with_h()

