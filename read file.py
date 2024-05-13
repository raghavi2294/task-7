def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)


file_name = "E:\\workspace\\Pat-28\\task 7\\raji.txt"


read_file(file_name)

    