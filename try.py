import anything
print('Welcome to Zealarax Clinic!\nCan I know Your Name?')  
userName=input('')
print(userName,', Can I know at least two of the symptoms you get, so as to know what your disease is?')
symptoms1=input()
symptoms2=input()
symptoms3=input()
symptoms_of_diseases=anything.diseaseSymptoms
symptoms_list=[symptoms1,symptoms2,symptoms3]

correlation_with_HA=[x for x in symptoms_of_diseases['heart attack'] if x in symptoms_list and x in symptoms_of_diseases['heart attack'] ]
print('correlation_with_HA: ',correlation_with_HA)

correlation_with_stroke=[x for x in symptoms_of_diseases['stroke'] if x in symptoms_list and x in symptoms_of_diseases['stroke'] ]
print('correlation_with_stroke: ',correlation_with_stroke)

if (len(correlation_with_HA)>=2):
    print('sorry',userName,', You\'re most likely to have an Heart Attack, please see our specialist in the Next Office. ')
elif (len(correlation_with_stroke)>=2):
    print('sorry',userName,', You\'re most likely to have a Stroke, please see our specialist in the Next Office. ')
else:
    print('sorry',userName,', We\'ll need to run some tests to be sure of what disease your\'re having. \n please call the next patient on your way out.')
