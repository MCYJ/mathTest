#NUMBER E

print('Let me know accuracy')
acc = int(input('Accuracy : '))
sum = 1
for i in range(1, acc+1):
    bot = 1
    for j in range(1,i+1):
        bot *= j
    sum += 1/bot
    print('STEP',i,' : ',sum)

print('E : ', sum)