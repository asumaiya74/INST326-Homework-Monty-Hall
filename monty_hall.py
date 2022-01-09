import random

class Simulation():
    ''' Simulation takes an attribute, an integer, which represents the amount of doors 
        that the simulation will use to play the game.
    '''
    def __init__(self,numdoors):
        ''' Set an attribute named numdoors that will be the number of doors that will be used to play the game

            Parameters:
                numdoors(int): An integer; the number of doors that will be used to play the game
            
        '''
        self.numdoors = numdoors

    def set_random_doors(self):
        ''' Creating a list containing "zonk" string and replace the iteam in the list to the string "car"
            Parameters: 
                zonk_list(int): creating a list of zonks equal to the number of doors & randomly choose the doors. Set the random
                number of index as car. 

            Returns:
                str: the list of index
        
        '''
        zonk_list = ['zonk'] * self.numdoors
        zonk_list[(random.randint(0, self.numdoors-1))] = 'car'
        return zonk_list

    
    def choose_doors(self):
        '''Call set_random_doors() and save the list to a variable.

            Args:
                game_list(list): Pick and remove a random item from the this list which represents the door that the user/contestant has chosen
                alternate_choice(): choosing an alternate door and keep choosing random no until it is not equal to user no
            
            Returns:
                 The contestant door and the alternate door in that order as a tuple.

        '''
        game_list = self.set_random_doors()
        player_choice = int(random.randint(0, len(game_list) - 1))
        player_choice = game_list[player_choice]
        game_list.remove('zonk')
        
        alternate_choice = int(random.randint(0, len(game_list) - 1))
        alternate_choice = game_list[alternate_choice]
        return (player_choice, alternate_choice)
        

    def play_game(self, switch = False, iterations = 1):
        '''Playing the game as many time as the value iterations by using choose_doors() to pick door, 
            the user door and an alternate each time game played
        
        Parameters:
            switch(boolean): ; Default value of False; Determines whether a contestant decides to
            switch their door when playing the game and given the option to do so
            
            iterations(int): Default value of 1; The number of times that a person will play the game.
        
        Returns: 
            The percentage of the amount of times that the game was won as a decimal (float)
        '''
        numwins = 0.0
        for i in range(iterations):
            first, second = self.choose_doors()
            if switch:
                if second == 'car':
                    numwins += 1
                    continue
            else:
                if first == 'car':
                    numwins += 1
                    continue
        return numwins/iterations

if __name__ == "__main__":
    '''Creating an instance of Simulation and running a simulation by playing a
        game where the player switches doors and the iterations is 1_000
    '''
    x = Simulation(3)
    print(x.play_game(True, 1000))

