import csv

def amount_words(inputtext):
    return {'values': [len(inputtext.split(" "))], 'heads': ['@Attribute amount_words REAL']}

def amount_positive_words(inputtext):
    total_positive_words = 0
    with open("/informatik2/students/home/schnup09/Desktop/schnupperstudium_basisprojekt/opinion-lexicon-English/positive-words.txt", "r") as f:
        for line in f:
            for word in inputtext.split(" "):
                if line == word + "\n":
                    total_positive_words += 1
    return {'values': [total_positive_words], 'heads': ['@Attribute amount_positive_words REAL']}

def amount_negative_words(inputtext):
    total_negative_words = 0
    with open("/informatik2/students/home/schnup09/Desktop/schnupperstudium_basisprojekt/opinion-lexicon-English/negative-words.txt", "r") as f:
        for line in f:
            for word in inputtext.split(" "):
                if line == word + "\n":
                    total_negative_words += 1
    return {'values': [total_negative_words], 'heads': ['@Attribute amount_negative_words REAL']}

def amount_bad_words(inputtext):
    total_negative_words = 0
    words = list()
    with open("/informatik2/students/home/schnup09/Desktop/schnupperstudium_basisprojekt/bad_word_list.csv", "r") as f:
        writer = csv.writer(f, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONE, escapechar='\\')
        # TODO
        for line in f:
            for word in inputtext.split(" "):
                if line == word + "\n":
                    total_negative_words += 1
    return {'values': [total_negative_words], 'heads': ['@Attribute amount_bad_words REAL']}

def ratio_positive_words_words(inputtext):
    return {'values': [amount_positive_words(inputtext)['values'][0] / amount_words(inputtext)['values'][0]], 'heads': ['@Attribute ratio_positive_words_words REAL']}

def ratio_negative_words_words(inputtext):
    return {'values': [amount_negative_words(inputtext)['values'][0] / amount_words(inputtext)['values'][0]], 'heads': ['@Attribute ratio_negative_words_words REAL']}

def ratio_bad_words_words(inputtext):
    return {'values': [amount_bad_words(inputtext)['values'][0] / amount_words(inputtext)['values'][0]], 'heads': ['@Attribute ratio_bad_words_words REAL']}