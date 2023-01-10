"""
https://leetcode.com/problems/guess-the-word/

You are given an array of unique strings words where words[i] is six letters long. One word of words was chosen as a
secret word.
You are also given the helper object Master. You may call Master.guess(word) where word is a six-letter-long string,
and it must be from words. Master.guess(word) returns:
    * -1 if word is not from words, or
    * an integer representing the number of exact matches (value and position) of your guess to the secret word.

There is a parameter allowedGuesses for each test case where allowedGuesses is the maximum number of times you can call
Master.guess(word).
For each test case, you should call Master.guess with the secret word without exceeding the maximum number of allowed
guesses. You will get:
    * "Either you took too many guesses, or you did not find the secret word." if you called Master.guess more than
      allowedGuesses times or if you did not call Master.guess with the secret word, or
    * "You guessed the secret word correctly." if you called Master.guess with the secret word with the number of calls
      to Master.guess less than or equal to allowedGuesses.

The test cases are generated such that you can guess the secret word with a reasonable strategy (other than using the
bruteforce method).

Example 1:
    Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
    Output: You guessed the secret word correctly.

Explanation:
    master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
    master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
    master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
    master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
    master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
    We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.

Example 2:
    Input: secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
    Output: You guessed the secret word correctly.

Explanation: Since there are two words, you can guess both.

Constraints:
    * 1 <= words.length <= 100
    * words[i].length == 6
    * words[i] consist of lowercase English letters.
    * All the strings of wordlist are unique.
    * secret exists in words.
    * 10 <= allowedGuesses <= 30
"""
from typing import List
from collections import Counter


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


class Master:
    def __init__(self, words: List[str], max_attempts: int, secret: str):
        self.words = set(words)
        self.max_attempts = max_attempts
        self.secret = secret
        self.attempts = 0

    def guess(self, word: str) -> int:
        self.attempts += 1
        if self.attempts > self.max_attempts:
            raise Exception('max attempts reached')
        if word not in self.words:
            return -1
        ret_num = 0
        for i in range(6):
            if word[i] == self.secret[i]:
                ret_num += 1
        return ret_num


class Solution:
    def make_similarity_matrix(self, words: List[str]):
        nw = len(words)
        matrix = [[0 for _ in range(nw)] for _ in range(nw)]
        for i in range(len(words)):
            for j in range(i, len(words)):
                num_match = 0
                if i == j:
                    num_match = 6
                else:
                    for k in range(6):
                        if words[i][k] == words[j][k]:
                            num_match += 1
                matrix[i][j] = num_match
                matrix[j][i] = num_match

        return matrix

    def choose_word(self, matrix, exclude_words):
        max_set_size = dict()
        for ri, row in enumerate(matrix):
            if ri not in exclude_words:
                b = Counter([c for i, c in enumerate(row) if i not in exclude_words])
                max_set_size[ri] = max([b[i] for i in b])

        word_entry = min(max_set_size.items(), key=lambda x: x[1])
        return word_entry[0]

    def find_secret_word(self, words: List[str], master: Master) -> None:
        matrix = self.make_similarity_matrix(words)
        exclude_words = set()
        for i in range(31):
            word_idx = self.choose_word(matrix, exclude_words)
            num_matches = master.guess(words[word_idx])
            if num_matches == 6:
                print('Found match, attempt ', i)
                return

            for j in range(len(matrix) - 1, -1, -1):
                if matrix[word_idx][j] != num_matches:
                    exclude_words.add(j)

        raise Exception('word not found')


def test1():
    words = ['gaxckt', 'trlccr', 'jxwhkz', 'ycbfps', 'peayuf', 'yiejjw', 'ldzccp', 'nqsjoa', 'qrjasy', 'pcldos',
             'acrtag', 'buyeia', 'ubmtpj', 'drtclz', 'zqderp', 'snywek', 'caoztp', 'ibpghw', 'evtkhl', 'bhpfla',
             'ymqhxk', 'qkvipb', 'tvmued', 'rvbass', 'axeasm', 'qolsjg', 'roswcb', 'vdjgxx', 'bugbyv', 'zipjpc',
             'tamszl', 'osdifo', 'dvxlxm', 'iwmyfb', 'wmnwhe', 'hslnop', 'nkrfwn', 'puvgve', 'rqsqpq', 'jwoswl',
             'tittgf', 'evqsqe', 'aishiv', 'pmwovj', 'sorbte', 'hbaczn', 'coifed', 'hrctvp', 'vkytbw', 'dizcxz',
             'arabol', 'uywurk', 'ppywdo', 'resfls', 'tmoliy', 'etriev', 'oanvlx', 'wcsnzy', 'loufkw', 'onnwcy',
             'novblw', 'mtxgwe', 'rgrdbt', 'ckolob', 'kxnflb', 'phonmg', 'egcdab', 'cykndr', 'lkzobv', 'ifwmwp',
             'jqmbib', 'mypnvf', 'lnrgnj', 'clijwa', 'kiioqr', 'syzebr', 'rqsmhg', 'sczjmz', 'hsdjfp', 'mjcgvm',
             'ajotcx', 'olgnfv', 'mjyjxj', 'wzgbmg', 'lpcnbj', 'yjjlwn', 'blrogv', 'bdplzs', 'oxblph', 'twejel',
             'rupapy', 'euwrrz', 'apiqzu', 'ydcroj', 'ldvzgq', 'zailgu', 'xgqpsr', 'wxdyho', 'alrplq', 'brklfk']
    master = Master(words, 10, 'hbaczn')
    sol = Solution()
    sol.find_secret_word(words, master)


test1()

# TODO: implment also https://leetcode.com/problems/guess-the-word/solutions/134087/elimination-histogram/
