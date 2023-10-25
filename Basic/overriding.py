#
class yoki:
    def name(self):
        print("yokesh")
class ram(yoki):
    def name(self):
        super().name()
        print("ram")
class arun(ram):
    def name(self):
        super().name()
        print("arun")
y=arun()
y.name()
