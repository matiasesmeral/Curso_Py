
#import numbers
#import os
#if os.path.exists("demofile.txt"):
#  os.remove("demofile.txt")
#else:
#  print("The file does not exist")

def append():
    number = [10,11,12,13];
    with open("./archivosPy/names.txt","a") as f:
        for i in number:
            f.write(str(i));
            f.write("\n")
            
def read():
    numbers = [];
    f = open("./archivosPy/names.txt","r",encoding="utf-8")
    #for i in f:
    #    numbers.append(i)
    #print(numbers)
    print("----------------")    
    print(f.read())

def write():
    numbers = [1,2,3,4,5,6,7,8,9];
    with open("./archivosPy/names.txt","w") as f:
        for num in numbers:
            f.write(str(num))
            f.write("\n");
def run():
    read()

if __name__=="__main__":
    run()