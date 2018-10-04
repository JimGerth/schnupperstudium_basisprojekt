def amount_words(inputtext):
    return {'values': [len(inputtext.split(" "))], 'heads': ['@Attribute amount_words REAL']}

def amount_positive_words(inputtext):
    total_positive_words = 0
    with open("/Users/jim/Desktop/schnup_nlp/schnupperstudium_basisprojekt/opinion-lexicon-English/positive-words.txt", "r") as f:
        for line in f:
            for word in inputtext.split(" "):
                if line == word:
                    total_positive_words += 1
    return {'values': [total_positive_words], 'heads': ['@Attribute amount_positive_words REAL']}

def amount_negative_words(inputtext):
    total_negative_words = 0
    with open("/Users/jim/Desktop/schnup_nlp/schnupperstudium_basisprojekt/opinion-lexicon-English/negative-words.txt", "r") as f:
        for line in f:
            for word in inputtext.split(" "):
                if line == word:
                    total_negative_words += 1
    return {'values': [total_negative_words], 'heads': ['@Attribute amount_negative_words REAL']}

def ratio_positive_words_words(inputtext):
    return {'values': [amount_positive_words(inputtext)['values'][0] / amount_words(inputtext)['values'][0]], 'heads': ['@Attribute ratio_positive_words_words REAL']}

def ratio_negative_words_words(inputtext):
    return {'values': [amount_negative_words(inputtext)['values'][0] / amount_words(inputtext)['values'][0]], 'heads': ['@Attribute ratio_negative_words_words REAL']}