def levenshtein(seq1: str, seq2: str) -> int:
    assert isinstance(seq1, str) and isinstance(seq2, str), 'Some sequence is not a string'
    oneago = None
    thisrow = [i for i in range(1, len(seq2) + 1)] + [0]
    for x in range(len(seq1)):
        oneago, thisrow = thisrow, [0] * len(seq2) + [x + 1]
        for y in range(len(seq2)):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)
    
    return thisrow[len(seq2) - 1]

if __name__ == '__main__':    
    str1 = "54" 
    str2 = 56 
    distance = levenshtein(str1,str2) 
    print(distance) 
