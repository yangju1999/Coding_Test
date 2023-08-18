def solution(s):
    result = len(s) 
    mid = result//2 
    for word in range(1, mid+1):
        now_string = ''
        now_word = s[0:word]
        count = 1 
        for i in range(word, len(s), word):

            if s[i:i+word] == now_word:
                count += 1
                
            else:
                if count != 1:
                    now_string = now_string + str(count) + now_word  
                else:
                    now_string = now_string + now_word

                now_word = s[i:i+word]
                count = 1 

        now_string += str(count) + now_word if count >=2 else now_word 

        if len(now_string) < result:
            result = len(now_string)

    print(f'result:{result}')

s = input() 
solution(s) 
