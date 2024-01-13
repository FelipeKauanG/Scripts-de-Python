# return statement = Functions send Python values/objects back to the caller.
# These values/objects are known the function's return value.

def multiply(num1=1, num2=1):
    result = num1 * num2
    return result


x = multiply()
print(x)
