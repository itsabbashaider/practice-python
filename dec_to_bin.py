def dec_to_bin(n):
    """
    :param n:
    :return n converted to binary:
    """
    dict_b_bin = {0:'0',1:'1'}
    q = n
    result = ''
    while q > 0:
        r = q % 2
        hx_digit = dict_b_bin[r]
        result = hx_digit + result
        q = q // 2
    return result


if __name__ == "__main__":
    n = int(input())
    print(dec_to_bin(n))
