def word_break(s:str, words:list[str]) -> int:
    if s == "":
        return [""]
    
    sentences = []
    for word in words:
        if s.startswith(word):
            suffix = s[len(words):]
            suffix_sentences = word_break(suffix,words)
            for sentence in suffix_sentences:
                if sentence:
                    sentences.append(word + " " + sentence)
                else:
                    sentence.append(word)
    return sentences
                    