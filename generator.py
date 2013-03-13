import sys
import math
import random

class Generator(object):

    N = 624
    M = 397

    worldmap = []
    worldmap2 = []
    mt = []   # the array for the state vector
    mti = N+1 # mti==N+1 means mt[N] is not initialized

    height = 40
    width = 40
    seed = 4357

    def __init__(self, height, width, seed):
        self.height = height
        self.width = width
        self.seed = seed
        random.seed(seed)

        self.initcells()
        self.createWays()
        #self.sgenrand()
        
        self.printMap()

    def initcells(self):
    
       for i in range(self.height * self.width):
            self.worldmap.append('*')

       for i in range(self.height * self.width):
            self.worldmap2.append('*')

    def createWays(self):

        for j in range(int((self.width * self.height) * 0.35)):
            number = self.generateRandomNumber()

            if number < self.height * self.width:
                self.worldmap[number] = ' '
                
        self.connectWays()
        self.createEntrie()

    def createEntrie(self):

        for i in range(self.height):
            if i == 0 or i == self.height -1:
                for j in range(self.width):
                    self.worldmap[i * self.width + j] = '*'
            else:
                self.worldmap[i * self.width] = '*'
                self.worldmap[(i + 1) * self.width -1] = '*'
                
        entriePos = -1
        entrieFound = True
        
        while entrieFound:
            entriePos = self.generateRandomNumber()
            if entriePos > self.width * (self.height-1) or entriePos < self.width:
                self.worldmap[entriePos] = ' '
                entrieFound = False
            else:
                for i in range(self.height):
                    if entriePos == i * self.width or entriePos == (i + 1) * self.width -1:
                        self.worldmap[entriePos] = ' '
                        entrieFound = False
                        
    def generateRandomNumber(self):
    
        while True:
            number = random.random()
            number = number * (self.width * self.height)
            
            if number < (self.width * self.height):
                return int(number)
                
    def printMap(self):
    
        for x in range(self.height):
            for y in range(self.width):
                sys.stdout.write(self.worldmap[x * self.width + y])
            sys.stdout.write("\n")

    def getMap(self):
	
        return self.worldmap

    def connectWays(self):
    
        global xi, yi
        
        for xi in range(1, self.height-1):
            for yi in range(1, self.width-1):
                adjcount_r1 = 0 
                adjcount_r2 = 0

                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                                        
                        if(self.worldmap[((xi+ii) * self.width) + yi+jj] != '*'):
                            adjcount_r2 += 1

                for ii in (xi-2, xi+3):
                    for jj in (yi-2, yi+3):
                    
                        if abs(ii-xi) == 2 and abs(jj-yi) == 2:
                            continue
                        if ii < 0 or jj < 0 or ii >= self.height or jj >= self.width:
                            continue
                        if self.worldmap[ii * self.width + jj] != '*':
                            adjcount_r1 += 1
                    
                if adjcount_r1 >= 5 or adjcount_r2 <= 2:
                    #print 'adjcount_r1 = {} adjcount_r1 = {}'.format(adjcount_r1, adjcount_r2)
                    self.worldmap2[xi * self.width + yi] = '*'
                else:
                    #print 'adjcount_r1 = {} adjcount_r1 = {}'.format(adjcount_r1, adjcount_r2)
                    self.worldmap2[xi * self.width + yi] = ' '
            
        for yi in range(1, self.width):
            for xi in range(1, self.height):
                self.worldmap[xi * self.width + yi] = self.worldmap2[xi * self.width + yi]

if __name__ == '__main__':
    Generator(40, 40, 1234)
