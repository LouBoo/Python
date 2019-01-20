Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f = 7.2332; str(f)[::-1].find('.')
4
>>> f = 76.543; str(f)[::-1].find('.')
3
>>> f = 76.543; str(f)[::1].find('.')
2
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> my_text = 'What you dont know wont hurt you'
my_text = my_text.replace('know', 'owe')
print (my_text)
SyntaxError: multiple statements found while compiling a single statement
>>> my_text = 'What you dont know wont hurt you'my_text = 'What you dont know wont hurt you'
SyntaxError: invalid syntax
>>> my_text = 'What you dont know wont hurt you'my_text = 'What you dont know wont hurt you'
SyntaxError: invalid syntax
>>> my_text = 'What you dont know wont hurt you'
>>> my_text = my_text.replace('know', 'owe')
>>> print (my_text)
What you dont owe wont hurt you
>>> my_text = "What you don't know won't hurt you"
>>> my_text = my_text.replace('know', 'owe')
>>> print (my_text)
What you don't owe won't hurt you
>>> 
