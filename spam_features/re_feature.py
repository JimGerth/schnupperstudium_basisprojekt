def is_response(inputtext):
    return {'values': [inputtext.count("Re: ")], 'heads': ['@Attribute is_response REAL']}