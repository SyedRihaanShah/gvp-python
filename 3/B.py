def quadratic_equation(a,b,c):
    print(f"{a}x^2 + {b}x + {c} is the quadratic equation")
    print(f"{a}x^2 + {b}x + {c} sum of roots of this equation is {(-b)/a}")
    print(f"{a}x^2 + {b}x + {c} product of the roots of this equation is {c/a}")
    print(f"{a}x^2 + {b}x + {c} discriminant of this equation is {(b**2) - 4*a*c}")



a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

quadratic_equation(a,b,c)