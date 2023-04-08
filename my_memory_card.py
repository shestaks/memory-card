#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QGroupBox, QWidget, QLabel, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout
from random import shuffle, randint


class Question():
    def __init__(self, question_text, right_answer, wrong1, wrong2, wrong3):
        self.question_text = question_text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_Question():
    result_box.hide()
    ansewer_group.show()
    button.setText('Отвечай')

def ask(q:Question):
    shuffle(ansewers)
    ansewers[0].setText(q.right_answer)
    ansewers[1].setText(q.wrong1)
    ansewers[2].setText(q.wrong2)
    ansewers[3].setText(q.wrong3)
    question.setText(q.question_text)
    result_text.setText(q.right_answer)
    show_Question()

def show_result():
    ansewer_group.hide()
    result_box.show()
    button.setText('Вперед к другому вопросу')

def show_Question():
    button_group.setExclusive(False)
    ansewer1.setChecked(False)
    ansewer2.setChecked(False)
    ansewer3.setChecked(False)
    ansewer4.setChecked(False)
    button_group.setExclusive(True)
    result_box.hide()
    ansewer_group.show()
    button.setText('Отвечай')

def start_programm():
    if button.text() == ('Отвечай'):
        check_answer()
    else: 
        next_question()

def check_answer():
    if ansewers[0].isChecked():
        result_text.setText('Правильно')
        main_win.score += 1
        show_result()
    else:
        result_text.setText('Не правильно')
        show_result()
    print("Всего вопросов:", main_win.total)
    print("Из них правильно", main_win.score)
    print("Рейтинг" , main_win.score / main_win.total * 100)


def next_question():
    main_win.total += 1
    cur_question = randint(0,len(questions_list)-1)
    q = questions_list [cur_question]
    ask(q)





questions_list = []
q1 = Question('Столица России', 'Москва', 'Англия', 'Пекин', 'Тверь')
q2 = Question('Из скольки цветов состоит российский флаг', 'три', 'один', 'четыре', 'пять')
q3 = Question('Сколько пальцев на одной руке', 'пять', 'четыре', 'шесть', 'десять')
q4 = Question('Цвет неба', 'Голубой', 'Алый', 'Пурпурный', 'Зеленый')
q5 = Question('Сколько цетов радуги', '5', '6', '7', '8')
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)
questions_list.append(q5)


app = QApplication([])
main_win = QWidget()

main_win.total = 0



main_win.score = 0



question = QLabel('Вопрос')
button = QPushButton('Ответить')
ansewer_group = QGroupBox('Варианты ответа')
vline = QVBoxLayout()
main_win.setLayout(vline)
main_win.resize(400,300)
main_win.setWindowTitle('Memory Card')
ansewer1 = QRadioButton('Вариант 1')
ansewer2 = QRadioButton('Вариант 2')
ansewer3 = QRadioButton('Вариант 3')
ansewer4 = QRadioButton('Вариант 4')

ansewers = [ansewer1, ansewer2, ansewer3, ansewer4]

button_group = QButtonGroup()
button_group.addButton(ansewer1)
button_group.addButton(ansewer2)
button_group.addButton(ansewer3)
button_group.addButton(ansewer4)



v1 = QVBoxLayout()
v1.addWidget(ansewer1)
v1.addWidget(ansewer2)
v2 = QVBoxLayout()
v2.addWidget(ansewer3)
v2.addWidget(ansewer4)
h = QHBoxLayout()
h.addLayout(v1)
h.addLayout(v2)
ansewer_group.setLayout(h)
result_box = QGroupBox('Результат')
result_text = QLabel('Правильно-Неправильно')
right_ansewer = QLabel('Тут будет верный ответ')
v3 = QVBoxLayout()
v3.addWidget(result_text)
v3.addWidget(right_ansewer)
result_box.setLayout(v3)


#ПРИВЯЗЫВАЕМ ГЛАВНЫЕ НАПРАВЛЯЮЩИЕ(ВОПРОС, ДВЕ ГРУППЫ ОТВЕТА)
vline.addWidget(question, alignment = Qt.AlignCenter)
vline.addWidget(ansewer_group)
vline.addWidget(result_box)
vline.addWidget(button)


#СПРЯТАТЬ ГРУППУ С ВАРИАНТАМИ ОТВЕТА
result_box.hide() 


button.clicked.connect(start_programm)

next_question()



main_win.show()
app.exec_()
