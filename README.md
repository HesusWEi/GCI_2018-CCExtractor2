# GCI_2018-CCExtractor2
print('This is the first question:')
i=0
while i < 10:
    i += 1
    print('GCI is great')
    if i < 10:
	      continue
print('This is the second question:')
name=input('Your name?')
print('Hello',name,',please to meet you!')
b=list(reversed(name))
print('hello!',name,'please to meet you,do you know your backwards name is',b,'?')

RUN:
This is the first question:
GCI is great
GCI is great
GCI is great
GCI is great
GCI is great
GCI is great
GCI is great
GCI is great
GCI is great
GCI is great
This is the second question:
Your name?jack
Hello jack ,please to meet you!
hello! jack please to meet you,do you know your backwards name is ['k', 'c', 'a', 'j'] ?

