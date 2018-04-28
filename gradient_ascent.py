#Currently broken: Not sure why, may revist later
#This file demonstrates sotcastic gradient ascent
# when choosing actions by having a preference not tied
# to reward when choosing an action

import numpy as np
import random
import math

randomint = random.randint(1,51) #How many actions we will have between 1 - 50
rewards = np.random.rand(1,randomint) #Rewards for each action set randomly
best_action = max(rewards[0]) #Find the best reward

print("Total choices are ", randomint, "!")

#Table for holding our progress so far, Col index is the action number
# Row 1: Total reward for an action
# Row 2: Number of times action chosen
# Row 3: Current preference for that action
table = np.zeros((3,randomint))
a = 0.1 #Stepsize constant 
e_rate = 0.2 #Exploration Rate

total_reward = 0 

def prob(index, array, curr_pref):
    try:
        return (math.exp(curr_pref) / sum([x for i, x in enumerate(array) if i !=\
                                       index]))
    except:
        return 0

#Loop for any number of times to allow the agent to try and pick
for attempt in range(100):

    #Do greedy algorithm only a % of the time
    if (random.random() > e_rate):
        #Equation is action = argmax(Ht(a))
        #Get the current action by greedily picking the max of a prefrence
        curr_action = max((value, index) for index, value in enumerate(table[2]))
    #Otherwise, pick a random value for exploration
    else:
        #Pick a random action
        ran_action = (random.randint(1,randomint) - 1)
        curr_action = (0,ran_action)

    action_index = curr_action[1] #What index is the action 

    curr_reward = rewards[0][action_index] #Grab reward from rewards table 
    #Update the table
    table[0][action_index] += curr_reward #Update reward for action
    table[1][action_index] += 1
    #Update table preference for action
    table[2][action_index] = table[2][action_index] - ((a * (curr_reward - \
                             table[0][action_index]/ table[1][action_index])) \
                             * prob(action_index, table[2], \
                             table[2][action_index]))

    #Update total reward
    total_reward += curr_reward

#Grab what the machine thinks is the best option overall
guess_best = max((value, index) for index, value in enumerate(table[2]))

print("Total reward was ", total_reward, "!")
print("Our AI thinks that the best choice is ", guess_best[1]+1, "!")

if rewards[0][guess_best[1]] == best_action:
    print("Our AI was correct!")
else:
    print("Dang, it was wrong...")
    
