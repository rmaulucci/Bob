code = raw_input('Enter code: ')

def decipher(word):
    new_word = list(word)
    dict = {'A':'b', 'B':'o', 'C':'i', 'D':'h', 'E':'g', 'F':'k',
            'G':'n', 'H':'q', 'I':'v', 'J':'t', 'K':'w', 'L':'y',
            'M':'u', 'N':'r', 'O':'x', 'P':'z', 'Q':'a', 'R':'j',
            'S':'e', 'T':'m', 'U':'s', 'V':'l', 'W':'d', 'X':'f',
            'Y':'p', 'Z':'c', ' ':''}
    for i in range(len(new_word)):
        new_word[i] = dict[new_word[i]]
    new_word = ''.join(new_word)
    return new_word
    
print '\n',decipher(code)
        
        
        

