num1, num2 = eval(input("Enter 2 numbers seperated by a comma: " ))
try:
    result = num1 / num2
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Dividing by 0 is not possible")
except SyntaxError:
    print("Error: You must enter 2 numbers seperated by a comma (e.g. 2, 3)")
except ValueError:
    print("Error: you must use integers only")
else:
    print("Division successful")
finally:
    print("No matter what, I will always execute")