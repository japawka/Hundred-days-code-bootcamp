def my_function(a, b):
    result = a * b
    return result


output = my_function
print(output(4, 56))


def format_name(f_name, l_name):
    """Returns formatted name an surname as titles"""
    if f_name == "" or l_name == "":
        return 'No valid inputs'
    a = f_name.title()
    b = l_name.title()
    return f'Result: {a} {b}'



print(format_name(input('What is ypur first name'), input('What is ypur last name')))


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return 'Invalid month'
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


