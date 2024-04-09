user_equation = input("Enter the quadratic equation '<a>x^2 + <b>x + <c> = 0'")

splitted = user_equation.split()

joined_str = ' '.join(splitted)

print(joined_str)

a = float(joined_str.split('x^2')[0].strip())

b = float(joined_str.split('x^2')[1].split('x')[0].strip()) 

c = float(joined_str.split('x^2')[1].split('x')[1].split('=')[0]
          .replace('+', '').replace('(', '').replace(')', '').strip()) 
print(a, b, c) 

res = f'{a}x^2 + {b}x + {c} = 0'
print(res)

x1 = (-b + (b**2 - 4*a*c) * 0.5) / (2*a)
x2 = (-b - (b**2 - 4*a*c) * 0.5) / (2*a)
print(f'The roots are {x1} and {x2}')
