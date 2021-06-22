import random
questions = [{"4-2 is = how much":2, "7-2 = How much":5, "1-1 = How much":0 },
{"7+9-9 = how much":7,"1+24-9+4 = how much":20,"19-12+10 = how much":17},
{"8/2 x 8= How much": 32, "10/5 x 10 = How much": 20 ,"21/7 * 9 = How Much": 27, "(6+9)/3 x 5 is = How much": 25} ]
step = 1
marks = 0
i = 0
r = 0
while step <= int(len(questions)):
    
    q = questions[i]
    ask = list(q.keys())
    answer= list(q.values())
    main_question_asked = ask[r]
    main_answer = q[main_question_asked]
    submitted_value = input("{} ".format(main_question_asked))
    if int(submitted_value) == int(main_answer):
        if i == 0:
            marks += 10
            step += 1
            i += 1
        elif i == 1:
            marks += 20
            step += 1
            i += 1
        else:
            marks += 30
            step += 1
    else:
        if i >= 1:
            i -= 1
            r += 1
            step += 1
        else:
            i = 0
            r += 1
            step += 1
    
print("Your Total Score is {}".format(marks))