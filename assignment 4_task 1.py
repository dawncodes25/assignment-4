
try:
    file1 = open('sample.txt', 'r')
    print('Reading file content:')
    reading_file = list(file1.readlines())
    n = 0
    for i in reading_file:
        n = n+1
        print(f'Line {n} : {i}')
    file1.close()
except FileNotFoundError:
    print("Error: The file \'sample.txt\' was not found.")