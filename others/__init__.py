from math import ceil


"""
TODO: study hacks from https://graphics.stanford.edu/~seander/bithacks.html
"""


def bin_format(x, decimal_padding=6):
    if x is None:
        return None
    is_negative = x < 0
    num_bytes = ceil(x.bit_length() / 8) + int(is_negative)
    x_bytes = x.to_bytes(num_bytes, 'big', signed=is_negative)
    x_bytes_str = ' '.join('{:08b}'.format(b) for b in x_bytes)
    x_deciaml_str = '{{:>{}d}}'.format(decimal_padding).format(x)
    return f'{x_bytes_str} ({x_deciaml_str})'
