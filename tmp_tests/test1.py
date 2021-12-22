from math import ceil


def bin_format(x):
    if x is None:
        return None
    num_bytes = ceil(x.bit_length() / 8) + int(x < 0)
    ba = x.to_bytes(num_bytes, 'big', signed=x < 0)
    return ''.join(' {:08b}'.format(b) for b in ba) + ' ({:6d})'.format(x)


def sum_iteration(a, b):
    t = a ^ b
    b = (a & b) << 1
    a = t
    return a, b


def get_sum_3(a: int, b: int) -> int:
    if a >= 0 and b >= 0 or a <= 0 and b <= 0:
        is_negative = a < 0
        while b > 0:
            a, b = sum_iteration(a, b)
        return get_sum_3(~a, 1) if is_negative else a
    elif a < 0:
        print(f' 0: {bin_format(a):>40s}', f'{bin_format(b):>40s}')
        for i in range(1, 110):
            a, b = sum_iteration(a, b)
            print(f'{i:>2d}: {bin_format(a):>40s}', f'{bin_format(b):>40s}')
            if b & 0xFFFF == 0:
                if (a & 0xFFFF) > 0x7FFF:
                    pass
                else:
                    a = a & 0xFFFF

                print('----')
                print(f'{i:>2d}: {bin_format(a):>40s}')
                break
    else:
        return get_sum_3(b, a)


res = get_sum_3(-37, 95)
print(bin_format(res))
print('-----------------------')
res = get_sum_3(-95, 37)
print(bin_format(res))
