ofc = open("update.txt", "w")
ofc.close()

with open('update.txt', 'w+') as f:
    f.write('readme')