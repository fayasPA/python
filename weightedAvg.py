written_test = int(input("Enter mark scored by Student\nWritten Test="))
lab_exam = int(input("Lab Exams="))
assignment = int(input("Assignments="))
weighted_avg = ((written_test*70)+(lab_exam*20)+(assignment*10))/100
print("Grade of student is "+str(weighted_avg))