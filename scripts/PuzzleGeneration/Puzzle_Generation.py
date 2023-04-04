'''
    This file is used to generate a large set of puzzles that will be used in game. This file does not need to be accessed by the game itself, only the results produced by the file.

    The idea is to run this file, generate a large number of puzzles (maybe 100-10,000 for each difficulty), and then encode them in some simple file format. These will be generated into the
    "EncodedPuzzles" directory. This directory must be copied over to some directory within src/game/. When playing the game, it will randomly choose one of the generated puzzles for each level.
'''
import numpy as np
from enum import Enum

# Each path can be modeled as a directional inputs.
# UP = move up by 1 tile, DOWN = move down by 1 tile, etc.
class Direction(Enum):
    UP = 1,
    DOWN = 2,
    LEFT = 3, 
    RIGHT = 4

class Puzzle:
    def __init__(self, n):
        # size of the puzzle (puzzle is N x N grid)
        self.size = n

        # total number of solutions 
        self.num_solutions = -1 # unassigned initially

        '''
        - Each path that can get you from the entrance to the exit is a number of direction inputs
        - This variable is the average number of inputs for all "non-trivial" paths
        - A trivial path is one that gets you from entrance to exit in <= 3 movements. These puzzles would be too easy, so 
          if a puzzle contains a path like this, it's not even worth considering a valid puzzle.
        '''
        self.avg_nontrivial_path_complexity = -1.0 # unassigned 

        # Each path in paths is the set of inputs required to get from entrance to exit for that specific path.
        self.paths = []

        self.grid = np.zeros(shape=(n, n))

        self.generate()


    # Numeric Difficulty = f(num_solutions, avg_nontrivial_path_complexity) = .4 * num_solutions + .6 * avg_nontrivial_path_complexity
    # This equation will make it so difficutly depends slightly more on how complex the average path is. 
    # Likely will need to be adjusted based on our own ideas.
    def get_numeric_difficulty(self):
        pass


    # 78% chance a tile is ice (0), 15% chance a single tile is snow (1), 2% chance it's a 2x2 island of snow, 5% chance it's an obstacle (2).
    # We can test and change these percentages later.
    def generate(self):
        for i in range(self.size):
            for j in range(self.size):
                # if something has already been assigned, don't try to reassign
                if self.grid[i, j] == 0:
                    tile = 0

                    # if we're not on the boundary, also consider generating island 
                    if (i < self.size - 1) and j < (self.size - 1):
                        tile = np.random.choice(np.arange(0, 4), p=[0.78, 0.15, .02, 0.05])
                    else:
                        tile = np.random.choice(np.arange(0, 3), p=[0.8, 0.15, 0.05]) # probabilities a bit adjusted, but it's fine 
                    
                    # if 3 chosen, generate 2x2 snow block
                    if tile == 3:
                        self.grid[i, j] = 1 
                        self.grid[i + 1, j] = 1
                        self.grid[i, j + 1] = 1
                        self.grid[i + 1, j + 1] = 1
                    # otherwise, just generate the single chosen tile
                    else:
                        self.grid[i, j] = tile

        print(self.grid)


class PuzzleGenerator:
    def __init__(self, num_puzzles_to_generate):
        self.num_puzzles_to_generate = num_puzzles_to_generate
        self.solvable_puzzles = []
        self.num_solvable_generated = 0
        pass


    def generate(self, size):
        while len(self.solvable_puzzles) < self.num_puzzles_to_generate:
            trialPuzzle = Puzzle(size)
            solvable = self.attemptToSolve(trialPuzzle)
            if solvable:
                self.solvable_puzzles.append(trialPuzzle)



    # Find ALL non-circular solutions, return if it can be done. Assign the number of solutions and average path complexity (number of movements needed) variables to get idea of difficulty.
    def attemptToSolve(self, puzzle):
        solvable = False

        # insert solving logic here

        return solvable

    def writePuzzlesToFiles(self):
        for puzzle in self.solvable_puzzles:
            pass
            # create file 
            # open file 
            # write puzzle to file 
            # close and save file 
            
            

