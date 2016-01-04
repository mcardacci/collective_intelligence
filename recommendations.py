# A dictionary of movie critics and their ratings of a small
# set of movies 
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5,
        'The Night Listener': 3.0},
    'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5, 'The Night Listener': 4.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5,
        'The Night Listener': 4.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0, 'Superman Returns': 3.0, 'You, Me and Dupree': 2.0,
        'The Night Listener': 3.0},
    'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
        'Superman Returns': 5.0, 'You, Me and Dupree': 3.5,'The Night Listener': 3.0},
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}

from math import sqrt

# EUCLIDEAN DIFFERENCE SCORE
# The value of one means that the two people have identical preferences.

# Returns a distance-based similarity score for person1 and person2
# Doesn't account for grade inflation
def sim_distance(prefs, person1, person2):
    # Get the list of shared items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si [item] = 1
            
    #if they have no ratings in common return 0
    if len(si) == 0: return 0

    #Add up the squares of all the differences
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in si])
    return 1/(1+sqrt(sum_of_squares))
 

# Example call sim_distance(critics, 'Lisa Rose', 'Gene Seymour')

# PEARSON CORRELATION SCORE
# Returns the Pearson Correlation coefficient for p1 and p2
def sim_pearson(prefs, p1, p2):
    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]: 
        if item in prefs[p2]: si[item] = 1

    # Find the number of elements
    n = len(si)

    # if they have no ratings in common, return 0
    if n==0: return 0

    # Add up all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Sum up the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # Sum up the products
    pSum = sum([prefs[p1][it]*prefs[p1][it] for it in si])

    # Calculate Pearson score
    num = pSum - (sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0

    r = num/den
    return r
sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')























>>>>>>> e0a194ef6fa32aa7b5eca969affb24cebf9fa90f
