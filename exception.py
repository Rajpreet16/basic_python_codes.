class e(Exception):
    def __init__(self):
        self.argument="lol"
        print(self.argument)

try:
    a=10
    b=0
    if b<=0:
        raise e
except e:
    print(e())
