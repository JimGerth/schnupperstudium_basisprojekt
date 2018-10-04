def amount_words(inputtext):
    total = len(inputtext.split(" "))
    return {'values': [total], 'heads': ['@Attribute amount_words REAL']}

def amount_sentences(inputtext):
    split_text_by_dots = inputtext.split(". ")
    '''for i in range(len(split_text_by_dots)):
        split_text_by_dots[i] = split_text_by_dots[i].split("! ")
        for j in range(len(split_text_by_dots[i])):
            split_text_by_dots[i][j] = split_text_by_dots[i][j].split("? ")'''
    total_sentences = len(split_text_by_dots)
    '''for i in split_text_by_dots:
        for j in split_text_by_dots[i]:
            total_sentences += split_text_by_dots[i][j]'''
    return {'values': [total_sentences], 'heads': ['@Attribute amount_sentences REAL']}

def word_sentence_ratio(inputtext):
    total_words = amount_words(inputtext)['values'][0]
    total_sentences = amount_sentences(inputtext)['values'][0]
    return {'values': [total_words / total_sentences], 'heads': ['@Attribute word_sentence_ratio REAL']}