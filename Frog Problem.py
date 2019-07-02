# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:41:51 2019

@author: Talat Zubair
"""
            
def swap(i,j,s):
    return ''.join((s[:i], s[j], s[i+1:j], s[i], s[j+1:]));


def count():
    count.counter = count.counter + 1;

    
def possibleMoves(current_state): 
    moves = [];
    blank = current_state.index('_');
    goal_state = "111_000";
    if(current_state is goal_state):
        return moves;
    else:
        if(blank < 6 and current_state[blank+1] is '1'):
            moves.append(swap(blank, blank+1,current_state));
        if(blank < 5 and current_state[blank+2] is '1'):
            moves.append(swap(blank, blank+2,current_state));
        if(blank > 1 and current_state[blank-2] is '0'):
            moves.append(swap(blank-2,blank,current_state));
        if(blank > 0 and current_state[blank-1] is '0'):
            moves.append(swap(blank-1, blank,current_state));
    return moves;

    
def PrintList(l, level = 0):
    count();
    print(' ' * (level - 1) + ' ' * (level > 0) + l[0]);
    for i in l[1:]:
            PrintList(i, level + 1);
            

def SearchTree(string):
    tree=[];
    tree.append(string);
    temp=possibleMoves(string);
    while(temp):
        tree.append(SearchTree(temp.pop()));
    return tree;


count.counter=0;
start_state = "000_111";
PrintList(SearchTree(start_state));
print " ";
print "Number of states: " + str(count.counter);

