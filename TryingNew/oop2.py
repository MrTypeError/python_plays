# Create a class that captures planets. Each planet has a name,
#  a distance from the sun, and its gravity relative to Earth’s gravity.
#  For distance and gravity, use the type double which captures real numbers. 
# Make objects for Earth and your favorite non-earth planet.

#--------------------------------------------------------------------------------------------------------------------------

class Universe:

    def __init__(self,Name,Distance,gravity,CName) :
        self.planetName=Name
        self.distanceSun=Distance+"Light Year"
        self.gravityFromEarth=gravity
        self.choiceName=CName


Planet_1=Universe("Earth,500.255",9.8,"Apna Gola")


nameOfPlanet=input("Enter the Conventational Name Of the Planet : -")
distanceOfThePlanet=float(input("Enter The Distance Of The planet Form The Sun : -"))
gravityRelativeEarth=float(input("Enter The Gravity Relative To Earth : -"))
givenName=input("Enter a Name of Your Choice : -")

Planet_2=Universe(nameOfPlanet,distanceOfThePlanet,gravityRelativeEarth,givenName)

