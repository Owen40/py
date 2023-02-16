# class EmobilisStudent:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def hello_me(self):
#         print(f"My name is {self.name} and I'm {self.age} years old.")
#
# #creating an object
# myobj=EmobilisStudent("Owen", 20)
# myobj2=EmobilisStudent("Joanna", 22)
#
# myobj.hello_me()
# myobj2.hello_me()
#
# class MyCars:
#     def __init__(self, make, model, year,):
#         self.make=make
#         self.model=model
#         self.year=year
#     def car(self):
#         print(f"This is a {self.make} {self.model} made in the year {self.year}.")
#
# cr1=MyCars("Toyota", "Supra", 2019)
# cr2=MyCars("Tesla", "Model s", 2022)
# cr3=MyCars("Mitsubishi", "Lancer Evo", 2015)
# cr4=MyCars("Aston Martin", "V12 Vantage", 2014)
#
# cr1.car()
# cr2.car()
# cr3.car()
# cr4.car()

class Phones:
    def __init__(solo,manufacturer, model, year):
        solo.manufacturer=manufacturer
        solo.model=model
        solo.year=year
    def simu(solo):
        print(f"This is a {solo.manufacturer} {solo.model} made in {solo.year}")

sim1=Phones("Nothing", "Phone 1", 2022)
sim2=Phones("Samsung", "Galaxy M13", 2022)
sim3=Phones("Honor", "7s", 2018)
sim4=Phones("Iphone", "14 Pro", 2022)
sim5=Phones("Asus", "Rog phone", 2018)
sim6=Phones("Motorola", "Razr", 2019)
sim7=Phones("Oneplus", "10 pro", 2022)

sim1.simu()
sim2.simu()
sim3.simu()
sim4.simu()
sim5.simu()
sim6.simu()
sim7.simu()