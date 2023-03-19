class RailwayForm:
    formType = "Railwayform"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

myapp = RailwayForm()
myapp.name = "harry"
myapp.train = "Rajdhani express"
myapp.printData()
        