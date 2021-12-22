from math import ceil


# def bin_format(x):
#     if x is None:
#         return None
#     num_bytes = ceil(x.bit_length() / 8) + int(x < 0)
#     ba = x.to_bytes(num_bytes, 'big', signed=x < 0)
#     return ''.join(' {:08b}'.format(b) for b in ba) + ' ({:6d})'.format(x)


def bin_format(x, decimal_padding=6):
    if x is None:
        return None
    is_negative = x < 0
    num_bytes = ceil(x.bit_length() / 8) + int(is_negative)
    x_bytes = x.to_bytes(num_bytes, 'big', signed=is_negative)
    x_bytes_str = ' '.join('{:08b}'.format(b) for b in x_bytes)
    x_deciaml_str = '{{:>{}d}}'.format(decimal_padding).format(x)
    return f'{x_bytes_str} ({x_deciaml_str})'


def sum_iteration(a, b):
    t = a ^ b
    b = (a & b) << 1
    a = t
    return a, b


def get_sum_3(a: int, b: int) -> int:
    print(f'{bin_format(a):>40s}', f'{bin_format(b):>40s}')
    while b & 0xFFFF != 0:
        a, b = sum_iteration(a, b)
        print(f'{bin_format(a):>40s}', f'{bin_format(b):>40s}')

    if (a & 0xFFFF) <= 0x7FFF:
        a = a & 0xFFFF

    # for i in range(1, 100):
    #     a, b = sum_iteration(a, b)
    #     print(f'{i:>2d}: {bin_format(a):>40s}', f'{bin_format(b):>40s}')
    #     if b & 0xFFFF == 0:
    #         if (a & 0xFFFF) <= 0x7FFF:
    #             a = a & 0xFFFF
    #         print('----')
    #         print(f'{i:>2d}: {bin_format(a):>40s}')
    #         break

    print(f'{"------------":>40s}')
    print(f'{bin_format(a):>40s}')
    return a


get_sum_3(-37, 95)
print('--------------------------------------------------------------------------------------------')
get_sum_3(-95, 37)
print('--------------------------------------------------------------------------------------------')
get_sum_3(95, 37)
