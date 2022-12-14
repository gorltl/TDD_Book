class TestCase:
    def __init__(self,name):
        self.name=name
    def run(self):
        self.setUp()
        method=getattr(self,self.name)
        method()
    def setUp(self):
        pass

class WasRun(TestCase):
    def testMethod(self):
        self.wasRun=1
    def setUp(self):
        self.wasRun=None
        self.wasSetUp=1
        self.log="setUp "

class TestCaseTest(TestCase):
    def setUp(self):
        self.test=WasRun("testMethod")
    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)
    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()