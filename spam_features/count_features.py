def amount_of_3_contiguous_spaces(inputtext):
    return {'values': [inputtext.count("     ")], 'heads': ['@Attribute amount_of_3_contiguous_spaces REAL']}

def amount_dollar_signs(inputtext):
    return {'values': [inputtext.count("$")], 'heads': ['@Attribute amount_dollar_signs REAL']}

def amount_percent_sign(inputtext):
    return {'values': [inputtext.count("%")], 'heads': ['@Attribute amount_percent_sign REAL']}

def amount_money(inputtext):
    return {'values': [inputtext.lower().count("money") + inputtext.lower().count("make money")], 'heads': ['@Attribute amount_money REAL']}

def amount_links(inputtext):
    return {'values': [inputtext.count("http://") + inputtext.count("https://")], 'heads': ['@Attribute amount_links REAL']}

def amount_question_marks(inputtext):
    return {'values': [len(inputtext.split("?"))], 'heads': ['@Attribute amount_question_marks REAL']}

def amount_responses(inputtext):
    return {'values': [inputtext.count("Re: ") + inputtext.count("re: ")], 'heads': ['@Attribute is_response REAL']}
