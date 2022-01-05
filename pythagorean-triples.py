import math
import msvcrt

from PyMohsen import LoopBreakException

if (__name__ == '__main__'):
    # Getting number of pythagorean triples from user...
    while True:
        try:
            num = int(input("Specify number of pythagorean triples to be found: "))
            if num <= 0:
                raise ValueError()
            break
        except ValueError:
            print("\tYour input is incorrect.")
            print('-' * 40)

    # Finding Pythagorean triples...
    n = 0
    num_digits = math.ceil(math.log10(num))
    try:
        # The first known pythagorean triple is (3, 4, 5), so starting at 5...
        c = 5
        while True:
            not_separated = True
            # Looping through c-1, c-2, c-3, ..., 3, 2, 1...
            for b in range(c-1, 0, -1):
                a_squared = c**2 - b**2
                a = math.isqrt(a_squared)
                # Avoiding (a, b, c) & (b, a, c) in results...
                if a >= b:
                    break
                elif a_squared == a**2:
                    # One solution has been found...
                    n += 1
                    if not_separated:
                        print('\t', '-' * 40)
                        not_separated = False
                    print('\t', str(n).rjust(num_digits), ': ', (a, b, c), sep='')
                    if (n >= num):
                        # We've done, quitting the algorithm...
                        raise LoopBreakException()
            c += 1
    except LoopBreakException:
        pass
    
    print('Press any key to quit: ', end='', flush=True)
    msvcrt.getwche()