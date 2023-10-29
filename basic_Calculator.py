class basic_Calculator:
    def __init__(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

# creation of 4 methods for different operations here
    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 == 0:
            return "Cannot be divided by zero"
        quotient = float(self.num1) / float(self.num2)
        return quotient


# Instance Creation here
this_Object = basic_Calculator()

print("\nAddition: ", this_Object.addition())
print("Subtraction: ", this_Object.subtraction())
print("Product: ", this_Object.multiplication())
print("Multiplication: ", this_Object.division())
