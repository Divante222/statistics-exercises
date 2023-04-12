import numpy as np
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
from pydataset import data

### for a two tail test you do not divide the p value by 2 for a 1 tail test you do divide the p value by two
### because you are only looking for 1 tail 
# Answer with the type of test you would use (assume normal distribution):


#=================================================================================
# Is there a difference in grades of students on the second floor compared to grades of all students?

# null = there is no differance 
# alternative = there is a difference

# Parametric Test
# I would use the One sample t-test: scipy.stats.ttest_1samp
# because it is comparing one set of data to another

# I am asuming there are more than 30 students per class
#=================================================================================


# Are adults who drink milk taller than adults who dont drink milk?

# null = there is no difference in height between adults who drink milk and adults who do not
# alternative = there is a difference in height between adults who drink milk and those that do not
# assuming we have over 30 samples I would use Independent t-test (or 2-sample): scipy.stats.ttest_ind
#=================================================================================


# Is the the price of gas higher in texas or in new mexico?
# again comparing two means i would use Independent t-test (or 2-sample): scipy.stats.ttest_ind
# 1 tail meaning divide the p value by 2
#=================================================================================


# Are there differences in stress levels between students who take data science vs students who take web development 
# vs students who take cloud academy?


#there are several means to compare so I would use the ANOVA: scipy.stats.f_oneway
#=================================================================================


# Ace Realty wants to determine whether the average time it takes to sell homes is different 
# for its two offices. 

# A sample of 40 sales from office #1 revealed a mean of 90 days and a # standard deviation of 15 days. 

# A sample of 50 sales from office #2 revealed a mean of 100 days and # a standard deviation of 20 days. 

# Use a .05 level of significance.

alpha = 0.05

sample_a = stats.norm(90, 15)


sample_b = stats.norm(100, 20)

sample_a_data = sample_a.rvs(40)

sample_b_data = sample_b.rvs(50)

    
print(sample_a_data.var(), sample_b_data.var())


t, p = stats.levene(sample_a_data, sample_b_data)
print(p > alpha)
##pvalue=0.05930830166570327 


print('the varience difference', p)


# pvalue for variance is greater than .05 equal_var == True
t, p = stats.ttest_ind(sample_b_data, sample_a_data, equal_var=True)

print(t, p)
print(p > alpha)
# p value tells if there is a significant differance and we want it less than .05 

### equal var true above false below

# only care about t value if there is greater than or less than direction
# we care about the negative or positive to tell if the mean is greater than or less than the one before
###=====================================================================================================


# Load the mpg dataset and use it to answer the following questions:
df = data('mpg')

# Is there a difference in fuel-efficiency in cars from 2008 vs 1999?
the_1999 = df[df['year'] == 1999]
the_2008 = df[df['year'] == 2008]


## create a average of the city and the highway miles and put the info into a mean column to run the data on for 2008 and 1999
alpha = .05


t, p = stats.levene(the_1999['hwy'], the_2008['hwy'])
print('p score for mileage')
print(p)

t, p = stats.ttest_ind(the_1999['hwy'], the_2008['hwy'], equal_var=True)


## greater than .05 or alpha no significant result          ==========================don't forget this is here===============================
## less than .05 there is a significant result


# there is no significant difference in fuel efficiency highway mileage so reject the null hypothesis
###========================================================= ============================================



# Are compact cars more fuel-efficient than the average car?
are_compact = df[df['class'] == 'compact']
are_not_compact = df[df['class'] != 'compact']


alpha = .05



t, p = stats.levene(are_compact.hwy, df.hwy)
print('lavene for highway mileage of cars')
print(p)

t, p = stats.ttest_ind(sample_b_data, sample_a_data, equal_var=False)
print()
print(p / 2)


t, p = stats.ttest_1samp(are_not_compact.hwy, df.hwy.mean())
print(p / 2)

## there is significant difference because the p value is less than .05 meaning we reject the null hypotheis
# 0.0021679015486328365






# greater than .05 or alpha no significant result          ==========================don't forget this is here===============================
## less than .05 there is a significant result


###=====================================================================================================
# Do manual cars get better gas mileage than automatic cars?

manual_cars = df[df.trans.str.contains('manual')]

automatic_cars = df[df.trans.str.contains('auto')]


t, pval = stats.levene(manual_cars['hwy'], automatic_cars['hwy'])
print('hello')
print(pval)


t, p = stats.ttest_ind(manual_cars['hwy'], automatic_cars['hwy'], equal_var=False)
print(p / 2)
# 1.6889124787124834e-05
print(t,p)


## the is a significant result because there are 5 zeros in front of the 3 in the p value
## we accept the null hypotheis because of this


# greater than .05 or alpha no significant result          ==========================don't forget this is here===============================
## less than .05 there is a significant result

## equal_var == true because if it is .05 or less 
