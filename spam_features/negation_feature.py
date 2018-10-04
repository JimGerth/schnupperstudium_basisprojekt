from spam_features.length_feature import amount_sentences

def negation_sentence_ratio(inputtext):
    total_negations = len(inputtext.split("'nt "))
    total_sentences = amount_sentences(inputtext)['values'][0]
    return {'values': [total_negations / total_sentences], 'heads': ['@Attribute negation_sentence_ratio REAL']}