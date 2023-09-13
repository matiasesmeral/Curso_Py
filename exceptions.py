# Programa que permite enviar u
#try: - exception: - raise - assert:  
def run():

    try:
        print("Hello")
    except:
        print("Something went wrong")
    else:
        print("Nothing went wrong")

    
    x = "hello"
    if not type(x) is int:
        raise TypeError("Only integers are allowed")

if __name__ == "__main__":
    run();