"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/

Reverse bits of a given 32 bits unsigned integer.

Note:
    - Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output
      will be given as a signed integer type. They should not affect your implementation, as the integer's internal
      binary representation is the same, whether it is signed or unsigned.
    - In Java, the compiler represents the signed integers using 2's complement notation
      (https://en.wikipedia.org/wiki/Two%27s_complement). Therefore, in Example 2 above, the input represents the
      signed integer -3 and the output represents the signed integer -1073741825.

Follow up:
If this function is called many times, how would you optimize it?

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
             so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
             so return 3221225471 which its binary representation is 10111111111111111111111111111111.

Constraints:
The input must be a binary string of length 32
"""


class Solution:
    def reverse_bits(self, n: int) -> int:
        bs = [0] * 32
        z = n
        for i in range(len(bs)):
            if z <= 0:
                break
            bs[i] = z % 2
            z = z // 2

        r = 0
        for i, b in enumerate(reversed(bs)):
            r += (b * (2 ** i))

        return r

    def reverse_bits2(self, n: int) -> int:
        s = 0
        z = n
        for i in range(32):
            s += ((2 * (z % 2)) ** (32 - i - 1))
            z = z // 2
            if z <= 0:
                break

        return s

    def reverse_bits3(self, n: int) -> int:
        def reverse_byte(b):
            return (b * 0x0202020202 & 0x010884422010) % 1023

        """
        0) n = x8 x7 x6 x5 x4 x3 x2 x1
        1) * 0x0202020202 - дублирование бинарного представления n 5 раз в одном 64 битном числе
        2) & 0x010884422010 - маскирование числа из п. 1 таким образом, что в каждой группе из 10 бит выбираются
           один или два бита на тех позициях, которые при сложении (групп из 10 бит) дадут обратный порядок бит
           ?: 10 битовые группы это важно, иначе не получится правильным образом замаскировать нужные биты
           ?: почему именно 10 не понятно
        3) % 1023 - фактически сложение замаскированных в п.2 групп из 10 бит.
           Как это происходит: если представить систему счисления по основанию 1024, то получившееся число в п.2 
           можно записать как g5g4g3g2g1 (g5,...g1 - это символы из системы счисления по основанию 1024)
           g1 в двоичном представлении равно первой группе из п.2
           ...
           g5 в двоичном представлении равно первой группе из п.2
           Остаток от деление в любой(?) системе счисления по основанию [b] на число b-1 равен
           "сумма цифр из представления этого числа в системе счисления по основанию [b]"
             % 
           (b-1)
        """

        # http://graphics.stanford.edu/~seander/bithacks.html#ReverseByteWith64BitsDiv
        s = 0
        for i in range(4):
            p = reverse_byte((n >> (8 * i)) & 0xff)
            s += (p << (8 * (3 - i)))

        return s


sol = Solution()
print(sol.reverse_bits(43261596))
print(sol.reverse_bits(4294967293))
print('------------------')
print(sol.reverse_bits2(43261596))  # 00000010100101000001111010011100
print(sol.reverse_bits2(4294967293))
print('------------------')
print(sol.reverse_bits3(43261596))  # 0000 0010  1001 0100  0001 1110  1001 1100
print(sol.reverse_bits3(4294967293))
