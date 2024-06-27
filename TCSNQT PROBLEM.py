# You are provided with a list of sales entries, each entry containing three fields: the name of the item, the price per unit, and the number of units sold. An item can appear multiple times in the list with different units sold each time. Your task is to compute the total sales, the average sales per entry, and identify the best-selling item based on total revenue generated from that item.
#
# Input Format:
#
# You will be given a list of tuples, each tuple containing a string and two floats. The string represents the item name, the first float represents the price per unit, and the second float represents the number of units sold.
# Output Format:
#
# Print the total sales rounded to two decimal places.
# Print the average sales per entry rounded to two decimal places.
# Print the name of the best-selling item based on the total sales.
# Constraints:
#
# The list will have at least one entry.
# The price per unit will be a positive decimal number.
# The units sold will be a non-negative integer
# Input:
#
# [ (“Tomato”, 2.0, 3),(“Potato”, 1.5, 10), (“Tomato”, 2.0, 2),(“Carrot”, 1.0, 8),(“Potato”, 1.5, 5)]
#
# Output:
#
# Total Sales: $47.50
#
# Average Sales: $9.50
#
# Best Selling Item: Potato
#
# Explanation:
#
# The total sales are calculated as follows: (2.0×3)+(1.5×10)+(2.0×2)+(1.0×8)+ (1.5×5)=6+15+4+8+7.5-40.5.
#
# (2.0×3)+(1.5×10)+(2.0×2)+(1.0×8)+(1.5×5)=6+15+4+8+7.5-40.5
#
# Average sales per entry: 40.5/5-9.5. 40.5/5-9.5
#
# Best selling item: “Potato” generates the most sales ($22.5 from selling 15 units at $1.5 each

def calculation(entries):
    total_sales=0
    product_list={}
    for i in entries:
        total_sales+=i[1]*i[2]
        if i[0] not in product_list.keys():
            product_list[i[0]]=i[1]*i[2]
        else:
            product_list[i[0]]+=i[1]*i[2]
    average_sales=total_sales/len(entries)
    best_selling_prodct=max(product_list,key=product_list.get)

    return total_sales,average_sales,best_selling_prodct

entries = [("Tomato", 2.0, 3), ("Potato", 1.5, 10), ("Tomato", 2.0, 2), ("Carrot", 1.0, 8), ("Potato", 1.5, 5)]

total_sales,average_sales,best_selling_product=calculation(entries)
print(f"Total Sales:${total_sales:.2f}")
print(f"Average Sales:${average_sales:.2f}")
print("Best Selling Item:",best_selling_product)



