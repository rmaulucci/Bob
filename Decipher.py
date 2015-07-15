code = raw_input('Enter code: ')

def decipher(word):
    new_word = list(word)
    dict = {'A':'b', 'B':'o', 'C':'s', 'D':'h', 'E':'g', 'F':'v',
            'G':'m', 'H':'x', 'I':'k', 'J':'t', 'K':'y', 'L':'p',
            'M':'u', 'N':'r', 'O':'j', 'P':'z', 'Q':'a', 'R':'q',
            'S':'e', 'T':'w', 'U':'i', 'V':'l', 'W':'n', 'X':'f',
            'Y':'c', 'Z':'d', ' ':''}
    for i in range(len(new_word)):
        new_word[i] = dict[new_word[i]]
    new_word = ''.join(new_word)
    return new_word
    
print '\n',decipher(code)
        
        
        

