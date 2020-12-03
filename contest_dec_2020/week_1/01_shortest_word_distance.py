"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3550/

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
from typing import List


def shortest_distance(words: List[str], word1: str, word2: str) -> int:
    min_distance = None
    prev_word = None
    prev_word_idx = None
    for i, word in enumerate(words):
        if word not in (word1, word2):
            continue

        if word == prev_word or prev_word is None:
            prev_word_idx = i
        else:
            distance = i - prev_word_idx
            if min_distance is None or distance < min_distance:
                min_distance = distance

        prev_word = word
        prev_word_idx = i

    return min_distance


print(shortest_distance(['a', 'c', 'b', 'a'], 'a', 'b'))
