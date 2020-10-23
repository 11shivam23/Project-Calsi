responses=["Welcome to smart calculator","My name is Calsi","Thanks","Sorry, this is beyond my ability","Hello User"]

def extract_numbers(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def lcm(a,b):
    L=a if a>b else b
    while L<a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
        
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def end():
    print(responses[2])
    input("Press enter to exit")
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[3])
def hi():
    print(responses[4])
    
operations={"PLUS":add,"ADDITION":add,"SUM":add,"ADD":add,"MINUS":sub,"SUBTRACT":sub,"SUB":sub,"SUBTRACTION":sub,"DIFFERENCE":sub,"MULTIPLY":multiply,"MULTIPLICATION":multiply,"PRODUCT":multiply,"DIVIDE":divide,"DIVISION":divide,"LCM":lcm,"HCF":hcf}
commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end,"HI":hi,"HELLO":hi,"HEY":hi}

