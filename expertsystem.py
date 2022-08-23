import symptoms
diseaseSymptoms={
'heart attack':['lightheadedness','nausea','extreme fatigue', 'fainting','dizziness'],
'stroke':['face dropping','arm weakness','speech difficulty']
}
disease=input('input disese: ')
list=[]
for i in diseaseSymptoms.keys():
    if i == disease:
        for a in diseaseSymptoms[i]:
         print("-",(a))




# for x,y in diseaseSymptoms.items():
# #   if disease== 'heart attack':
#         print(x)
#         print(y) 
#       if disease== i[0]:
#         print(a['heart attack'])

# # print('Welcome to Zealarax Clinic!\nCan I know Your Name?')  
# userName=input('')
# print(userName,', Can I know at least two of the symptoms you get, so as to know what your disease is?')

# symptoms1=input()
# symptoms2=input()
# symptoms3=input()
# heartAttack=symptoms.HAsymptoms
# stroke=symptoms.symotomsOfStroke
# if (symptoms1 in heartAttack ) and (symptoms2 in heartAttack) or (symptoms3  in heartAttack):
#     print('sorry',userName,', You\'re most likely to have an Heart Attack, please see our specialist in the Next Office. ')
# elif (symptoms1 in heartAttack) or (symptoms2 in heartAttack) and (symptoms3  in heartAttack):
#     print('sorry',userName,', You\'re most likely to have an Heart Attack, please see our specialist in the Next Office. ')
# elif (symptoms1 in heartAttack) and (symptoms3 in heartAttack) or (symptoms2  in heartAttack):
#     print('sorry',userName,', You\'re most likely to have an Heart Attack, please see our specialist in the Next Office. ')

# elif (symptoms1 in stroke) and (symptoms2 in stroke) or (symptoms3  in stroke):
#     print('sorry',userName,', You\'re most likely to have a Stroke, please see our specialist in the Next Office. ')
# elif (symptoms1 in stroke) or (symptoms2 in stroke) and (symptoms3  in stroke):
#     print('sorry',userName,', You\'re most likely to have a Stroke, please see our specialist in the Next Office. ')
# elif (symptoms1 in stroke) and (symptoms3 in stroke) or (symptoms2  in stroke):
#     print('sorry',userName,', You\'re most likely to have a Stroke, please see our specialist in the Next Office. ')

# else:
#     print('sorry',userName,', We\'ll need to run some tests to be sure of what disease your\'re having. \n please call the next patient on your way out.')

