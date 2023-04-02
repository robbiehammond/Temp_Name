'''
    This file is used to generate a large set of puzzles that will be used in game. This file does not need to be accessed by the game itself, only the results produced by the file.
    
    The idea is to run this file, generate a large number of puzzles (maybe 100-10,000 for each difficulty), and then encode them in some simple file format. These will be generated into the
    "EncodedPuzzles" directory. This directory must be copied over to some directory within src/game/. When playing the game, it will randomly choose one of the generated puzzles for each level.
'''

class Puzzle:
    def __init__(self, difficulty):
        self.difficulty = difficulty





class PuzzleGenerator:
    def __init__(self, num_puzzles_to_generate):
        self.num_puzzles_to_generate = num_puzzles_to_generate
        self.solvable_puzzles = []
        self.num_solvable_generated = 0
        pass

    def generate(self, difficulty):
        pass

    def attemptToSolve(self, puzzle):
        solvable = False

        # insert solving logic here

        if solvable:
            self.solvable_puzzles.append(puzzle)
            self.num_solvable_generated += 1


    def writePuzzlesToFiles(self):
        for puzzle in self.solvable_puzzles:
            # create file 
            # open file 
            # write puzzle to file 
            # close and save file 
            
            

            
        





