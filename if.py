speed = int(input("Enter Top speed: "))

if speed<=100 and speed>=0:
    print("You have a car")
elif speed<=200 and speed>=101:
    print("You have a speedy car")
elif speed<=300 and speed>=201:
    print("You have super car")
elif speed<=400 and speed>=301:
    print("You have hyper car")
else:
    print("You have a bugatti")



