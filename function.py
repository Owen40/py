# def hello():
#     print("This is my first function")
#
# hello()
#
# def calculate():
#     x=30
#     y=25
#     print(x*y)
#
# calculate()
#
# def maina(fname, lname):
#     print(fname+ " " +lname)
# maina("Nolari", "John")
# maina("Carol", "Stacy")
# maina("Joanna", "Furaha")
#
# def greetings(name, greeting="Hello"):
#     print(greeting + " " + name)
# greetings("Nolari")
#
# def login(name, password, greet="Hello"):
#     print(greet + " " + name + ", your password is " + password)
#
# login("Listless17", "Password123")
#
# def maxvalu(a,b,c,d,e,f):
#     return max(a,b,c,d,e,f)
# result=maxvalu(1,9,18,20,2,5)
# print(result)
#
# def minvalu(num1,num2,num3,num4,num5,num6,num7):
#     return min(num1,num2,num3,num4,num5,num6,num7)
# res = minvalu(2,4,10,45,1,20,5)
# print(res)

# def sort_list(lst):
#     return sorted(lst)
# answer=sort_list([3,9,0,2,7,1,5,4,2,20])
# print(answer)

def print_numbers(n):
    for i in range(n):
        print(i)

print_numbers(20)