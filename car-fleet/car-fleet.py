// https://leetcode.com/problems/car-fleet

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse = True)
        count = 0 
        lastTime = None
        for i, (pos, speed) in enumerate(cars):
            if i == 0:
                lastTime = max(0, (target - pos) * 1.0 / speed)
                count += 1 
            else:
                time = max(0, (target - pos) * 1.0 /speed)
                if time > lastTime:
                    count += 1 
                lastTime = max(lastTime, time)
        return count