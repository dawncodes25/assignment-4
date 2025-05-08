text1 = input("Enter text to write to the file: ")
file1 = open('output.txt', 'w')
write1 = file1.write(text1)
file1.close()
print("Data successfully written to output.txt.")

text2 = input('Enter additional text to append: ')
file1 = open('output.txt', 'a')
write2 = file1.write(f'\n{text2}')
file1.close()
print("Data successfully appended.")

print("Final content of output.text:")
file1 = open('output.txt', 'r')
read1 = list(file1.readlines())
for i in read1:
    print(i)
file1.close()

