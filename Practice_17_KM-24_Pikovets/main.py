from factorial.factorial import fact
from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from logarithm.logarithm import log, ln, lg

def main():
    func_dict = {
    'fact': ['Calculates factorial of natural number n'],
    'exp2': ['Calculates x^2'],
    'exp3': ['Calculates x^3'],
    'root2': ['Calculates the square root of x', 'x >= 0'],
    'root3': ['Calculates the cube root of x'],
    'log': ['Calculates the logarithm of b with base a', 'a > 0, a != 1; b > 0'],
    'ln': ['Calculates the natural logarithm of b', 'b > 0'],
    'lg': ['Calculates the decimal logarithm of b', 'b > 0'],
    }

    print('\nMenu of functions: \n')
    for func, description in func_dict.items():
        print(' '*7 + '|')
        print(f"{func:7}| {description[0]}")

        for text in description[1:]:
            print(f"{' '*7}| {text}")

        print('-'*7 + '|' + '-'*45)


    f = input("\nEnter the name of the function: ")
    f = f.strip()

    try:
        if f == 'fact':
            n = int(input("n = "))
            if n <= 0:
                raise ValueError
            print(f"{f}({n}) = {fact(n)}")
        elif f == 'exp2':
            x = float(input("x = "))
            print(f"{f}({x}) = {exp2(x)}")
        elif f == 'exp3':
            x = float(input("x = "))
            print(f"{f}({x}) = {exp3(x)}")
        elif f == 'root2':
            x = float(input("x = "))
            if x < 0: 
                raise ValueError
            print(f"{f}({x}) = {root2(x)}")
        elif f == 'root3':
            x = float(input("x = "))
            print(f"{f}({x}) = {root3(x)}")
        elif f == 'log':
            a = float(input("a = "))
            b = float(input("b = "))
            if (a <= 0) or (a == 1) or (b <= 0): 
                raise ValueError
            print(f"{f}({a}, {b}) = {log(a, b)}")
        elif f == 'ln':
            b = float(input("b = "))
            if b <= 0: 
                raise ValueError
            print(f"{f}({b}) = {ln(b)}")
        elif f == 'lg':
            b = float(input("b = "))
            if b <= 0: 
                raise ValueError
            print(f"{f}({b}) = {lg(b)}")
        else:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print("Incorrect function...")
    except ValueError:
        print("Incorrect input...")

        

if __name__ == '__main__':
    main()