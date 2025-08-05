def dec_to_bin(n):
    """
    :param n:
    :return n converted to octal:
    """
    dict_b_octal = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7'}
    q = n
    result = ''
    while q > 0:
        r = q % 8
        oc_digit = dict_b_octal[r]
        result = oc_digit + result
        q = q // 8
    return result


if __name__ == "__main__":
    n = int(input())
    print(dec_to_bin(n))
