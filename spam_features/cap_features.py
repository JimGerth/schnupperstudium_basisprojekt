from spam_features.length_feature import amount_words

def amount_cap_words(inputtext):
	splittext = inputtext.split(" ")
	total = 0
	for word in splittext:
		if (len(word) > 0):
			first = word[0]
			if first.isupper():
				total += 1
	return {'values' : [total], 'heads' : ['@Attribute amount_cap_words REAL']}

def cap_words_words_ratio(inputtext):
	total_cap_words = float(amount_cap_words(inputtext)['values'][0])
	total_words = float(amount_words(inputtext)['values'][0])
	return {'values' : [total_cap_words / total_words], 'heads' : ['@Attribute cap_word_ratio REAL']}