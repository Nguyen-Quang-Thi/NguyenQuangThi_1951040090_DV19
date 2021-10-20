import random

class STUDENT():

    def __init__(self,  id=None , score=None , credit=None):
        if score is not None:
            self.score = score
        else:
            self.score = round((random.uniform(0, 4)),1)
        
        if credit is not None:
            self.credit = credit
        else:
            self.credit = random.randint(0, 500)
        
        if id is not None:
            self.id = id
        else:
            self.id = "SV_{}".format(random.randint(0, 9999))
    
    def result(self):
        if self.score >= 3.8 and self.score <= 4:
            return "A+"
        elif self.score >= 3.3 and self.score <= 3.7:
            return "A"
        elif self.score >= 3 and self.score <= 3.2:
            return "B+"
        elif self.score >= 2.6 and self.score <= 2.9:
            return "B"
        elif self.score >= 1.8 and self.score <= 2.5:
            return "C"
        elif self.score < 1.8:
            return "D"
    
    def graduate(self):
        if self.result != 'D'  and self.credit >= 250 and self.score >= 1.8:
            return True
        else: return False

def sort(x: STUDENT):
    return x.score

def check_student(n):
   
    list_graduate = []
    list_student = []
    for i in range(int(n)):
        s = STUDENT()
        list_student.append(s)
        if s.graduate():
            list_graduate.append(s)
    count = 0
    list_student.sort(key=sort, reverse=True)
    for student in list_student:
        if student.graduate() == True:
            count = count +1
        print(f'{student.id}: {student.score}, result: {student.result()}, credit: {student.credit}, graduate: {student.graduate()}')
    print(f'Tổng số sinh viên tốt nghiệp : {count}')
    print(f'MSSV có điểm cao nhất là {list_student[0].id} với số điểm là {list_student[0].score}')
    
if __name__=='__main__':
    i = input(" Nhap so hoc sinh: ")
    check_student(i)


