#Square root of a Equation
a = int(input("Enter the x^2 coefficient: "))
b = int(input("Enter the x^1 coefficient: "))
c = int(input("Enter the x^0 coefficient: "))
r1 = (-b+(b*2 - 4*a*c)**0.5)/2*a
r2 = (-b-(b*2 - 4*a*c)**0.5)/2*a
print("The roots of the given equation are {} and {}".format(r1,r2))

