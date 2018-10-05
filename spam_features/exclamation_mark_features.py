def amount_exclamation_marks(inputtext):
    total = inputtext.count("!")
    return {'values': [total], 'heads': ['@Attribute amount_exclamation_marks REAL']}


def exclamation_mark_char_ratio(inputtext):
    total_chars = len(inputtext)
    total_exclamation_marks = float(amount_exclamation_marks(inputtext)['values'][0])
    return {'values': [total_exclamation_marks / total_chars], 'heads': ['@Attribute exclamation_mark_word_ratio REAL']}