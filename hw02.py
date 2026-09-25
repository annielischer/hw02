# Annie Lischer, 9/25/26

# This function receives two int inputs and returns them
def read_two_ints():
    x=input("give me x: ")
    x=int(x)
    y=input("give me y: ")
    y=int(y)
    return x,y

# This function multiplies two ints then prints the product
# This function adds two ints then prints the sum
# This function then divides the product and sum and returns it
def compute_multadd(a, b):
    numer=a*b
    print(f"mult result: {numer}")
    denom=a+b
    print(f"add result: {denom}")
    return numer/denom

# This function prints three variables
def print_fancy(a, b, ab_multadd):
    print("*"*16)
    print("RESULTS:")
    print(f"first number: {a}")
    print(f"second number: {b}")
    print(f"multadd result: {ab_multadd}")
    print("="*16)

# This function calls previous functions in order to do then print math
def main ():
    # Returns two ints
    x,y=read_two_ints()
    # Does math with two ints and returns a third
    xy_multadd=compute_multadd(x,y)
    # Prints three variables (ints are variables)
    print_fancy(x,y,xy_multadd)

    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()

# [x] you added your name to the top comments of the python file
# [x] runs without syntax errors (or -50%)
# [x] adds a few small but informative comments (or -5%)
# [ ] adds docstrings to each function (or -5%)
"""I did not do the above because I find the grey easier to read when inside text and also think the
    that a comment describing a func should be atop and not inside it. Just personal opinions on readability.
    And also maybe me not entirely understanding what the difference is supposed to be between these two boxes."""
# [x] Passes all tests (or lose 15% per missed test). If you do not pass all tests, do not check this box
# [x] You checked the correct boxes
