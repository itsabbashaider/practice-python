def dec_to_bin(n):
    """
    :param n:
    :return n converted to binary:
    """
    q = n
    result = ''
    while q > 0:
        r = q % 2
        hx_digit = str(r)
        result = hx_digit + result
        q = q // 2
    return result


if __name__ == "__main__":
    n = int(input())
    print(dec_to_bin(n))
