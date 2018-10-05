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

def amount_cap_lock_words(inputtext):
	splittext = inputtext.split(" ")
	total_cap_lock_words = 0
	for word in splittext:
		total_chars = 0
		total_caps = 0
		for letter in word:
			if letter.isalpha():
				total_chars += 1
				if letter.isupper():
					total_caps += 1
		if total_chars == total_caps:
			total_cap_lock_words += 1
	return {'values': [total_cap_lock_words], 'heads': ['@Attribute amount_cap_lock_words REAL']}

def cap_words_words_ratio(inputtext):
	total_cap_words = float(amount_cap_words(inputtext)['values'][0])
	total_words = float(amount_words(inputtext)['values'][0])
	return {'values' : [total_cap_words / total_words], 'heads' : ['@Attribute cap_words_words_ratio REAL']}

def cap_lock_words_words_ratio(inputtext):
	total_cap_lock_words = float(amount_cap_lock_words(inputtext)['values'][0])
	total_words = float(amount_words(inputtext)['values'][0])
	return {'values' : [total_cap_lock_words / total_words], 'heads' : ['@Attribute cap_lock_words_words_ratio REAL']}

print(amount_cap_lock_words("hello TH.IS is A TEST.")['values'][0])