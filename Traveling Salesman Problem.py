# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:19:55 2019

@author: Talat Zubair
"""


import itertools, random, matplotlib.pyplot as plt


#l = ('A', 'B', 'C', 'D', 'E', 'F');
#permutation = itertools.permutations(l)   
#for i in list(permutation):
#    print(i)


class City:
     
   def __init__(self, id):
      self.id = id;
   
   def getId(self):
      return self.id;
   
   def distanceTo(self, city):
       distance = 0;
       if self.getId == 'A' :
           if city.getid == 'B':
               distance = 8;
           elif city.getid == 'C':
               distance = 10;
           elif city.getid == 'D':
               distance = 3;
           elif city.getid == 'E':
               distance = 4;
           elif city.getid == 'F':
               distance = 6;
       if self.getId == 'B' :
           if city.getid == 'A':
               distance = 8;
           elif city.getid == 'C':
               distance = 9;
           elif city.getid == 'D': 
               distance = 5;
           elif city.getid == 'E':
               distance = 8;
           elif city.getid == 'F':
               distance = 12;
       if self.getId == 'C' :
           if city.getid == 'A':
               distance = 10;
           elif city.getid == 'B':
               distance = 9;
           elif city.getid == 'D':
               distance = 7;
           elif city.getid == 'E':
               distance = 6;
           elif city.getid == 'F':
               distance = 2;
       if self.getId == 'D' :
           if city.getid == 'A':
               distance = 3;
           elif city.getid == 'B':
               distance = 5;
           elif city.getid == 'C':
               distance = 7;
           elif city.getid == 'E':
               distance = 8;
           elif city.getid == 'F':
               distance = 11;
       if self.getId == 'E' :
           if city.getid == 'A':
               distance = 4;
           elif city.getid == 'B':
               distance = 8;
           elif city.getid == 'C':
               distance = 6;
           elif city.getid == 'D':
               distance = 8;
           elif city.getid == 'F':
               distance = 8;
       elif self.getId == 'F' :
           if city.getid == 'A':
               distance = 6;
           elif city.getid == 'B':
               distance = 12;
           elif city.getid == 'C':
               distance = 2;
           elif city.getid == 'D':
               distance = 11;
           elif city.getid == 'E':
               distance = 8;
       return distance
   
   
   def __repr__(self):
      return str(self.id);



class Tour(City):
    totalcost = 0;
    c = City('A');
    tourlist = [c, c, c];
    
    def __init__(self, tourlist):
        del(self.tourlist[:]);
        self.tourlist = tourlist;
  
    def CalculateCost(self):
        totalcost = 0;
        for i in range(len(self.tourlist) - 1):
            totalcost = totalcost + self.tourlist[i].distanceTo(self.tourlist[i+1]);
        self.totalcost = totalcost;

    
    def getCost(self):
      return self.CalculateCost();
     
        
    
    
class Population(Tour):
    #list of all possible routes starting with C
    mylist = [('C', 'A', 'B', 'D', 'E', 'F'), ('C', 'A', 'B', 'D', 'F', 'E'), ('C', 'A', 'B', 'E', 'D', 'F'), ('C', 'A', 'B', 'E', 'F', 'D'), ('C', 'A', 'B', 'F', 'D', 'E'), ('C', 'A', 'B', 'F', 'E', 'D'), ('C', 'A', 'D', 'B', 'E', 'F'), ('C', 'A', 'D', 'B', 'F', 'E'), ('C', 'A', 'D', 'E', 'B', 'F'), ('C', 'A', 'D', 'E', 'F', 'B'), ('C', 'A', 'D', 'F', 'B', 'E'), ('C', 'A', 'D', 'F', 'E', 'B'), ('C', 'A', 'E', 'B', 'D', 'F'), ('C', 'A', 'E', 'B', 'F', 'D'), ('C', 'A', 'E', 'D', 'B', 'F'), ('C', 'A', 'E', 'D', 'F', 'B'), ('C', 'A', 'E', 'F', 'B', 'D'), ('C', 'A', 'E', 'F', 'D', 'B'), ('C', 'A', 'F', 'B', 'D', 'E'), ('C', 'A', 'F', 'B', 'E', 'D'), ('C', 'A', 'F', 'D', 'B', 'E'), ('C', 'A', 'F', 'D', 'E', 'B'), ('C', 'A', 'F', 'E', 'B', 'D'), ('C', 'A', 'F', 'E', 'D', 'B'), ('C', 'B', 'A', 'D', 'E', 'F'), ('C', 'B', 'A', 'D', 'F', 'E'), ('C', 'B', 'A', 'E', 'D', 'F'), ('C', 'B', 'A', 'E', 'F', 'D'), ('C', 'B', 'A', 'F', 'D', 'E'), ('C', 'B', 'A', 'F', 'E', 'D'), ('C', 'B', 'D', 'A', 'E', 'F'), ('C', 'B', 'D', 'A', 'F', 'E'), ('C', 'B', 'D', 'E', 'A', 'F'), ('C', 'B', 'D', 'E', 'F', 'A'), ('C', 'B', 'D', 'F', 'A', 'E'), ('C', 'B', 'D', 'F', 'E', 'A'), ('C', 'B', 'E', 'A', 'D', 'F'), ('C', 'B', 'E', 'A', 'F', 'D'), ('C', 'B', 'E', 'D', 'A', 'F'), ('C', 'B', 'E', 'D', 'F', 'A'), ('C', 'B', 'E', 'F', 'A', 'D'), ('C', 'B', 'E', 'F', 'D', 'A'), ('C', 'B', 'F', 'A', 'D', 'E'), ('C', 'B', 'F', 'A', 'E', 'D'), ('C', 'B', 'F', 'D', 'A', 'E'), ('C', 'B', 'F', 'D', 'E', 'A'), ('C', 'B', 'F', 'E', 'A', 'D'), ('C', 'B', 'F', 'E', 'D', 'A'), ('C', 'D', 'A', 'B', 'E', 'F'), ('C', 'D', 'A', 'B', 'F', 'E'), ('C', 'D', 'A', 'E', 'B', 'F'), ('C', 'D', 'A', 'E', 'F', 'B'), ('C', 'D', 'A', 'F', 'B', 'E'), ('C', 'D', 'A', 'F', 'E', 'B'), ('C', 'D', 'B', 'A', 'E', 'F'), ('C', 'D', 'B', 'A', 'F', 'E'), ('C', 'D', 'B', 'E', 'A', 'F'), ('C', 'D', 'B', 'E', 'F', 'A'), ('C', 'D', 'B', 'F', 'A', 'E'), ('C', 'D', 'B', 'F', 'E', 'A'), ('C', 'D', 'E', 'A', 'B', 'F'), ('C', 'D', 'E', 'A', 'F', 'B'), ('C', 'D', 'E', 'B', 'A', 'F'), ('C', 'D', 'E', 'B', 'F', 'A'), ('C', 'D', 'E', 'F', 'A', 'B'), ('C', 'D', 'E', 'F', 'B', 'A'), ('C', 'D', 'F', 'A', 'B', 'E'), ('C', 'D', 'F', 'A', 'E', 'B'), ('C', 'D', 'F', 'B', 'A', 'E'), ('C', 'D', 'F', 'B', 'E', 'A'), ('C', 'D', 'F', 'E', 'A', 'B'), ('C', 'D', 'F', 'E', 'B', 'A'), ('C', 'E', 'A', 'B', 'D', 'F'), ('C', 'E', 'A', 'B', 'F', 'D'), ('C', 'E', 'A', 'D', 'B', 'F'), ('C', 'E', 'A', 'D', 'F', 'B'), ('C', 'E', 'A', 'F', 'B', 'D'), ('C', 'E', 'A', 'F', 'D', 'B'), ('C', 'E', 'B', 'A', 'D', 'F'), ('C', 'E', 'B', 'A', 'F', 'D'), ('C', 'E', 'B', 'D', 'A', 'F'), ('C', 'E', 'B', 'D', 'F', 'A'), ('C', 'E', 'B', 'F', 'A', 'D'), ('C', 'E', 'B', 'F', 'D', 'A'), ('C', 'E', 'D', 'A', 'B', 'F'), ('C', 'E', 'D', 'A', 'F', 'B'), ('C', 'E', 'D', 'B', 'A', 'F'), ('C', 'E', 'D', 'B', 'F', 'A'), ('C', 'E', 'D', 'F', 'A', 'B'), ('C', 'E', 'D', 'F', 'B', 'A'), ('C', 'E', 'F', 'A', 'B', 'D'), ('C', 'E', 'F', 'A', 'D', 'B'), ('C', 'E', 'F', 'B', 'A', 'D'), ('C', 'E', 'F', 'B', 'D', 'A'), ('C', 'E', 'F', 'D', 'A', 'B'), ('C', 'E', 'F', 'D', 'B', 'A'), ('C', 'F', 'A', 'B', 'D', 'E'), ('C', 'F', 'A', 'B', 'E', 'D'), ('C', 'F', 'A', 'D', 'B', 'E'), ('C', 'F', 'A', 'D', 'E', 'B'), ('C', 'F', 'A', 'E', 'B', 'D'), ('C', 'F', 'A', 'E', 'D', 'B'), ('C', 'F', 'B', 'A', 'D', 'E'), ('C', 'F', 'B', 'A', 'E', 'D'), ('C', 'F', 'B', 'D', 'A', 'E'), ('C', 'F', 'B', 'D', 'E', 'A'), ('C', 'F', 'B', 'E', 'A', 'D'), ('C', 'F', 'B', 'E', 'D', 'A'), ('C', 'F', 'D', 'A', 'B', 'E'), ('C', 'F', 'D', 'A', 'E', 'B'), ('C', 'F', 'D', 'B', 'A', 'E'), ('C', 'F', 'D', 'B', 'E', 'A'), ('C', 'F', 'D', 'E', 'A', 'B'), ('C', 'F', 'D', 'E', 'B', 'A'), ('C', 'F', 'E', 'A', 'B', 'D'), ('C', 'F', 'E', 'A', 'D', 'B'), ('C', 'F', 'E', 'B', 'A', 'D'), ('C', 'F', 'E', 'B', 'D', 'A'), ('C', 'F', 'E', 'D', 'A', 'B'), ('C', 'F', 'E', 'D', 'B', 'A')];
    pop = [];
    
    def __init__(self):
        #randomly selecting 10 routes
        self.pop = random.sample(self.mylist, 10);


    def CreatePopulation(self, pop):
        self.pop = pop;

    
    def GetIndividual(self, num):
        return self.mylist[num];
    

    def GetPopulation(self):    
        return self.pop;


class GeneticAlgorithm:
    GenerationCount = 0;
    parent1 = [];
    parent2 = [];
    offspring1 = [];
    offspring2 = [];
    pop = [];
    survivors = [];

    def __init__(self, pop):    
        self.pop = pop;
    
    
    def ParentSelection(self):
        select = random.sample(self.pop, 2);    
        if select[1].getCost > select[2].getCost:
            self.parent1 = select[2];
        else:
            self.parent1 = select[1];
        select = random.sample(self.pop, 2);    
        if select[1].getCost > select[2].getCost:
            self.parent2 = select[2];
        else:
            self.parent2 = select[1];    
    
    

    def Crossover(self):
        self.offspring1 = [self.parent1[1], self.parent1[2], self.parent2[3], self.parent2[4], self.parent1[5], self.parent1[6]];
        self.offspring2 = [self.parent2[1], self.parent2[2], self.parent1[3], self.parent1[4], self.parent2[5], self.parent2[6]];


    def Mutation(self):
        e1 = self.offspring1.pop(3);
        self.offspring1.insert(5, e1);
        e2 = self.offspring2.pop(4);
        self.offspring2.insert(2, e2);
    

    def NewPopulation(self):
        self.pop.append(self.offspring1, self.offspring2);
        self.GenerationCount = self.GenerationCount + 1;
        return self.pop;
        
        
    def GetPop(self):
        return self.NewPopulation(self);

    def GenerationCount(self):
        return self.GenerationCount;

    def SurvivorSelection(self):
        p = self.GetPop().sort;
        return p[:6];
    
    
    
    
    
#MAIN
p = Population();
totalfitness = 0;
smallest = 9999;

while True:
    for i in range(10):
        T = Tour(p.GetIndividual(i));
        totalfitness = totalfitness + T.getCost();
        if T.getCost < smallest:
            smallest = T.getCost();
    G = GeneticAlgorithm(p.GetPopulation);
    G.ParentSelection();
    G.Crossover();
    G.Mutation();
    pnew = p.CreatePopulation(G.SurvivorSelection);
    avgfitness = totalfitness/100;
    if (G.GenerationCount > 100):
        break;
        
     
        
    plt.plot(avgfitness);
    plt.plot(smallest)
    plt.ylabel('Fitness')
    plt.xlabel('Generation')
    plt.show()
