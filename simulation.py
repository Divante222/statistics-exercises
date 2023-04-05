# How likely is it that you roll doubles when rolling two dice?
import numpy as np
import pandas as pd
outcomes = [1,2,3,4,5,6]

n_simulations = 10000

n_trials = 2

the_tests = np.random.choice(outcomes, (n_simulations, n_trials))
the_list = []
the_check_list = []
for i in the_tests:
    if i[0] == i[1]:
        the_list.append(True)
    else:
        the_list.append(False)
    the_check_list.append(i)

the_answer = np.array(the_list)  

print(the_answer.mean())
print('\n')



# If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

outcomes = ['heads','tails']
n_simulations = 100000
n_trials = 8


the_test = np.random.choice(outcomes, (n_simulations, n_trials))
df = pd.DataFrame(the_test)

exactly_3 = (df == 'heads').sum(axis=1) == 3
print(exactly_3)
print(exactly_3.mean())


# There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup 
# randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data 
# science students on them?

# 3 web dev / 1 data 
# 2 billboards chance
outcomes = ['data_science','web_development','web_development','web_development']

n_simulations = 100000
n_trials = 2

the_test = np.random.choice(outcomes, (n_simulations, n_trials))

df = pd.DataFrame(the_test)

print('\n\n\n')
print(((df[0] == 'data_science') & (df[1] == 'data_science')).mean())



# Codeup students buy, on average, 3 poptart packages with a standard deviation of 1.5 a day from the snack vending machine. 
# If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon? 
# (Remember, if you have mean and standard deviation, use the np.random.normal) You'll need to make a judgement call on how to handle some of your values

# 3 poptarts 1.5 std
# 17 poptarts monday
the_list = []
one_std = np.random.normal(3, 1.5, 10)
for i in one_std:
    the_list.append(i)
poptarts_friday = True
number_poptarts = 17

for i in range(52):
    for i in range(5):
        number_poptarts = number_poptarts - the_list[i]
        if number_poptarts < 0:
            poptarts_friday = False




