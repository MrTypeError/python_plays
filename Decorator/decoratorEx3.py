import datetime
def log(func):
    def wrapper(*args,**kwargs):
        with open("log.txt","a") as f:
            f.write("called function with "+" ".join([str(arg)for arg in args ])+ "at" + str(datetime.datetime.now())+"\n")
        value= func(*args,**kwargs)
        return value
    return wrapper

@log
def run(a,b,c):
    print(a+b+c)

run(2,4,10)
