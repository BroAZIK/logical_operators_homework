def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = a%10
    c = a//10
    v = c//10
    return(x+c+v)%2==0
print(main(123))