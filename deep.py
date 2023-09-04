ques = input('Какой ответ на главный вопрос жизни, вселенной и всего такого? ')

match ques.lower():
    case '42' | 'сорок два':
        print('Да')
    case _:
        print('Нет')
