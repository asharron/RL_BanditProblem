import numpy as np
import random

randomint = random.randint(1,51) #How many actions we will have between 1 - 50
rewards = np.random.rand(1,randomint) #Rewards for each action set randomly
best_action = max(rewards[0]) #Find the best reward

print("Total choices are ", randomint, "!")

#Table for holding our progress so far, Col index is the action number
# Row 1: Total reward for each action
# Row 2: Total number of times called
table = np.zeros((2,randomint))

e_rate = .5 #Exploration rate
total_reward = 0 

#This is the equation for determining the value of an action
def q_equation(total_reward, total_called):
    return total_reward * total_called


#Loop for any number of times to allow the agent to try and pick
for attempt in range(10000):

    #Do a random choice for e_rate % of the time
    if (random.random() > e_rate):
        #Get the current action by greedily picking the max of the q_equation applied to
        # each reward and value in the table
        curr_action = max([(q_equation(tReward,tCalls),index) for index,\
                        (tReward,tCalls) in \
                        enumerate(zip(table[0],table[1]))])
    else:
        #Pick a random action
        ran_action = (random.randint(1,randomint) - 1)
        curr_action = (0,ran_action)

    curr_reward = rewards[0][curr_action[1]] #Grab reward from rewards table 

    #Update the table
    table[0][curr_action[1]] += curr_reward
    table[1][curr_action[1]] += 1

    #Update total reward
    total_reward += curr_reward

#Grab what the machine thinks is the best option overall
guess_best = max([(q_equation(tReward,tCalls),index) for index,\
                       (tReward,tCalls) in \
                       enumerate(zip(table[0],table[1]))])

print("Total reward was ", total_reward, "!")
print("Our AI thinks that the best choice is ", guess_best[1]+1, "!")

if rewards[0][guess_best[1]] == best_action:
    print("Our AI was correct!")
else:
    print("Dang, it was wrong...")
    
