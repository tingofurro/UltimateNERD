from segtok import tokenizer

sentence = "Video of the incident resurfaced Wednesday after Affleck joined a chorus of others in denouncing the actions of disgraced movie mogul Harvey Weinstein, who stands accused of numerous incidents of sexual harassment and three incidents of rape. "

words = tokenizer.word_tokenizer(sentence)
capitalized = False
start = -1

groups = []
for i, w in enumerate(words):
    if len(w) > 0:
        if w[0].upper() == w[0]:
            if capitalized:
                pass
            else:
                start = i
                capitalized = True
        else:
            if capitalized:
                groups.append((start, i-1))
                capitalized = False
    
for start, end in groups:
    print " ".join([words[i] for i in range(start, end+1)])