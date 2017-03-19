# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:30:22 2017

@author: Gayatri
"""
#https://github.com/atbaker/wikipedia-question-generator/blob/master/wikitrivia/article.py
from textblob import TextBlob
import re
b=TextBlob('Bob likes red apples.')
print(b.parse())
for sen in b.sentences:
#    print (sen.tags)
    tag_map = {word.lower(): tag for word, tag in sen.tags}
    replace_nouns=[]
    for word, tag in sen.tags:
            #print(word,tag)
            # For now, only blank out non-proper nouns that don't appear in the article title
            if tag == 'NN' :
                #print('went here atleast')
                # Is it in a noun phrase? If so, blank out the last two words in that phrase
                for phrase in sen.noun_phrases:
                    #print('lallalalala',phrase)
#                    if phrase[0] == '\'':
#                        # If it starts with an apostrophe, ignore it
#                        # (this is a weird error that should probably
#                        # be handled elsewhere)
#                        break
                    #print('hoooooooooooooo',word,phrase)
                    if word in phrase:
                        #print('here')
                        # Blank out the last two words in this phrase
                        [replace_nouns.append(phrase_word) for phrase_word in phrase.split()[-2:]]
                        break
                        #print(replace_nouns)
                replace_phrase = ' '.join(replace_nouns)
                blanks_phrase = ('__________ ' * len(replace_nouns)).strip()

                expression = re.compile(re.escape(replace_phrase), re.IGNORECASE)
                sentence = expression.sub(blanks_phrase, str(sen), count=1)
                print('hohohohohohoho',sentence)
