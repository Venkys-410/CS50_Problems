temps = {'t1': -30,'t2': -20,'t3': -10,'t4': 0,'t5':25}

'''convert farhenheit to celcius general method'''
#Here we converted farenheit into celcius by applying lambda function to each of the values in dict using map()
#the below celciuslist will contain the converted temps
celciuslist = list(map(lambda t : round((t-32)*(5/9),2),temps.values()))

#here we are zipping the converted temps with dict keys
temptuplles= zip(temps.keys(),celciuslist)

#print(temptuplles)

#finally we are converting the zipped object to dictionary
print(dict(temptuplles))

''' Adove problem with dictionary comprehension'''

celciusdict = {k: round((v-32)*(5/9),2)  for k,v in temps.items()}

print(celciusdict)