#/usr/bin/env python3
# A program to sum the digitals of a factorial result

import numpy as np
import sys

def as_array(fact_result):
    # Convert factorial result integer to an array
    result = []
    while fact_result != 0:
        fact_result, r = divmod(fact_result, 10)
        result.insert(0, r)
    return result
    

def main(f_in):
    # Compute factorial
    fact_result = np.math.factorial(f_in)
    # Convert integer to array of digits
    result = as_array(fact_result)
    # Sum digits of factorial result
    dig_sum = np.sum(result)
    # Display result
    print(dig_sum)

if __name__ == "__main__":
    try:
        f_in = int(sys.argv[1])
        if f_in <= 0:
            print(0)
        else:
            main(f_in)
    except Exception as e:
        print(e)