my_dict={}

person={
    'nume':'Ion' ,
    'prenume':'Maria' ,
    'inaltime':'1.65'
    }

    



print(person['nume'])
print(person['prenume'])
print(person['inaltime'])

print(person)
print(person.keys())
print(person.values())

x=float(person['inaltime'])
person['inaltime']=x+0.1
print(person)
