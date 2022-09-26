#1
your_name = "Jongwon Yoon"
your_address, your_city, your_state, your_zipcode = "7 Ellwood Place", "Newport", "Rhode Island", "02840"
your_telephone_number = "401-239-7254"
your_college_major = "Computer Science"

#2
total_profit = int(input("user input total profit"))
normal_profit = total_profit * 0.23

#3
acre_of_land = 43560
total_sq = int(input("user input total square feets"))
number_of_acres = total_sq / acre_of_land

#4
apple = int(input("how much is apple?"))
banana = int(input("how much is banana?"))
melon = int(input("how much is melon?"))
orange = int(input("how much is orange?"))
strawberry = int(input("how much is strawberry?"))
sub_total = apple+banana+melon+orange+strawberry
print("subtotal is: ", sub_total)
total_amount_of_sale = sub_total * 0.07
print("total amount of sale after tax is: ", total_amount_of_sale)

#5
speed_of_car_per_hour = 70
distance_6_hour = speed_of_car_per_hour * 6
print("distance travel in 6 hours is: {}".format(distance_6_hour))
distance_10_hour = speed_of_car_per_hour * 10
print("distance travel in 10 hours is {}".format(distance_10_hour))
distance_15_hour = speed_of_car_per_hour * 15
print("distance travel in 15 hours is {}".format(distance_15_hour))

#6
amount_of_purchased = int(input("what is your amount of purchase"))
state_tax = 0.05
country_tax = 0.025
total_sale_tax = state_tax + country_tax
total_of_the_sale = amount_of_purchased + (amount_of_purchased * total_sale_tax)

#7
mile_driven = int(input("how many miles did you drive? "))
gas_used = int(input("how much gas did you use? "))
MPG = mile_driven / gas_used

#8
charge_for_the_food = int(input("how much did you get charge from restaurant? "))
restaurant_tip = charge_for_the_food * 0.18
restaurant_sale_tax = charge_for_the_food * 0.07
total_amount_of_meal = charge_for_the_food + restaurant_sale_tax + restaurant_tip
print(total_amount_of_meal, restaurant_sale_tax, restaurant_tip)

#9
current_temp_in_C = int(input("what is current temperature in Celsius? "))
temp_in_F = current_temp_in_C * (9/5) + 32
print(temp_in_F)

#10
cookies = int(input("how many cookies would you like to cook? "))
ingredient_sugar = 1.5 / 48
ingredient_butter = 1 / 48
ingredient_flour = 2.75 / 48
require_sugar = cookies * ingredient_sugar
require_butter = cookies * ingredient_butter
require_flour = cookies * ingredient_flour


#11
total_number_of_student = 20
number_of_male = int(input("number of male: "))
number_of_female = int(input("number of female: "))
percent_of_male = (number_of_male / total_number_of_student) * 100
percent_of_female = (number_of_female / total_number_of_student) * 100
print(percent_of_male, "%")
print(percent_of_female, "%")