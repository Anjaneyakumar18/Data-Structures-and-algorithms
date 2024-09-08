'''
    Return the occurences of each letter in the given string  
'''

s='I am anjaneya kumar and i am learning DSA'
frequencies={}

def populate(s):

    for ch in s:

        ch=ch.lower()
        if ch!=' ':
            if ch in frequencies:
                frequencies[ch]+=1
            else:
                frequencies[ch]=1


populate(s)
print(frequencies)