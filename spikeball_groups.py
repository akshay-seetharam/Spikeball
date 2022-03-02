import names
import random
import numpy as np
import time
from tqdm import tqdm
from rich.prompt import Prompt
from rich.pretty import pprint
import warnings
warnings.filterwarnings("ignore")



def recursive_scheduler(games, schedule, bar):
    #print(f"recursive_scheduler called with \ngames: {games} \nschedule: {schedule}")
=======
# def recursive_scheduler(games, schedule):
#     print(schedule)

    games_scheduled = len(schedule)
    # base case
    if len(games) == games_scheduled:
        return schedule
    else:
        i = 0
        while i < len(games[games_scheduled][2]):
            if games[games_scheduled][2][i] and i not in schedule.values():
                break
            i += 1


        # no remaining options, then set previous game schedule to false and try again
        if i == sum(games[games_scheduled][2]):
            games[games_scheduled - 1][2][schedule[games_scheduled-1]] = False
            schedule.pop(games_scheduled - 1)
            return recursive_scheduler(games, schedule, bar)

        schedule[games_scheduled] = i
        bar.update()
        return recursive_scheduler(games, schedule, bar)
        
        


def schedule_helper(zipped, groups, time_dict):

    games = []

    schedule = {}

    for group in groups:
        i = 0
        while i < len(group):
            j = i + 1
            while j < len(group):
                games.append([group[i][0], group[j][0], group[i][1] and group[j][1]])
                j += 1
            i += 1

    random.shuffle(games)

    bar = tqdm(total=len(games))
    recursive_scheduler(games, schedule, bar)

    text_schedule = {}
    
    for i in schedule:
        text_schedule[games[i][0] + " vs. " + games[i][1]] = time_dict[schedule[i]]
    
    return text_schedule
    
    

def schedulify(zipped, timeslots, teams_per_group):

    num_teams = len(zipped)
    num_timeslots = len(timeslots)

    time_dict = dict(zip(range(num_timeslots), timeslots))

    if num_teams % teams_per_group != 0:
        raise Exception("Number of teams should be divisible by the number of teams per group")

    if (teams_per_group - 1) * num_teams / 2 > num_timeslots:
        raise Exception("Not enough timeslots for a round-robin")
    
    groups = np.reshape(zipped, (int(num_teams/teams_per_group), int(teams_per_group), 2))
    

    # what do we have now:
    # groups: a num_groups by teams_per_group by 2 array listing each team in its group along with which timeslots it can handle
    # time_dict: a dictionary that connects the index of a timeslot to the datetime
    
    return schedule_helper(zipped, groups, time_dict)
    
if __name__ == '__main__':
    start_time = time.time()
    with open('teams.txt', 'r') as f:
        teams = f.readlines()
    num_teams = len(teams)

    i = 0
    while i < len(teams):
        teams[i] = teams[i][:-1]
        i += 1


    #pprint((num_teams, teams))
=======


    with open('timeslots.txt', 'r') as f:
        timeslots = f.readlines()
    i = 0
    while i < len(timeslots):
        timeslots[i] = timeslots[i][:-1]
        i += 1
        

    #pprint(timeslots)
=======


    
    num_timeslots = len(timeslots)
    time_compatibilities = np.zeros((num_teams, num_timeslots), dtype=bool)

    i = 0
    while i < num_teams:
        j = 0
        while j < num_timeslots:
            if np.random.random() < 0.6:
                time_compatibilities[i][j] = True
            j += 1
        i += 1

    time_compatibilities = time_compatibilities.tolist()
    user_input = int(Prompt.ask("Number of teams in each group?", default="2"))
    assert(user_input > 0)
    text_schedule = schedulify(list(zip(teams, time_compatibilities)), timeslots, user_input)
    pprint(text_schedule)
    print("Done in %s seconds." % (time.time() - start_time))
