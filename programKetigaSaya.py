import os
import sys


CONST_CURRENT_DIR = os.path.abspath(os.path.dirname(sys.argv[0]))
CONST_FOLDER = os.path.join(CONST_CURRENT_DIR, 'folder')
CONST_FOLDER1 = os.path.join(CONST_FOLDER, 'folder1')
CONST_FOLDER2 = os.path.join(CONST_FOLDER1, 'folder2')
# print(os.listdir(CONST_CURRENT_DIR))
print(CONST_CURRENT_DIR, CONST_FOLDER, CONST_FOLDER1, CONST_FOLDER2)

def main():

    # Windows -> "C:\\Users\\amirul\\belajarPython\\programPertamaSaya\\test.txt"
    # Linux/Mac OS -> "/home/amirul/belajarPython/programPertamaSaya/test.txt"

    ## mode
    # 'r'	Open a file for reading. (default)
    # 'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
    # 'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
    # 'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
    # 't'	Open in text mode. (default)
    # 'b'	Open in binary mode.
    # '+'	Open a file for updating (reading and writing)


    # with open('test.txt', 'a') as fp:
    #     fp.write("makan nasi\n")
    #     fp.write("dengan ayam\n")
    #     fp.write("dan sup\n")
    #     fp.close()


    # with open('test.txt', 'r') as fp:
    #     test = fp.read()
    #     print(test)
    #     fp.close()
    # print("END")

    # C:\Users\User\Desktop\e-learning\belajarPython\programPertamaSaya
    # /home/amirul/belajarPython/programPertamaSaya/test.txt
    # os.makedirs('/home/Users/User/Desktop/e-learning/belajarPython/programPertamaSaya/')
    # os.makedirs('C:\\Users\\User\\Desktop\\e-learning\\belajarPython\\programPertamaSaya\\folder1')

    # os.makedirs("folder\\folder1\\folder2")
    # with open('folder\\folder1\\folder2\\test.txt', 'r') as fp:
    # \\folder1\\folder2\\test.txt
    
    os.makedirs(os.path.join(CONST_FOLDER2, "folder3"))
    with open(os.path.join(CONST_FOLDER2, "test.txt"), 'r') as fp:
        test = fp.read()
        print(test)
        fp.close()
    print("END")

if __name__ == '__main__':
    main()
