
def solution(subset,maxLength):
    if len(subset)<maxLength:
        return False
    for index1 in range(0,len(subset)-2):
        for index2 in range(index1+1,len(subset)-1):
            for index3 in range(index2+1,len(subset)):
                if not determinant(subset[index1][0],subset[index1][1],subset[index2][0],subset[index2][1],subset[index3][0],subset[index3][1]):
                    return False
    return True

def consistent(subset):
    for index1 in range(0,len(subset)-2):
        for index2 in range(index1+1,len(subset)-1):
            for index3 in range(index2+2,len(subset)):
                if not determinant(subset[index1][0],subset[index1][1],subset[index2][0],subset[index2][1],subset[index3][0],subset[index3][1]):
                    return False
    return True

def determinant(firstX,firstY,secondX,secondY,thirdX,thirdY):
    return (secondX-firstX)*(secondY-thirdY) - (secondX-thirdX)*(firstY-secondY)==0
    
def backtrackingRecursive(points,visited,numberOfPoints,maxLength):
    subset = []
    for index in visited:
        subset.append(points[index])
    if solution(subset,maxLength):
        print(subset)
    else:
        beginIndex = 0
        if visited!=[]:
            beginIndex = visited[-1]+1
        for index in range(beginIndex,numberOfPoints):
            visited.append(index)
            backtrackingRecursive(points,visited,numberOfPoints,maxLength)
            visited.pop()
            

def main():
    points = [(0,0),(1,1),(2,2),(3,1),(4,0)]
    numberOfPoints = 5
    visited = []
    for maxLength in range (numberOfPoints,2,-1):
        backtrackingRecursive(points,visited,numberOfPoints,maxLength)
    
main()
