#!/usr/bin/python
#filename:DB_interface.py

######To manage the database for morph-analyser########

import codecs
import os
import re
import sys

from morph_examples import examples
	
def readAllExamples():
	out=codecs.open('../output.txt',mode='w',encoding='utf-8')
	sort_list=examples.keys()
	sort_list.sort()
	for ex in sort_list:
	  out.write(ex+'\t')
	  for i in examples[ex]:
		out.write(i+'  ')
	  out.write('\n')
	out.close()
	
def findMorph(word):
	suffixes=[]
	analysed_word=''
	if word=='':
		return [word,'']
	for w in examples:
	   if re.match('.*'+word+'$',w):
		suffix=examples[w][1]
		index=(len(w)-len(word))
	   	word=examples[w][0][index:]
	   	if suffix=='-':
	   		return [word,'']
	   	else:
	   		return [word,suffix]
	pre_part=''
	if(len(word)>1):
	   	pre_part=pre_part+word[0]
	   	word=word[1:]
	   	morph_list=findMorph(word)
	   	return [pre_part+morph_list[0]]+morph_list[1:]
	else:
		return [word,'']	
	out.close()

def morphAnal(root):
	wrd=''
	analysed_word=[]
	while(root!=wrd):
		wrd=root
		temp=findMorph(wrd)
		root=temp[0]
		analysed_word=[temp[1]]+analysed_word
	return [root]+analysed_word



	
def dbEntry():
	inp=codecs.open('../input.txt',encoding='utf-8',mode='w')
	inp.write('*'*25+'Enter the inputs here'+'*'*25+'\n(Format:<full word><tab><root><space><suffix>)\n')
	inp.close()
	os.system('gedit ../input.txt')
	raw_input('Enter the examples in the text file, and save it.')
	inp=codecs.open('../input.txt',encoding='utf-8',mode='r')
	db=codecs.open('morph_examples.py',mode='a',encoding='utf-8')
	from uniCodeMap import uniCode
	inp.readline()
	inp.readline()
	ln=inp.readline()
	while(ln!=''):
	    word=ln.split('\t')[0]
	    new_answer = ln.split('\t')[1][:-1].split(' ')
	    new_answer = [new_answer[0]] + [''] + new_answer[1:]
	    analysed_word=morphAnal(word)
	    if(new_answer == analysed_word):
		print "This entry("+word+") would create redundancy"
		ln=inp.readline()
		pass
	    else:
		new_ln='examples[u\''
		for char in ln:
			if char in uniCode:
				new_ln=new_ln+uniCode[char]
			elif char=='\t':
				new_ln=new_ln+"\']=[u\'"
			elif char==' ':
				new_ln=new_ln+'\',u\''
			elif char==u'\u200d':
				new_ln=new_ln+'\\u200d'
			elif char=='\n':
				pass
			else:
				new_ln=new_ln+char			##Error message

		new_ln=new_ln+'\']\n'				
		db.write(new_ln)
		ln=inp.readline()
	inp.close()
	db.close()
	
	
		

def normal_exec():
	choice=0
	print ("What do you want?\n\t1.View the whole database\n\t2.Check the morph-segmentation for an entry\n\t3.Add examples to DB\n\t4.Exit the program\n")
	  
	while choice!=4:
	  choice=input("Enter choice: ")
	  if choice==1:
		readAllExamples()	
		os.system('gedit ../output.txt')
	  elif choice==2:
		raw_input('Enter the word(with suffixes) in the file and save it.')
		os.system('gedit ../input.txt')
		word=codecs.open('../input.txt',mode='r',encoding='utf-8').read()
		actual_word=word[:-1]
		analysed_word=morphAnal(actual_word)
		out=codecs.open('../output.txt',mode='w',encoding='utf-8')
		#print actual_word,'\t',analysed_word
		out.write(actual_word+'\t')
		for i in analysed_word[:]:
			out.write(i+' ')
		out.write('\n')
		out.close()
		os.system('gedit ../output.txt')
	  elif choice==3:
	  	dbEntry()
	  elif choice==4:
		pass
	  else:
		print "Hey! What does that mean?!" 
		print ("Select a number from below\n\t1.View the whole database\n\t2.Check the database for an entry\n\t3.Add examples to DB\n\t4.Exit the program\n")
	
		
if __name__ == "__main__":
	if(len(sys.argv)>1):
		choice = sys.argv[1]
		if choice=='1':
			readAllExamples()	
			os.system('gedit ../output.txt')
		elif choice=='2':
			raw_input('Enter the word(with suffixes) in the file and save it.')
			os.system('gedit ../input.txt')
			word=codecs.open('../input.txt',mode='r',encoding='utf-8').read()
			actual_word=word[:-1]
			analysed_word=morphAnal(actual_word)
			out=codecs.open('../output.txt',mode='w',encoding='utf-8')
			#print actual_word,'\t',analysed_word
			out.write(actual_word+'\t')
			for i in analysed_word[:]:
				out.write(i+' ')
			out.write('\n')
			out.close()
			os.system('gedit ../output.txt')
		elif choice=='3':
		  	dbEntry()
		else:
			print "Hey! What does that mean?!" 
	else:
		normal_exec()

