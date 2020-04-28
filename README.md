# Overview of Code
This code describes and models the current coronavirus (COVID-19) pandemic in the state of Idaho. With this, we hope to provide information on how well Idaho is dealing with COVID-19.

It models the pandemic in Idaho as a kinetic function of time in days, with equations that model the uninfected, infected, recovered, and deaths in Idaho.

## Tell us a little bit about the idaho_infections.csv file and what it holds
The idaho_infections.csv file contains the reported numbers of the total reported infected people, deaths, and recoveries in Idaho. The file starts on the first day of reported cases in the state. It also includes the number of new cases of each designation. This csv file works in conjunction with kinetics.py as it will show the comparison of the reported data alongside with the projected data. 

# Software Requirements
This code requires access to a commandline terminal and to have a github account to access the p2-kinetics repository and to be able to track and collaborate with other researchers on this topic. For this program to run, python must be installed on the local machine. To download Python, go to terminal, type in the command line "apt-get install python". This will start 
downloading Python onto the local machine. Your computer will ask a few permission questions and you will have to let it install Python onto the local machine.

# How to Get This Code
To run the code on your computer, pull the p2-kinetics repository from github class master to your terminal, or fork the repository and pull the code from your own personal repository. 

# How to Use This Code
To use this code you must be in the directory that contains the code. Type "$ python kinetics" + the path to the file that contains the data. To run the code, type python (filename.py) in your command line. Then hit Enter.

# Example of how to use this code
`$ cd p2-kinetics/`

`$ python kinetics.py Data/idaho_infections.csv`

A plot will appear if everything is working correctly.


# Figures Showing Our Code Output Here

![alt text](#waiting for Cody's image to be merged here)

# Links to Cite Where We Got Our Data
1. Idaho Division of Public Health - https://public.tableau.com/profile/idaho.division.of.public.health#

1. New York Times GitHub Repo -  https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

1. Idaho Statesman - https://www.idahostatesman.com/news/coronavirus/article242127516.html

1. KTVB 7 - https://www.ktvb.com/article/news/health/coronavirus/idaho-confirms-first-covid-19-coronavirus-case/277-262de30b-ef00-40a2-b40e-43e26f0bb99b

1. Centers for Disease Control and Prevention - https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/summary.html#:~:text=On%20March%2011%2C%20the,of%20novel%20influenza%20viruses.


# Results from playing with parameters
Increasing k1 increases the rate at which uninfected people are infected, increasing k2 increases the rate at which people recover from the infected portion of the graph, and increasing k3 increases the rate at which people die from the infected portion of the graph.

# Info copy pasted from info.txt - should be cleaned up
Project 2 descriptions:
    Modeling kinetics: rate of change between things!
    
    A -> B -> C
    
The rates of change betweeen A->B and B->C Determine when we will see a certain concentration, AND the initial conditions. 

Species C:
    comes from a reaction from B->C
    
    Line 14 has k2*B in that big list that's returned
    That MEANS: dC/dt = k2 * B
    That means: Amount of C goes up over time, depending on how much B there is.
    k2 is a CONSTANT for this project
    
Species A: 
    dA/dt is in the first element of the list returned on line 14
    dA/dt = -k1\*A*B/(A+B+C)
This reaction depends on the concentration of A and the concentration of B
concentration of A is A/(A+B+C), and the concentration of B is B/(A+B+C)

k1 and k2 are our reaction constants

