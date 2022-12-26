from random import sample

word_list=['father','break','country','green','aeroplane','india','creative','power','computer','python','website','koo','neuralink','english','vaccine','engine','advocate','ancient','beyond','campaign','champion','circle','citizen']

def update_words():#To Update List of Words...
    global word_list
    word_list=[x for x in input('Enter Any Five Words Separated By Comma : ').split(',')]

def word_puzzle():
    print("Hey! User Let's Start The Game, You Have To Arrange The Letters to Form a Valid Word...😜")
    input('Press Any Key To Start...')
    count,score=0,0
    for word in sample(word_list,5):

        count+=1
        print('\n%d. %s'%(count,''.join(sample(word,len(word)))))
        u_word=input('Enter Arranged Word : ')

        if u_word.lower()==word.lower():
            print('Correct')
            score+=1
            print('Current Score :',score)
        else:
            print('Wrong, Correct Arrangement is :',word)
            score-=1
            print('Current Score :',score)
    else:
        print('\nFinal Score :',score)
        if score==5:
            print('Great Effort')
        elif score==4:
            print('Good Efford')
        else:
            print('Practice Makes Man Perfect')

word_puzzle()
