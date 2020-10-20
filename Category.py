class Category:
    def __init__(self, name):
        self.name = name
        self.tasks = []
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def addTask(self, task):
        self.tasks.append(task)
    
    def getTask(self, index):
        return self.tasks[index]

    def getTasks(self):
        return self.tasks[:]
    
    def getNumberOfTasks(self):
        return len(self.tasks)