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