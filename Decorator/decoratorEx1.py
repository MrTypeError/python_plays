import time

def test_timer(func):
    def wrapper(*args):
        print("Before")
        func(*args)
        print("After")
    return wrapper
class Test:
    @test_timer
    def decorated_methods(self):
        print("Run")

object=Test()
object.decorated_methods()

        