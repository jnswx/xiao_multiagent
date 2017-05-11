# mapRefinement.py
# 2017.5.11
# XIAO TANG
# tangxiao.dalian@gmail.com
import pursuerAgents as pursuers

class Refinement:

	def refine(abstractions, start, goal):
		"""
		level: abstraction highest level
		abstractions: [each level abstraction object]
		start: start position
		goal:  goal position

		return next position
		"""
		level = len(abstractions)
		startPosition = None
		goalPosition = goal
		while level > 0:
			currentMap = abstractions[level-1]
			startNode = currentMap.getNode(start)
			startPosition = startNode.position
			goalNode = currentMap.getNode(goalPosition)
			goalPosition = goalNode.position
			a = pursuers.AstarPursuer()
			next = a.aStar(None, startPosition, goalPosition, True, abstractionMap=currentMap)
			goalNode = currentMap.getNode(next)
			goalPosition = goalNode.getRandomChildPosition()
			print "level", level
			print "goalPosition", goalPosition
			level -= 1
		return goalPosition

	refine = staticmethod(refine)
