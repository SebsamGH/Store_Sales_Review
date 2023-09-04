
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#  calculate the total price average for all products

total = sum(prices)
print("Total: $", total)
average = total/len(prices)
print("Average: $" + str(round(average,2)))

#   create a new price list that reduces the old prices by $ 5


products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
new_prices = [25, 20, 35, 15, 15, 30, 40, 45, 30]


total = sum(new_prices)
print("Total: $", total)


#calculate the average daily revenue generated from the products

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

weekly_revenue = sum(last_week)
print("Weekly Revenue: $", weekly_revenue)

days_of_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
daily_revenue = (weekly_revenue /7)
print("daily Revenue: $",  daily_revenue)

dail_average = weekly_revenue/len(last_week)
print("Average daily Revenue: $: " + str(round(dail_average,2)))

# based on the new prices, which products are less than $ 30 

new_products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

new_prices = [25, 20, 35, 15, 15, 30, 40, 45, 30]
 
products_less_than_30 =(new_products[0], new_products[1], new_products[3], new_products[4],) 

print("product_less_than_$30 :", products_less_than_30)