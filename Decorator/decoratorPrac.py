
# def f1(func):
#     def wrapper():
#         print("code started")
#         func()
#         print("code ended" )
#     return wrapper
# @f1
# def calculator():
#     print("hello")

# calculator()

def new_try(func):
    def wrapper(*args,**kwargs):
        print("Another Example")
        value=func(*args,**kwargs)
        print(value)
        print("Execution Done")
        return value
    return wrapper        

@new_try
def new_calculator(a,b):
    return a+b

Sum=new_calculator(20,50)
