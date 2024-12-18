print ('Enter Marks Obtained in 4 Subjects:')
math = int(input('Enter Marks Obtained in Math: '))
english = int(input('Enter Marks Obtained in English: '))
science = int(input('Enter Marks Obtained in Science: '))
history = int(input('Enter Marks Obtained in History: '))
sum = math + english + science + history
perc = (sum/400) * 100
print (perc)