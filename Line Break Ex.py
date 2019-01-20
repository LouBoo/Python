Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str1 = "How are you" +/
SyntaxError: invalid syntax
>>>  str1 = "How are you" +\
	
SyntaxError: unexpected indent
>>> str1 = "How are you?" +\
       "I am OK."
>>> print (str1)
How are you?I am OK.
>>> str1 = "How are you?" +\
       " I am OK."
>>> print (str1)
How are you? I am OK.
>>> 
How are you? I am OK.
SyntaxError: invalid syntax
>>> 
>>> 
>>> lst1 = ["abc", "edf"]
>>> lst2 = [33, 44, "ght"]
>>> print (lst1 + lst2)
['abc', 'edf', 33, 44, 'ght']
>>> comList = (lst1 + lst2)
>>> print (comList)
['abc', 'edf', 33, 44, 'ght']
>>> print ("a test for \"double\" quotation.")
a test for "double" quotation.
>>> print ("a test for double quotation. (\").")
a test for double quotation. (").
>>> print ("a test for double quotation. (").")
SyntaxError: EOL while scanning string literal
>>> print ("a test for double quotation. (\n).")
a test for double quotation. (
).
>>> print ("a test for double quotation. (\t).")
a test for double quotation. (	).
>>> print ("a test for double quotation. (n).")
a test for double quotation. (n).
>>> print ("a test for double quotation. (t).")
a test for double quotation. (t).
>>> 
