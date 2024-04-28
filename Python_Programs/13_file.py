# Reading a file

# f = open("D:\Python\Python_Programs\example.txt", "r")

# text = f.read()

# print(text)

# writing a file


# f = open("D:\Python\Python_Programs\example.txt", "w")

# f.write("hello everyone")

# f.close()



# append a file using with



# with open("D:\Python\Python_Programs\example.txt", "a") as f:
#     f.write("\t hello everyone how are you")


# read lines by lines content 

with open("D:\Python\Python_Programs\example.txt", "r") as f:
    while True:
        lines = f.readlines()
        if not lines:
            break
        print(lines)