import os

current_path = os.path.abspath(__file__)
current_dir = os.path.dirname(os.path.abspath(__file__))

def changeCurrentDir():
    os.chdir(current_dir)

if __name__ == '__main__':
    print(current_dir)
    print(current_path)
