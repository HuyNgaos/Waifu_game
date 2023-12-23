import random
correct_num = 0
ngan_hang_de_hoa = {
    1:'Q: What are the 4 basic IMF in decending power\n',
    2:'Q: Name the 4 quantum number of the last electron of Potassium\n',
    3:'Q: From left to right, what is the trend of atomic radius\n',
    4:'Q: What is the bonding angle of tetrahedral molecues\n',
    5:'Q: What is the coordination number of [Cu(NH3)4]2+\n',
    6:'Q: Name the ideal gas formula',
    7:'Q: Can C6H12(cycohexane) dissolve in CH3OH(methanol)\n'
}
ngan_hang_dap_an_hoa = {
    1:'ion-dipole,hydrogen-bond,dipole-dipole,london-dispersion',
    2:'n=4,l=0,ml=0,ms=1/2',
    3:'decrease',
    4: '109.5',
    5: '4',
    6:'pv=ntr',
    7:'no'
}
ngan_hang_de_toan = {
    1: 'Q: If 2x - 5 = 5x + 4, then x2 + x =\n',
    2: 'Q: For x in (pi/2, 2pi), sin(x)=sqrt(2)/2, then x= (pi=3.14)\n',
    3: 'Q: For x < 3 Solve x^2 - 7x + 10 = 0\n',
    4: 'Q: If you deposit $100 into a savings account which earns a 5% yearly interest rate, how much is in your account after two years?\n',
    5: 'Q: A community baseball stadium has 10 seats in the first row, 13 seats in the second row, 16 seats in the third row, and so on. There are 11 rows in all. What is the seating capacity of the stadium?\n'
}
ngan_hang_dap_an_toan = {
    1: '6',
    2: '2.355',
    3: '2',
    4: '110.25',
    5: '275'
}
class quiz_libary():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def fusion_question():
        p = random.randint(1,2)
        n = random.randint(1,13)
        T = random.randint(179, 421)
        R = 0.0821 #L atm / mol K 
        print('3 numbers after decimal point\nR = 0.0821 L*atm/mol*K\n')
        answer = input(f'What is the volume in liters of {n} mol of a gas at {p}atm and {T}K?\nYour answer: ')
        correct_answer = (n*R*T)/p
        correct_answer = round(correct_answer, 3)
        global correct_num
        if answer == str(correct_answer):
            print('Correct')
            correct_num += 1
        else:
            print('Wrong', '\nCorrect answer is', correct_answer)
        
class generate(quiz_libary):
    def generate_question_chem():
        chem_q = random.randint(1,7)
        chem_question = ngan_hang_de_hoa[chem_q]
        chem_answer = ngan_hang_dap_an_hoa[chem_q]
        quiz_chem = quiz_libary(chem_question, chem_answer)
        return quiz_chem
    def generate_question_math():
        math_q = random.randint(1,5)
        math_question = ngan_hang_de_toan[math_q]
        math_answer = ngan_hang_dap_an_toan[math_q]
        quiz_math = quiz_libary(math_question, math_answer)
        return quiz_math
class check(quiz_libary):
    def check_answer_chem(quiz, input_ans):
        if quiz.answer == input_ans:
            return True
        else:
            return False
        
class ask_and_evaluate(quiz_libary):
    def ask_question_chem(quiz_chem):
        print(quiz_chem.question)
        input_ans = input('Your answer: ')
        return input_ans
    def ask_question_math(quiz_math):
        print(quiz_math.question)
        input_ans = input('Your answer: ')
        return input_ans
    def out_put(quiz, input_ans):
        global correct_num
        if check.check_answer_chem(quiz, input_ans):
            print('Correct')
            correct_num += 1
        else:
            print('Wrong', '\nCorrect answer is', quiz.answer)

class cum_to_ask(quiz_libary):
    def cum_to_ask():
        print('no space, use (,) to seperate, use (-) for space, only lowercase')
        quiz_chem = generate.generate_question_chem()
        quiz_math = generate.generate_question_math()
        input_ans_chem = ask_and_evaluate.ask_question_chem(quiz_chem)
        ask_and_evaluate.out_put(quiz_chem, input_ans_chem)
        input_ans_math = ask_and_evaluate.ask_question_math(quiz_math)
        ask_and_evaluate.out_put(quiz_math, input_ans_math)
        global correct_num
        quiz_libary.fusion_question()
        print(f'You have {correct_num} correct answers')
        if correct_num >= 3:
            print('Laura passed the test all thanks to you.\nEveryone is pleased by your performance.')
        elif correct_num == 2:
            print('Laura barely passed the test. At least, she still have a fighting chance.\nYou still can do better.')
        else:
            print('Laura failed. She will be sent to the gulag.\nEveryone is dissappointed at your performance.')
        correct_num = 0