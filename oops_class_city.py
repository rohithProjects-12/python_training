class City:
    def addCityDetails(self,name,country):
        self.name = name
        self.country = country

    def printCityDetails(self):
        print("City Name: "+ self.name)
        print("Country: "+ self.country)

delhi = City()
delhi.addCityDetails("delhi","India")
delhi.printCityDetails()

mumbai = City()
mumbai.addCityDetails("mumbai","India")
mumbai.addCityDetails("London","India")
mumbai.printCityDetails()

chennai = City()
chennai.addCityDetails("chennai","India")
chennai.printCityDetails()

bangalore = City()
bangalore.addCityDetails("bangalore","India")
bangalore.printCityDetails()
