def find_solution(equation: str) -> str:
    equation_list = equation.split()
    a = float(equation_list[0][0])
    b = float(''.join([equation_list[1], equation_list[2][0]]))
    c = float(''.join([equation_list[3], equation_list[4]]))

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return 'No solutions'
    elif discriminant == 0:
        x = -b / (2*a)
        return str(x)
    else:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return f'{x1}, {x2}'


if __name__ == '__main__':
    equation = '5x^2 - 4x + 2'
    print(find_solution(equation))