a=input("Введіть ваше ім'я = ")

b=input("Введіть ваше прізвище =")

print("Привіт, " + b, a + "!")

import datetime

current_year = datetime.datetime.now().year

year_of_birth = int(input("Введіть рік свого народження: "))

age = current_year - year_of_birth

if age > 18:
    print("Ви повнолітній!")

else:
    print("Вам ще не виповнилося 18 років.")

