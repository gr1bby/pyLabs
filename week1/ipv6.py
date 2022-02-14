def convert_to_dec(hexadec: str) -> str:
    list_of_hexadec = hexadec.split(hexadec[4])
    converted = list()
    for block in list_of_hexadec:
        sum_of_block = 0
        for el in block:
            sum_of_block += int(el, 16)
        converted.append(str(sum_of_block))
    return ''.join(converted)


if __name__ == '__main__':
    ipv6_str = "ABCD_1111_ABCD_1111_ABCD_1111_ABCD_1111"
    print(convert_to_dec(ipv6_str))
