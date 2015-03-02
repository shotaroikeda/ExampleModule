class Addition(object):

    def addthree(self,a,b,c):
        return (a+b+c)

    def addfour(self,a,b,c,d):
        return (a+b+c+d)

    def addfive(self,a,b,c,d,e):
        return (a+b+c+d+e)

class TestClass(Addition):
    def addfour(self, a, b, c, d):
        print "adding four"
        return super(TestClass, self).addfour(a,b,c,d)
    def addthree(self, a, b, c):
        return "I don't feel like adding"

    def newfunct(self):
        return "I'm a new function!"

if __name__ == '__main__': # Only run when you do python mathmatic.py
    test = TestClass()
    print test.addfour(1,2,3,4)
