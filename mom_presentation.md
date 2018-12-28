# Renting The House
Currently there are a lot of unmet expenses causing you anxiety. Jonah and I 
have been going back and forth. And, we think we have a solution by renting it
out through Airbnb etc. 

## Current 
Here is my estimation of the current monthly expenses for the house:
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
%matplotlib inline

data = pd.read_csv('house.csv')
expenses_monthly = data[data['Type1'] == 'Expenses']
expenses_monthly.iloc[:,1:].plot(x='Type2', y='Values', kind='bar', rot=45)
plt.ylabel('$')
plt.title('Monthly Expenses')
```

Monthly:
```python
expenses_monthly.Values.sum()
```
Yearly:
```python
expenses_monthly.Values.sum()*12
```
This is a large amount. Do you have plans to cover it when Grandma passes?

## Airbnb
With a lot of work, I think I can get the house in shape to rent out 4 bedrooms
at $20/night: 

```python
data.groupby('Type1').sum().plot(kind='bar', grid=True, rot=0)
plt.title("Monthly Without Garage")
plt.ylabel('$')
```
So, there's still a 1,000 shortfall every month, but down from 1,600.

## Moving Forward
Additionally, I see a path to improve the cash flow by renovating the garage
into a loft. 

```python
data.iloc[0,2] = 80*365/12
data.iloc[2,2] = -.25 * (data.iloc[:2,2].sum())
data.iloc[3,2] = -.5 * (data.iloc[:2,2].sum())

data.groupby('Type1').sum().plot(kind='bar', grid=True, rot=0)
plt.title("Monthly With Garage")
plt.ylabel('$')
```
Assuming we can rent the garage for 80/night, continue to rent the rooms in 
the house for a couple years, I think we can sell it for ~600,000. I can
make this money last for you for the rest of your life. You won't have anymore
financial problems. 

## Other Living Arrangements
But, I need you to be out of the house to make this work. I know you mentioned
Pittsburgh and you're interested in going to school for music. I also have a
couple other options for you based on my travels over the last two years:

- Colombia
    - incredibly cheap: 250/month for rent and food
    - most beautiful place I've seen. More so than Thailand.
- Mexico
    - cheap: 400/month for rent and food. 4/ride with Uber
    - Southern California, minus the prices
- Ypsilanti
    - cheap compared to Ann arbor: 1600/month for rent and food

## Music Teaching
I know you want to go back to school, but I think your main goal is to have an
impact on others through sharing your love for piano with them. A cheaper,
easier, more effective way to do that is taking online courses through
Udemy/Coursera and publishing your content on Youtube.

- Udemy
    - [Teaching Music: Start teaching an instrument successfully](https://www.udemy.com/teaching-piano-a-quick-guide-for-begginers/)
    - [Music Pedagogy: 7 advices to teach a musical instrument](https://www.udemy.com/music-pedagogy/)
- Coursera
    - [Fundamentals of Music Theory from The University of Edinburgh](https://www.coursera.org/learn/edinburgh-music-theory)
    - [Developing Your Musicanship from Berklee College of Music](https://www.coursera.org/specializations/musicianship-specialization)

If you search YouTube for "learn piano" you'll see a lot of videos from
different people. Some with many views, some with little. But, think about how
long one of your lessons are (1 hour) and the number of students you have at
any one time (one). Then think about a YouTube video you made to teach children
their first piano chord. Say it gets 200 views. How long would it take you to
teach 200 students in real life? 200 hours? Yet, you can make one 10 minute
video and get the same result. 


## Conclusion
Moving out and allowing Jonah and I to work towards renting out your place is a
step forward. It will help you reduce your current expenses, alleviate anxiety
about the future, and help me too.

