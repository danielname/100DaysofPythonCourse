total = float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = float(input("How many people to split the bill? "))
cost = total * ((100+tip)/100) / split
rounded_up = round(-((cost * 100)//-1) /100, 2) #this line makes it so that the calculation always rounds up so that you do not underpay the bill -(a//-b) is a de-facto ceiling function. alternatively I could have imported math and used math.ceil
formatted_bill = "{:.2f}".format(rounded_up) #this line makes sure that there are are always 2 decimal places
print(f"Each person should pay: ${formatted_bill}")
# different ways to split check (e.g. by item, etc)