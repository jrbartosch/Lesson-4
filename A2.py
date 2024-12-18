amount = int((input('Please Enter Amount for Withdrawal:')))
note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//20
note_4 = (((amount%100)%50)%20)//10
note_5 = ((((amount%100)%50)%20)%10)//5
note_6 = (((((amount%100)%50)%20)%10)%5)//1
print ('Notes of $100: ', note_1)
print ('Notes of $50: ', note_2)
print ('Notes of $20: ', note_3)
print ('Notes of $10: ', note_4)
print ('Notes of $5: ', note_5)
print ('Notes of $1: ', note_6)