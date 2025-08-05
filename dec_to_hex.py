def dec_to_hex(n):
    """
    :param n:
    :return n converted to hexadecimal:
    """
    dict_b_hex = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    result = ''
    q = n
    while q > 0:
        r = q % 16
        hx_digit = dict_b_hex[r]
        result = hx_digit + result
        q = q // 16
    return result


if __name__ == "__main__":
    n = int(input())
    print(dec_to_hex(n))
