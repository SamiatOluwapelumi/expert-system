tuple1=('orange','apple','banana','mango','grape')
x=list(tuple1)
emptytuple=[]
for fruits in x:
    emptytuple.append(fruits)
    if 'n' in fruits:
     print(fruits)
# print(tuple(emptytuple))
    
