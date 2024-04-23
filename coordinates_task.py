import math

class Shape:
    def __init__(self, coordinates):
        self.coordinates = coordinates     

    def checkCountOfCoordinates(self,pointCoordinates):
        for i in range(len(pointCoordinates)):
            if len(pointCoordinates[i].coordinates) != len(pointCoordinates[0].coordinates):
                return 0

        return len(pointCoordinates)

    def checkIfXisInside(self,pointCoordinates, X):
        min_coordinates =[min(coord) for coord in zip(*[cords.coordinates for cords in pointCoordinates])]#vraca min [x1,x2,x3..][y1,y2,y3...]..
        max_coordinates = [max(coord) for coord in zip(*[cords.coordinates for cords in pointCoordinates])]
        
        for i in range(len(X.coordinates)):
            if X.coordinates[i] < min_coordinates[i] or X.coordinates[i] > max_coordinates[i]:
                return False
        return True

    def dimensional_diagonal(self,pointCoordinates):
        coordinates = [list(map(float, cord.coordinates)) for cord in pointCoordinates]
        diagonal =  math.sqrt(sum ([(max(coord) - min(coord)) ** 2 for coord in zip(*coordinates)]))
        return diagonal
        
    def differentSizeOfSides(self,pointCoordinates):
        coordinates = [list(map(float, cord.coordinates)) for cord in pointCoordinates]
        sizeOfSides = set([(max(coord) - min(coord)) for coord in zip(*coordinates)])

        return sizeOfSides
        
class Rectangle(Shape):
    def __init__(self, coordinates):
        super().__init__(coordinates)

    def checkIfXisInside(self, pointCoordinates, X):
        
        if(super().checkIfXisInside(pointCoordinates, X)):
            print("X is inside the rectangle")
        else:
            print("X isn't inside the rectangle")
    
    def dimensional_diagonal(self, pointCoordinates):
        diagonal = super().dimensional_diagonal(pointCoordinates)
        print("------------------")
        print(f'Diagonal of rectangle is: {diagonal}')

    def differentSizeOfSides(self,pointCoordinates):
        differentSizes = super().differentSizeOfSides(pointCoordinates)
        if(len(differentSizes)>=2):
            print("------------------")
            print("Coordinates form a rectangle")
            print("Different sizes in rectangle are:")
            for size in differentSizes:
                print(size)

    
class Cuboid(Shape):
    def __init__(self, coordinates):
        super().__init__(coordinates)

    def checkIfXisInside(self, pointCoordinates, X):
        
        if(super().checkIfXisInside(pointCoordinates, X)):
            print("X is inside the cuboid")
        else:
            print("X isn't inside the cuboid")
    
    def dimensional_diagonal(self, pointCoordinates):
        diagonal = super().dimensional_diagonal(pointCoordinates)
        print("------------------")
        print(f'Diagonal of cuboid is: {diagonal}')

    def differentSizeOfSides(self,pointCoordinates):
        differentSizes = super().differentSizeOfSides(pointCoordinates)
        if(len(differentSizes)>=3):
            print("------------------")
            print("Coordinates form a cuboid")
            print("Different sizes in cuboid are:")
            for size in differentSizes:
                print(size)

def loadCordsFromFile(coordinatesFile):
    with open(coordinatesFile, 'r') as file: 
                pointCoordinates = [Shape(line.strip().split(',')) for line in file]          
                return pointCoordinates

def main():
    try:
        listOfCordinates = loadCordsFromFile("coordinates.txt")
        if(len(listOfCordinates)!=0):
            X=listOfCordinates.pop()

            shape = Shape(listOfCordinates)
            rectangle = Rectangle(listOfCordinates)
            cuboid = Cuboid(listOfCordinates)

            countOfCoordinates=shape.checkCountOfCoordinates(listOfCordinates)
            differentSizeOfSides=shape.differentSizeOfSides(listOfCordinates)

            if countOfCoordinates == 3:
                if(len(differentSizeOfSides)>=2):
                    rectangle.differentSizeOfSides(listOfCordinates)
                    rectangle.dimensional_diagonal(listOfCordinates)
                    rectangle.checkIfXisInside(listOfCordinates,X)
                else:
                    print("Coordinates have necessary number of axis to form a rectangle but their values aren't valid")
            elif countOfCoordinates == 4:
                if(len(differentSizeOfSides)>=3):
                    cuboid.differentSizeOfSides(listOfCordinates)
                    cuboid.dimensional_diagonal(listOfCordinates)
                    cuboid.checkIfXisInside(listOfCordinates,X)
                else:
                    print("Coordinates have necessary number of axis to form a cuboid but their values aren't valid")
            elif countOfCoordinates == 0:
                print("Coordinates have uneven number of axis!!!")
        else:
            print("File doesn't contain coordindates")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()