import random
q1 = {"4-2 is = how much":2, "7-2 = How much":5, "1-1 = How much":0 }
q2 = {"7+9-9 = how much":7,"1+24-9+4 = how much":20,"19-12+10 = how much":17}
q3 = {"8/2 x 8= How much": 32, "10/5 x 10 = How much": 20 ,"21/7 * 9 = How Much": 27,
 "(6+9)/3 x 5 is = How much": 25}
attemp1 = False
attemp2 = False
attemp3 = False
marks = 0
total = 1
def set1(i=0, attemp= False, marks = marks, total = 1):
    while attemp is False:
        if total <= 3:
            question = list(q1.keys())
            answers = list(q1.values())
            ans = input(question[i])
            correctans = answers[i]
            if int(ans) == int(correctans):
                marks = marks + 10
                attemp = True
                total = total + 1
                i  += 1
                if total <= 3:
                     set2(total, marks, i)
                else:
                    print(marks)
            else:
                i = i +1
                if total >= 3:
                    print("Your Tota Marks is {}".format(marks))
                    attemp = True
                    break
                else:
                    total = total + 1

def set2(total, marks ,i, attemp= False):
    if int(total) <= 3:
        while attemp is False:
            question = list(q2.keys())
            answers = list(q2.values())
            ans = input(question[i])
            correctans = answers[i]
            if int(ans) == int(correctans):
                marks = marks + 20
                attemp = True
                total = total + 1
                attemp = True
                set3(marks)
            else:
                if total <= 3:
                    total = total + 1
                    i += 1
                    set1(i, False , marks, total)
                    break
                else:
                    print(marks)                                    
    else:
        print(marks)
        attemp = True
def set3(marks):
    questions = list(q3.keys())
    i = 3
    question = questions[i]
    answer = q3[question]
    ask = input("{} ".format(question))
    if int(ask) == int(answer):
        marks += 30
        print("Your Total Score is {}".format(marks))
    else:
        questions.remove(question)
        i2 = random.choice(range(0, 2))
        q = questions[i2]
        a = q3[q]
        ask2 = input("{} ".format(q))
        if int(ask2) == int(a):
            marks += 15
            print("Your Total Score is {}".format(marks))
        else:
            print("Your Total Score is {}".format(marks))
set1()
