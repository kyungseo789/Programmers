def solution(s):
    answer = ''
    lower_alphabet = []
    upper_alphabet = []
    for i in s:
        if i.islower():
            lower_alphabet.append(i)
        else:
            upper_alphabet.append(i)
            
    lower_alphabet.sort(reverse=True)
    upper_alphabet.sort(reverse=True)
    lower_alphabet.extend(upper_alphabet)
    answer = "".join(lower_alphabet) 
    return answer