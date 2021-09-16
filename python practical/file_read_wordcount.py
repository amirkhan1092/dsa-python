

# f = open("E:\\Python39\\dsa-python\\dsa-python\\dsa-python\\python practical\\sampledata.txt")

# # data = f.read()  # read() will read the entire data of the file in the form of text 
# flag = True
# while flag:
#     line = f.readline()
#     data = "#".join(line.split())
#     print(data)
#     if line == '':
#         break




# f = open("E:\\Python39\\dsa-python\\dsa-python\\dsa-python\\python practical\\sampledatabinary.txt", "wb")

# while 1:
#     rolln = int(input("Enter the roll Number "))
#     name = input("Enter the name ")
#     marks = eval(input("Enter the marks "))
#     data = f"{rolln}\t{name}\t{marks}\n"
#     f.write(data.encode())
#     if input("Enter the Y for continue or N for exit: ") == 'N':
#             break
# f.close()

# h = eval('12.0')  # return the float


f = open("E:\\Python39\\dsa-python\\dsa-python\\dsa-python\\python practical\\sampledatabinary.txt", "rb+")

count = 0
roll_n = input("Enter the rolln ")
marks = input("Enter the marks ")

while 1:

    data = f.readline().decode().split()
    if roll_n == data[0]:
        data[-1] = int(marks)
    print(data)
    count += 1
    if data == '':
        break

print(data)








