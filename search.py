# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    """
    Initialize the frontier with nodes surrounding starting position.
    Frontier objects consist of the current node, as well as a list
    that keeps track of the path taken to get to that node.
    
    The frontier is a stack because we want a last in, first out mechanism
    for dfs.
    """
    
    frontier = util.Stack()
    for startFrontier in problem.getSuccessors(problem.getStartState()) :
        frontier.push((startFrontier, []))
    
    """
    Create a solution list to be filled and returned once success is met.
    Create lists for the nodes and node locations visited along the way
    so that we do not expand nodes twice.
    """
    solution = []
    nodesVisited = [problem.getStartState()]
    nodesVisitedLoc = [problem.getStartState()]
    currentNode = None
    
    while True:
        if frontier.isEmpty():
            return "Fail"
        else:
            """
            Pop the frontier to get the current node and append to visited node
            lists.
            """
            
            currentNode = frontier.pop()
            nodesVisited.append(currentNode[0])
            nodesVisitedLoc.append(currentNode[0][0])
            

        if problem.isGoalState(currentNode[0][0]):
            """
            When solution is found, append the directions of the current path
            to the solution list and return.
            """
            
            i = 0
            for node in currentNode[1]:
                solution.append(node[1])
                i = i + 1
            solution.append(currentNode[0][1])    
            
            return solution
        else:
            """
            Add current successors to a list only if they have not been
            expanded before
            """
            successors = []
            for successor in problem.getSuccessors(currentNode[0][0]):
                if successor[0] not in nodesVisitedLoc:
                    successors.append(successor)
            for successor in successors:
                """
                Create copies of the current path with each successor
                added on and push to frontier
                """
                currentPath = []
                for node in currentNode[1]:
                    currentPath.append(node)
                currentPath.append(currentNode[0])
                frontier.push((successor, currentPath))
            

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
#    from collections.abc import Iterable
#    
#    isIterable = False
#    startState = problem.getStartState()
#    startPos = None
#    if isinstance(startState[0], Iterable):
#        startPos = startState[0]
#        isIterable = True
#    else:
#        startPos = startState
    startPos = problem.getStartState()
    """
    Initialize the frontier with nodes surrounding starting position.
    Frontier objects consist of the current node, as well as a list
    that keeps track of the path taken to get to that node.
    
    The frontier is a queue because we want a first in, first out mechanism
    for bfs.
    """
    frontier = util.Queue()
    for startFrontier in problem.getSuccessors(startPos) :
        frontier.push((startFrontier, []))
    
    """
    Create a solution list to be filled and returned once success is met.
    Create lists for the nodes and node locations visited along the way
    so that we do not expand nodes twice.
    """
    solution = []
    nodesVisited = [startPos]
    nodesVisitedLoc = [startPos]
    currentNode = None
    
    while True:
        if frontier.isEmpty():
            return "Fail"
        else:
            """
            Pop the frontier to get the current node and append to visited node
            lists.
            
            Also, double check to make sure we aren't expanding a previously
            visited node.
            """
            while True:
                currentNode = frontier.pop()
                if currentNode[0][0] not in nodesVisitedLoc:
                    break
            nodesVisited.append(currentNode[0])
            nodesVisitedLoc.append(currentNode[0][0])
       
            

#        if (isIterable and problem.isGoalState(currentNode[1])) or problem.isGoalState(currentNode[0][0]):
        if problem.isGoalState(currentNode[0][0]):    
            """
            When solution is found, append the directions of the current path
            to the solution list and return.
            """
            i = 0
            for node in currentNode[1]:
                solution.append(node[1])
                i = i + 1
            solution.append(currentNode[0][1])    
            
            return solution
        else:
            """
            Add current successors to a list only if they have not been
            expanded before
            """
            successors = []
            i = 1
            for successor in problem.getSuccessors(currentNode[0][0]):
                if successor[0] not in nodesVisitedLoc:
                    successors.append(successor)
            for successor in successors:
                """
                Create copies of the current path with each successor
                added on and push to frontier
                """
                currentPath = []
                for node in currentNode[1]:
                    currentPath.append(node)
                currentPath.append(currentNode[0])
                frontier.push((successor, currentPath))
            

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    """
    Initialize the frontier with nodes surrounding starting position.
    Frontier objects consist of the current node, as well as a list
    that keeps track of the path taken to get to that node.
    
    The frontier is a priority queue because we want a first in, first out mechanism
    that prioritizes movement cost for ucs.
    """
    
    frontier = util.PriorityQueue()
    
    for startFrontier in problem.getSuccessors(problem.getStartState()) :
        """
        Push the usual frontier object, but use the cost in determining its
        order in the queue.
        """
        frontier.push((startFrontier, []), startFrontier[2])

    
    solution = []
    nodesVisited = [problem.getStartState()]
    nodesVisitedLoc = [problem.getStartState()]
    currentNode = None
    
    while True:
        if frontier.isEmpty():
            return "Fail"
        else:
            while True:
                currentNode = frontier.pop()
                if currentNode[0][0] not in nodesVisitedLoc:
                    break
            nodesVisited.append(currentNode[0])
            nodesVisitedLoc.append(currentNode[0][0])
            

        if problem.isGoalState(currentNode[0][0]):
            i = 0
            for node in currentNode[1]:
                solution.append(node[1])
                i = i + 1
            solution.append(currentNode[0][1])    
            
            return solution
        else:
            successors = []
            for successor in problem.getSuccessors(currentNode[0][0]):
                
                if successor[0] not in nodesVisitedLoc:
                    successors.append(successor)

            for successor in successors:
                currentPath = []
                currentSum = successor[2] + currentNode[0][2]
                for node in currentNode[1]:
                    currentPath.append(node)
                    """
                    Take the sum of the total current path and it along to the
                    cost of the current successor to determine its priority
                    level
                    """
                    currentSum = currentSum + node[2]
                currentPath.append(currentNode[0])
                frontier.push((successor, currentPath), currentSum)
            
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    """
    Initialize the frontier with nodes surrounding starting position.
    Frontier objects consist of the current node, as well as a list
    that keeps track of the path taken to get to that node.
    
    The frontier is a priority queue because we want a first in, first out mechanism
    that prioritizes movement cost for a*.
    """
    
    frontier = util.PriorityQueue()
    
    for startFrontier in problem.getSuccessors(problem.getStartState()) :
        """
        Push the usual frontier object, but use the sum of its cost and heuristic
        in determining its order in the queue.
        """
        currentHue = heuristic(startFrontier[0], problem)
        frontier.push((startFrontier, []), currentHue + startFrontier[2])

    
    solution = []
    nodesVisited = [problem.getStartState()]
    nodesVisitedLoc = [problem.getStartState()]
    currentNode = None
    
    while True:
        if frontier.isEmpty():
            return "Fail"
        else:
            while True:
                currentNode = frontier.pop()
                if currentNode[0][0] not in nodesVisitedLoc:
                    break
            
                
            nodesVisited.append(currentNode[0])
            nodesVisitedLoc.append(currentNode[0][0])

        if problem.isGoalState(currentNode[0][0]):
            i = 0
            for node in currentNode[1]:
                solution.append(node[1])
                i = i + 1
            solution.append(currentNode[0][1])    
            
            return solution
        else:
            successors = []
            for successor in problem.getSuccessors(currentNode[0][0]):
                
                if successor[0] not in nodesVisitedLoc:
                    successors.append(successor)

            for successor in successors:
                currentPath = []
                currentSum = successor[2] + currentNode[0][2]
                for node in currentNode[1]:
                    currentPath.append(node)
                    """
                    Take the sum of the total current path and it along to the
                    cost of the current successor to determine its priority
                    level
                    """
                    currentSum = currentSum + node[2]
                currentPath.append(currentNode[0])
                currentHue = heuristic(successor[0], problem)
                """
                Use the heuristic and current sum to determine the priority
                of the new frontier object.
                """
                frontier.push((successor, currentPath), currentSum + currentHue)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
