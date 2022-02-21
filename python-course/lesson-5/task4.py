EN_FILENAME = 'task4-en'
RU_FILENAME = 'task4-ru'
NUM_TRANSLATE = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
WORD_SEPARATE = ' — '

ru_file = open(RU_FILENAME, 'w+')

with open('task4-en', 'r') as f:
    lines = f.readlines()
    for line in lines:
        text, num = line.rstrip().split(WORD_SEPARATE)
        ru_file.write(f'{NUM_TRANSLATE[text.lower()].capitalize()} {WORD_SEPARATE} {num}\n')
    ru_file.close()
