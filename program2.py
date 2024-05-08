def decode_message(s: str, p: str) -> bool:
# Initialize two pointers, one for the secret message and one for the pattern
    s_index = 0
    p_index = 0


    #Iterate through the pattern
    while p_index < len(p):
        #If the current character in the pattern is a star symbol, skip over it
        if p[p_index] == '*':
                # skip over consecutive star symbols
            while p_index < len(p) and p[p_index] == '*':
                p_index += 1
            #If the pattern has been fully processed, then return True    
            if p_index == len(p):
                return True
            #Skip over characters in the secret message until a match is found   
            while s_index < len(s) and (p_index == len(p) or s[s_index]!= p[p_index]):
                s_index += 1
        # If the current character in the pattern is a question mark or matches the current character in the secret message, move to the next character        
        elif p[p_index] == '?' or p[p_index] == s[s_index]:
            s_index += 1
            p_index += 1
         # If the characters do not match, return False    
        else:
            return False

    # If the entire secret message has been processed, return True
    return s_index == len(s)
        

# write your code here
  