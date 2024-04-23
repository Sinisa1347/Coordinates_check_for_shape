import math

class Shape:
    def __init__(self, coordinates):
        self.coordinates = coordinates

def loadCordsFromFile(coordinatesFile):
    #coordinatesFile = "koordinate.txt"

    try:
        with open(coordinatesFile, 'r') as file: 
                pointCoordinates = [Shape(line.strip().split(',')) for line in file]          
                return pointCoordinates
    except:
        print(f'Fajl pod nazivom {coordinatesFile} ne postoji')         

def checkCountOfCoordinates(pointCoordinates):
    for i in range(len(pointCoordinates)):
        if len(pointCoordinates[i].coordinates) != len(pointCoordinates[0].coordinates):
            print("Coordinates determine unknown figure")
            return False
    if(len(pointCoordinates)==3):
        print("Cordinates have a chance to form a rectangle")
    
    if(len(pointCoordinates)==4):
        print("Cordinates have a chance to form a cuboid")

    return True

def checkIfXisInside(pointCoordinates, X):
    min_coordinates =[min(coord) for coord in zip(*[cords.coordinates for cords in pointCoordinates])]#vraca min [x1,x2,x3..][y1,y2,y3...]..
    max_coordinates = [max(coord) for coord in zip(*[cords.coordinates for cords in pointCoordinates])]
    
    for i in range(len(X.coordinates)):
        if X.coordinates[i] < min_coordinates[i] or X.coordinates[i] > max_coordinates[i]:
            return False
    return True

def dimensional_diagonal(pointCoordinates):
    coordinates = [list(map(float, cord.coordinates)) for cord in pointCoordinates]

    sizeOfSides = [(max(coord) - min(coord)) ** 2 for coord in zip(*coordinates)]
    diagonal =  math.sqrt(sum ([(max(coord) - min(coord)) ** 2 for coord in zip(*coordinates)]))
    
        

    if len(set(sizeOfSides)) == 2:
        print("------------------")
        print("Coordinates form a rectangle")
        print(f'Diagonal of rectangle is: {diagonal}')
        print("------------------")
        return True
    elif len(set(sizeOfSides)) == 3:
        print("------------------")
        print("Coordinates form a cuboid")
        print(f'Diagonal of cuboid is: {diagonal}')
        print("------------------")
        return True
    else:
        print("Coordinates form an unknown shape!!!")
        return False

def main():
    try:
        listOfCordinates = loadCordsFromFile("coordinates.txt")
        
        X=listOfCordinates.pop()

        if(checkCountOfCoordinates(listOfCordinates)):#check if cords can determine rectangle or cuboid
            if(dimensional_diagonal(listOfCordinates)):
                if checkIfXisInside(listOfCordinates, X):
                    print("X is inside the shape")
                    print ("True")
                else:
                    print("X isn't inside the shape")
                    print ("False")
        else:
            print("Please check number of coordinates in each line in file")

    except FileNotFoundError:
        print("Datoteka s točkama nije pronađena.")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()