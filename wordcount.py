import sys
count = {}
with open('input.txt', 'r') as f:
    lines = [line.rstrip() for line in f]  # read lines from input

for line in lines:
    words = line.split()  # split the line to get words
    for word in words:  # for each word
        if word in count:  # if the word already present
            count[word] += 1  # increase count
        else:
            count[word] = 1  # else insert the word


sys.stdout = open('outputfile', 'w')
print('Word_Count:')  # print word counts
print(line)  # print each line
for key, value in count.items():
    print(f'{key}: {value}')