import matplotlib.pyplot as plt
import seaborn as sns
import monty_hall as mh
import pandas as pd


class Plot():
    '''This class stores the data for a particular instance of a simulation of the monty hall problem. It
        contains functionality to export a visualization of the win percentages.
    '''
    def __init__(self, doors = 3, iterations = 200):
        '''Create an attribute named sequence that will be a list that will 
        eventually contain dictionaries that we will use to create a data frame
        Attributes:

            doors(int): The number of doors that the simulation will be based on.

            iterations(int): The number of iterations that a simulation will be based on.

            sequence(list): Starts empty, is later populated by dictionaries each containing: num of
            iterations a game was played, percentage won for that simulation, doors used in that
            simulation, whether the door was switched or not for that simulation.

        '''
        self.iterations = iterations
        self.sequence = []
        self.doors = doors
        self.switch = True
        for i in range(1, iterations+1):
            self.sequence.append(i)
            if ( i % 2) == 0:
                y = mh.Simulation(doors)
                number_win = y.play_game(True, i)
            else:
                y = mh.Simulation(doors)
                number_win = y.play_game(False, i)
            self.sequence.append({"doors": self.doors, "iterations": i, "switched": self.switch, "percentage": number_win})
        self.make_plot()

    
    def make_plot(self):
        '''
            Use the sequence attribute to create a pandas Dataframe
        '''
        sns.set_theme(color_codes=True)
        df = pd.DataFrame(self.sequence)
        df = sns.load_dataset('df')
        df = sns.lmplot(x="iterations", y="percentage", data=df, hue="switched")
        plt.savefig(f"iterations{self.iterations}_doors_{self.doors}.png")

if __name__ == "__main__":
    '''
        Calling an instance of Plot by passing in doors as 5 and iterations as 100.
    '''
    Plot(100,5)
