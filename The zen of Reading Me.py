import time

with open('C:/Users/timo/Documents/GitHub/read-files/README.md', 'r') as file:
    for line in file:
        time.sleep(1)
        print(line)