employee_salary = float(input("ENTER YOUR SALRY.\n"))
employee_year_of_service = int(input("ENTER YEARS OF SERVICE.\n"))
if employee_year_of_service >= 5:
    net_bonus = (0.15 * employee_salary)
    print("CONGRATULATION YOU'VE EARNED YOURSELF A BONUS.")
    print("YOUR NET BONUS IS Ksh " + str(net_bonus))
else:
    net_bonus = 0
    print("YOU ARE NOT ELIGIBLE FOR BONUS.")
    print("YOUR NET BONUS IS Ksh " + str(net_bonus))
