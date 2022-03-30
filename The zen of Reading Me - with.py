import time

file = open('C:/Users/timo/Documents/GitHub/read-files/README.md', 'r')
line = True

while line:
    time.sleep(1)
    line = file.readline()
    print(line)