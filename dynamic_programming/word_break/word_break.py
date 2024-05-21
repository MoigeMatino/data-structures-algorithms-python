def word_break(s, words):
    memo = {}
    sentences = _word_break(s, words, memo)
    return sentences
    
def _word_break(s, words, memo):
    if s in memo:
        return memo[s]
        
    if s == "":
        return [""]
        
    sentences = [] 
    for word in words:
        if s.startswith(word):
            suffix = s[len(word):]
            suffix_sentences = _word_break(suffix, words, memo)
            for sentence in suffix_sentences:
                if sentence:
                    sentences.append(word + " " + sentence)
                else:
                    sentences.append(word)
    memo[s] = sentences
    return memo[s]
