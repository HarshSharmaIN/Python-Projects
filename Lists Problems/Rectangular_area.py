#Level: Hard
'''
Given a 2D array of axis- aligned rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] denotes the ith rectangle where (xi1, yi1) are the coordinates of the bottom- left corner, and (xi2, yi2) are the coordinates of the top- right corner.
Calculate the total area covered by all rectangles in the plane. Any area covered by two or more rectangles should only be counted once.
Return the total area. Since the answer may be too large, return it modulo 10^9 + 7.


Input:
There is an integer n(size of ractangles, 2d array) is given as input.
In next n lines coordinates of each rectangle are given as input.

Constraints:
1 <= rectangles.length <= 200
rectanges[i].length == 4
0 <= xi1, yi1, xi2, yi2 <= 109

Output:
Return the total area. Since the answer may be too large, return it modulo 10^9 + 7.

Sample Input:
3
0 0 2 2
1 0 2 3
1 0 3 1

Sample Output:
6


The Code is as Follows:
'''
def rectangleArea(rectangles):
    MOD = 10**9 + 7
    
    #Collect all events
    events = []  # (x-coordinate, type, y1, y2)
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, 1, y1, y2))  # 1 is an opening one
        events.append((x2, -1, y1, y2)) # -1 is a closing one
    
    # Step 2: Sort events by x-coordinate
    events.sort()
    
    # Active set of intervals in the y-coordinate
    active_intervals = []
    
    # This Calculates the area
    prev_x = 0
    total_area = 0
    
    def compute_covered_y():
        """Calculates the total length covered by the union of intervals in active_intervals."""
        covered_y = 0
        prev_y = -1
        count = 0
        for y1, y2 in active_intervals:
            if y1 > prev_y:
                covered_y += y2 - y1
                prev_y = y2
            elif y2 > prev_y:
                covered_y += y2 - prev_y
                prev_y = y2
        return covered_y
    
    # Step 3: Sweep line
    for x, typ, y1, y2 in events:
        # Update the total area based on the previous x
        total_area += (x - prev_x) * compute_covered_y()
        total_area %= MOD
        prev_x = x
        
        # Update active_intervals based on the current event
        if typ == 1:  # Opening event
            active_intervals.append((y1, y2))
            active_intervals.sort()
        else:  # Closing event
            active_intervals.remove((y1, y2))
    
    return total_area % MOD

# Input
n = int(input())
rectangles = [list(map(int, input().split())) for _ in range(n)]

# Output
print(rectangleArea(rectangles))