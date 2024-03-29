# sort the number in words in an string in ascending order

my_str = " Hello my name is Gautam Kushwaha. I want to do codeing at least 7 hours a day. Being a computer science student. I must do coding 7 hours a day. Otherwise it is waste to go without doing coding 7 hours a day. We can't live and become a good coders without doing coding that much time"

words = [word.lower() for word in my_str.split()]
    
words.sort()

for word in words:
  print(word)