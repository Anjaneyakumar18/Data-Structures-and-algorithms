def anagrams(s1:str,s2:str)->bool:
    table={}

    # populating hash table

    for ch in s1:
        if ch in table:
            table[ch]+=1
        else:
            table[ch]=1


    for ch in s2:
        if ch in table:
            table[ch]-=1
            if table[ch]<0:
                return False
        else:
            return False
        
     # Return true if all values are 0 else False  
      
    return len(set(table.values()))==1

print(anagrams('abcdef','fedcba'))