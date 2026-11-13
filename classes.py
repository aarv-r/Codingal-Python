class myclass:
    __privvar = 27
    def __privmeth(self):
        print("I am inside class myclass")
    def hello(self):
        print("private variable value ",myclass.__privvar)
foo = myclass()
foo.hello()
foo.__privmeth()