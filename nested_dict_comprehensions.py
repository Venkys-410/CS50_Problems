nested_dict = {'first':{'a':1}, 'second':{'b':2},'third':{'d':4}}

#Problem: Convert the numeric values in inner dict into floats

''' Regular Approach'''

for outer_key,outer_value in nested_dict.items():
    for inner_key,inner_value in outer_value.items():
        outer_value[inner_key] = float(inner_value)
       #outer_value.update({inner_key:float(inner_value)})
    nested_dict[outer_key]=outer_value
   #nested_dict.update({outer_key:outer_value})

print(nested_dict)

nested_dict2 = {'first':{'a':1}, 'second':{'b':2},'third':{'d':4}}

''' Dictionary Comprehension'''
converted_dict = {outer_k:{inner_k: float(inner_v) for inner_k,inner_v in outer_v.items()}for outer_k,outer_v in nested_dict2.items()}

print(converted_dict)