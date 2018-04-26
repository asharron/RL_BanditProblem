# Bandit Problem
This refers to the k-armed bandit problem and the standard intoructory RL algorithm used to solve it

# How it works
This uses the standard Qt(a) = E[Rt | At=a] formula to calculate which action should be taken at time step t. It also has an exploration rate in which it randomly chooses an action rather than the greedy solution. 

To use the file, install numpy with pip and run python3 on main.py. This will generate a random number of rewards and actions between 1 and 50. Then it will run through about 1000 times to see if the agent finds the action with the highest reward value. Sometimes it does, sometimes it doesn't

# Who is this for
Anyone who wants to see how the bandit problem looks like as arrays in a python implemenation 
