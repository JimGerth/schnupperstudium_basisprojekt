from spam_features.length_feature import amount_words

def amount_question_marks(inputtext):
    return {'values': [len(inputtext.split("?"))], 'heads': ['@Attribute amount_question_marks REAL']}

def question_mark_word_ratio(inputtext):
    total_words = float(amount_words(inputtext)['values'][0])
    total_question_marks = float(amount_question_marks(inputtext)['values'][0])
    return {'values': [total_question_marks / total_words], 'heads': ['@Attribute exclamation_mark_word_ratio REAL']}