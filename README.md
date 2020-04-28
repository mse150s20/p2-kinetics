# Overview of Code
This code describes and models the current coronavirus (COVID-19) pandemic in the state of Idaho. With this, we hope to provide information on how well Idaho is dealing with COVID-19.

The idaho_infections.csv file can be found under the data directory. This file contains data from the sources provided below. It models the pandemic in Idaho as kinetic function of time in days, with equations that model the uninfected, infected, recovered, and deaths in Idaho. This file is probably the most important and valuable file in this project! 


# Software Requirements
This code requires access to a commandline terminal and to have a github account to access the p2-kinetics repository and to be able to track and collaborate with other researchers on this topic. For this program to run, python must be installed on the local machine. To download Python go to terminal, type in the command line "apt-get install python". This will start downloading Python onto the local machine. It will ask a few permission questions and you will have to let it install Python onto the local machine. Depending on the machine you are using you may have do download an additional program in the same mannor. Mac users, such as myself, running older operating systems have to download XQuartz. Without it my code ran but there was no visual graph of the data, but with XQuartz downloaded it worked as it should.


# How to Get This Code
To run the code on your computer, pull the p2-kinetics repository from github class master to your terminal, or fork the repository and pull the code from your own personal repository. Once you've done this you can now access all files needed. This code should give you the ability to graph the data colected as well as access the idaho_infections.csv file in order to view the raw data yourself. 

# How to Use This Code
To use this code you must be in the directory that contains the code. Type "$ python kinetics.py " + the path to the file that contains the data. To run the code, type python (filename.py) in your command line. For examples we'll move to the next section.

# Example of how to use this code
$ cd p2-kinetics/

$ python kinetics.py Data/idaho_infections.csv

A plot of the data from the data idaho_indections.csv will appear if everything is working correctly.


# Information About Idaho Infection data
The file idaho_infections.csv is the location where we're consolidating the infection vs. time data.
The data used to plot the graph contains information from idaho division of health resource (Link 1). Additional links used for additional information and further understanding of the virus can be found below.


## Links to specific sources
1. Idaho Division of Public Health - https://public.tableau.com/profile/idaho.division.of.public.health#

1. New York Times GitHub Repo -  https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

1. Idaho Statesman - https://www.idahostatesman.com/news/coronavirus/article242127516.html

# Results from playing with parameters
Increasing k1 makes the beginning of the infection begin sooner, and increasing k2 raises the maximum number of individuals that won't be infected.

Project 2 descriptions:

    Modeling kinetics: The rate of change between things, specifically the rate of change between the different species!
    
    A -> B -> C
    
The rates of change betweeen A->B and B->C determine when we will see a certain concentration, and the initial conditions. 

Species C:
    Comes from a reaction from B->C
    
    Line 14 has k2*B in that big list that's returned
    That means: dC/dt = k2 * B
    That means: The amount of C goes up over time, depending on how much B there is.
    
Species A: 

    dA/dt is in the first element of the list returned on line 14

    dA/dt = -k1*A*B/(A+B+C)

This reaction depends on the concentration of A and the concentration of B
concentration of A is A/(A+B+C), and the concentration of B is B/(A+B+C)

Both k1 and k2 are our reaction constants for this project.
