#!/usr/bin/python
#filename:DB_interface.py

#import DB_interface
from DB_interface import *
from uniCodeMap import uniCode 

import re
import codecs

text = codecs.open('input.txt',mode='r',encoding='utf-8').read()
#words = re.split("[\s.?!,:;]",text)

out=codecs.open('output.txt',mode='w',encoding='utf-8')
word = ""
for letter in text:
	#print letter
	if letter in uniCode:
		word = word + letter
	else:
		print (word+"---->")
		if word != "":
			analysed_word = morphAnal(word)
			# for anal_word in analysed_word:
			# 	print (anal_word)
			# 	out.write(anal_word+' ')
			out.write(analysed_word[0])
			word = ""
			out.write(letter)
		else:
			print (letter)
			out.write(letter)
out.close()
