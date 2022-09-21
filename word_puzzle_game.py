from random import sample

def update_words():
    global word_list
    word_list=[x for x in input('Enter Any Five Words Separated By Comma : ').split(',')]


def puzzle():
    score=0
    print('Hey User! ,Let\'s Start The Puzzle....\n')
    for word in set(word_list):
        print('Arrange the Letters to Form a Valid Word :\n',''.join(sample(word,len(word))).upper(),sep='')
        user_input=input('Enter Arranged Word : ')
        if user_input.lower()==word.lower():
            score+=1
            print('\nCorrect\n')
        else:
            score-=1
            print('\nWrong\n')
    else:
        print('Net Score is',score)

word_list=['father','break','country','green','aeroplane']

#To Update Word List...
#update_words() 

puzzle()