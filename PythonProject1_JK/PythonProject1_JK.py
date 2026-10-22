def discount_calc(employee_type, years_employed):
    '''
    Calculates the discount based on employee type and years employed.

    Args:
        employee_type (int): Whether the employee is management or otherwise. 1 is for management, 2 or more for anything else.
        years_employed (int): How many years the employee has been employed at the company.

    Returns:
        float: discount
        
    '''
    if employee_type == 1:
        if years_employed >= 1 and years_employed <= 3:
            discount = 0.2
        elif years_employed >= 4 and years_employed <= 6:
            discount = 0.24
        elif years_employed >= 7 and years_employed <= 10:
            discount = 0.3
        elif years_employed >= 11 and years_employed <= 15:
            discount = 0.35
        else:
            discount = 0.4

    else:
        if years_employed >= 1 and years_employed <= 3:
            discount = 0.1
        elif years_employed >= 4 and years_employed <= 6:
            discount = 0.14
        elif years_employed >= 7 and years_employed <= 10:
            discount = 0.2
        elif years_employed >= 11 and years_employed <= 15:
            discount = 0.25
        else:
            discount = 0.3
    return discount

def final_cost_and_outputs(charge, discount, ytd_discount, discount_on_charge):
    '''
    Calculates the final cost and displays all the outputs.

    Args:
        charge (int or float): Cost of the purchase.
        discount (float): Discount for the purchase.
        ytd_discount (int or float): Amount of money you've saved with discounts throughout your career.
        discount_on_charge (int or float): Amount of money you saved on this purchase.
        
    Returns:
        int or float: final_cost
    '''
    if ytd_discount >= 200:
        final_cost = charge
        discount = 0
        discount_on_charge = 0
    else:
        if ytd_discount + discount_on_charge <= 200:
            final_cost = charge - discount_on_charge

        elif ytd_discount + discount_on_charge > 200:
            discount_on_charge = (discount_on_charge - ((ytd_discount + discount_on_charge) - 200))
            final_cost = charge - discount_on_charge 

    print("Employee Discount: ", discount * 100, "%")
    print("YTD Discount: ", "${:,.2f}".format(ytd_discount))
    print("Charge before Discount: ", "${:,.2f}".format(charge))
    print("Discount for Today's Purchase: ", "${:,.2f}".format(discount_on_charge))
    print("Total with Discount", "${:,.2f}".format(final_cost))
    return final_cost

def calculation_and_output(years_employed, money_spent, employee_type, charge):
    '''
    Calls the discount calculation function, the final cost and output function, and calculates ytd discount and discount on charge.

    Args:
        years_employed (int): How many years the employee has been employed at the company.
        charge (int or float): Cost of the purchase.
        employee_type (int): Whether the employee is management or otherwise. 1 is for management, 2 or more for anything else.
        money_spent (int or float): Amount of money you've spent on previous purchases throughout your career.

    Returns:
        function: final cost and outputs function, i.e: final cost
    '''
    discount = discount_calc(employee_type, years_employed)
    ytd_discount = money_spent * discount
    discount_on_charge = charge * discount
    return final_cost_and_outputs(charge, discount, ytd_discount, discount_on_charge)

def validation(strData):
    try:
        float(strData)
        return True

    except ValueError:
        return False

def years_employed_value():
    years_employed = input("How long have you been employed? (In Years): ")
    if validation(years_employed) == True:
        return int(years_employed)
    else:
        while validation(years_employed) == False:
            print("Please input a number")
            years_employed = input("How long have you been employed? (In Years): ")
            validation(years_employed)
        return int(years_employed)

def money_spent_value():
    money_spent = input("How much in purchases have you spent previously? (Before discounts): ")
    if validation(money_spent) == True:
        return float(money_spent)
    else:
        while validation(money_spent) == False:
            print("Please input a number")
            money_spent = input("How much in purchases have you spent previously? (Before discounts): ")
            validation(money_spent)
        return float(money_spent)

def employee_type_value():
    employee_type = input("Are you a manager (1) or standard employee? (2+): ")
    if validation(employee_type) == True:
        return int(employee_type)
    else:
        while validation(employee_type) == False:
            print("Please input a number")
            employee_type = input("Are you a manager (1) or standard employee? (2+): ")
            validation(employee_type)
        return int(employee_type)

def charge_value():
    charge= input("Total of today's purchase?: ")
    if validation(charge) == True:
        return float(charge)
    else:
        while validation(charge) == False:
            print("Please input a number")
            charge = input("Total of today's purchase?: ")
            validation(charge)
        return float(charge)

def application():
    '''
    Provides inputs, runs accumulating loop and associated variables, displays accumulating variables when loop ends.
    '''
    employee_processing = "Y"
    total_charge = 0
    total_final_costs = 0
    while employee_processing == "Y":
        years_employed = years_employed_value()
        money_spent = float(money_spent_value())
        employee_type = int(employee_type_value())
        charge = float(charge_value())
        total_final_costs += calculation_and_output(years_employed, money_spent, employee_type, charge)
        total_charge += charge
        employee_processing = str(input("Another Employee? (Y/N): "))
    print("Total Charge: ", "${:,.2f}".format(total_charge))
    print("Total Charge After Discounts: ", "${:,.2f}".format(total_final_costs))

application()