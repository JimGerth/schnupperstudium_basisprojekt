from spam_features.length_feature import amount_words

def amount_exclamation_marks(inputtext):
    total = inputtext.count("!")
    return {'values': [total], 'heads': ['@Attribute amount_exclamation_marks REAL']}


def exclamation_mark_word_ratio(inputtext):
    total_words = float(amount_words(inputtext)['values'][0])
    total_exclamation_marks = float(amount_exclamation_marks(inputtext)['values'][0])
    return {'values': [total_exclamation_marks / total_words], 'heads': ['@Attribute exclamation_mark_word_ratio REAL']}