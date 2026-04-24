class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o

    def do_work(self):
        if self.occupation == "actor":
            print(self.name,"is an actor")
        elif self.occupation == "tennis player":
            print(self.name,"is an tennis player")

    def speak(self):
        print(self.name,"says how are you?")

tom=Human("tom cruise","actor")
tom.do_work()
tom.speak()

gump=Human("Forrest gump","tennis player")
gump.do_work()
gump.speak()