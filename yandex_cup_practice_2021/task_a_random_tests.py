#!/usr/bin/env python3

import sys
import random
import string
import subprocess


def get_random_strings(num):
    symbols = string.ascii_lowercase + string.ascii_uppercase + ' '
    l_ascii_len = len(string.ascii_lowercase)
    u_ascii_len = len(string.ascii_uppercase)
    symbols_p = [0.7 / l_ascii_len] * l_ascii_len + [0.1 / u_ascii_len] * u_ascii_len + [0.2]
    return [''.join(random.choices(symbols, weights=symbols_p, k=random.randint(0, 50))) for _ in range(num)]


def solution(s):
    def if_lowercase(c, y, n, s):
        if 'a' <= c <= 'z':
            return y
        elif 'A' <= c <= 'Z':
            return n
        else:
            return s

    small = [0] * (len(s) + 1)
    big = [0] * (len(s) + 1)

    for i, c in enumerate(s, 1):
        small[i] = min(small[i-1] + if_lowercase(c, 1, 2, 1),
                       (big[i-1] + if_lowercase(c, 3, 3, 3)) if i > 1 else sys.maxsize)

        big[i] = min(small[i-1] + if_lowercase(c, 3, 3, 3),
                     (big[i-1] + if_lowercase(c, 2, 1, 1)) if i > 1 else sys.maxsize)

    return min(small[-1], big[-1])


def get_ground_truth(s):
    """
    a.out - это скомиплированное решение
        #include <string>
        #include <iostream>
        #include <vector>
        #include <cstdint>
        #include <numeric>
        #include <array>

        void run(std::istream &in, std::ostream &out) {
            std::string s;
            std::getline(in, s);
            int n = s.length();
            std::array<std::vector<int>, 2> dyn;
            dyn[0].assign(n + 1, 0);
            dyn[1].assign(n + 1, 0);
            dyn[1][0] = 2 * n + 2;
            for (int i = 0; i < n; i++) {
                char c = s[i];
                if (c >= 'a' && c <= 'z') {
                    dyn[1][i + 1] = dyn[1][i] + 1;
                    dyn[0][i + 1] = std::min(dyn[0][i], dyn[1][i] + 2);
                } else if (c >= 'A' && c <= 'Z') {
                    dyn[0][i + 1] = dyn[0][i] + 1;
                    dyn[1][i + 1] = std::min(dyn[1][i], dyn[0][i] + 2);
                } else {
                    dyn[0][i + 1] = dyn[0][i];
                    dyn[1][i + 1] = dyn[1][i];
                }
            }
            int ans = std::min(dyn[0][n], dyn[1][n]) + n;
            out << ans << "\n";
        }

        int main() {
          std::cin.sync_with_stdio(false);
          std::cin.tie(nullptr);
          run(std::cin, std::cout);
          return 0;
        }
    """
    p = subprocess.Popen(["./a.out"],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True,
                         bufsize=0)

    p.stdin.write(f'{s}\n')
    p.stdin.close()
    return p.stdout.read().strip()


for i in get_random_strings(100):
    res = solution(i)
    gth = get_ground_truth(i)
    if gth != str(res):
        print(f'{i : <50}\t{res}\t{gth}\t!!!')

