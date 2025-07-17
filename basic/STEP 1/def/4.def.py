def hello():
    print("Hello!")

def repeat_hello():
    for i in range(3):
        hello()

repeat_hello()
