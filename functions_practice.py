def hello():
    print("Hello, user!")
hello()

def pack(arg1, arg2, arg3):
    print([arg1, arg2, arg3])
    return [arg1, arg2, arg3]
pack("books", "clothes", "laptob")


def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")  
      else:
        print(f"Next I eat {my_lst[i]}")
  
my_lunch = ["biscuits", "grapes", "pizza"]
empty = []

eat_lunch(empty)
eat_lunch(my_lunch)
