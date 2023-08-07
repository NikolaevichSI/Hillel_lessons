"""
HomeWork 14
Припустимо, що у нас є дві множини, які містять моделі деяких автомобілів:

car1 = {"Toyota", "Sedan", "Automatic", "Black"} 
car2 = {"Honda", "SUV", "Manual", "White"}
Напишіть логіку, яка повертає множину, що містить спільні моделі обох множин."""

print("\nHomeWork 14\n")

car_1 = {"Toyota", "Sedan", "Automatic", "Black", "White"}
car_2 = {"Honda", "Toyota", "SUV", "Manual", "White"}
com_cars = car_1.intersection(car_2)
print(com_cars)