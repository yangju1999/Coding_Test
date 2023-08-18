from bisect import bisect_left, bisect_right 
from copy import deepcopy 

def first_parsing(word):
    result =''
    for i in range(len(word)):
        if word[i] == '?':
            result += 'a'
        else:
            result += word[i]
    return result


def second_parsing(word):
    result =''
    for i in range(len(word)):
        if word[i] == '?':
            result += 'z'
        else:
            result += word[i]
    return result 

def reverse_words(words):
    result = []
    for w in words:
        result.append(w[::-1])
    return result 

def solution(words, queries):
    answer = []
    words_by_length =  [[] for _ in range(10001)]
    for w in words:
        words_by_length[len(w)].append(w)

    words_by_length_reverse = deepcopy(words_by_length)

    for i in range(1, 10001):
        words_by_length[i] = sorted(words_by_length[i])
        words_by_length_reverse[i] = sorted(reverse_words(words_by_length_reverse[i]))
    

    for q in queries:
        length = len(q)
        if q[0] == '?':
            left_index = bisect_left(words_by_length_reverse[length], first_parsing(q)[::-1])
            right_index = bisect_right(words_by_length_reverse[length], second_parsing(q)[::-1]) 
            now = right_index - left_index 
            answer.append(now)

        elif q[-1] == '?': 
            left_index = bisect_left(words_by_length[length], first_parsing(q))
            right_index = bisect_right(words_by_length[length], second_parsing(q)) 
            now = right_index - left_index 
            answer.append(now)

    return answer

print(solution(['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao'], ['fro??', '????o', 'fr???', 'fro???', 'pro?'])) 