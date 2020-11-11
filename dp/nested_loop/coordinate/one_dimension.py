class one_dimension:
1093, 1645, 602,1565
"""
76. Longest Increasing Subsequence
https://www.lintcode.com/problem/longest-increasing-subsequence/description
Given a sequence of integers, find the longest increasing subsequence (LIS).
You code should return the length of the LIS.
Input:  [5,4,1,2,3] Output: 3 Explanation: LIS is [1,2,3]
Input: [4,2,4,5,3,7] Output: 4 Explanation: LIS is [2,4,5,7]
暴力：O(2^n) 每个数字可以选或不选
接龙型： 看成1*n矩阵， 任意一个点 都可以作为起点， 跳跃规则： 后一个点比前一个大
坐标型dp,  input维度=状态维度
其他解法:binary search
"""
    #left to right
    def longestIncreasingSubsequence(self, a):
        n = len(a)
        f = [1] * n if a else [0] #init： [1]最小情况
        # state: 错：前i个数最长序列长度(global_max) 对：从左到右跳到i的最长路径长度(local max)
        # ex:[7,8,9,1,2,3,4] 如果存global_max: f=[1,2,3,3,3,3,3], local_max: f=[1,2,3,1,2,3,4]
        # 坐标型dp：1维2维数组中，走到某个点的计算结果 local_max
        for i in range(n):
            for j in range(i):
                if a[j] < a[i]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f) # global max

    #打印最优解 2维 prv[i][j] = (i - 1, j - 2)
    def longestIncreasingSubsequence(self, a):
            f, prv = [1] * len(a) if a else [0], [-1] * len(a)

            for i in range(len(a)):
                for j in range(i):
                    if a[j] < a[i] and f[j] + 1 > f[i]:
                        f[i], prv[i] = f[j] + 1, j

            lngst, lst = 0, -1
            for i in range(len(a)):
                if f[i] > lngst:
                    lngst, lst = f[i], i

            pth = []
            while lst != -1:
                pth.append(a[lst])
                lst = prv[lst]
            print(pth[::-1])

            return max(f) # global max
"""
111. Climbing Stairs
https://www.lintcode.com/problem/climbing-stairs/description
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input:  n = 3 Output: 3 Explanation: 1) 1, 1, 1 2) 1, 2 3) 2, 1 total 3.
Input:  n = 1 Output: 1	Explanation: only 1 way.
"""
    def climbStairs(self, n):
        f = [1, 2] + [0] * (n - 2)

        for i in range(2, n):
            f[i] = f[i - 1] + f[i - 2]

        return f[n - 1] if n > 0 else 0
"""
116. Jump Game
https://www.lintcode.com/problem/jump-game/description
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
Input: [2,3,1,1,4] Output : true
Input : [3,2,1,0,4] Output : false
Challenge This problem have two method which is Greedy and Dynamic Programming.
The time complexity of Greedy method is O(n).
The time complexity of Dynamic Programming method is O(n^2).
We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.
Notice: The array A contains 𝑛 integers 𝑎1, 𝑎2, …, 𝑎𝑛 (1≤𝑎𝑖≤5000) (1≤n≤5000 )
"""
    def canJump(self, a):
        f = [True] + [False] * (len(a) - 1)

        for j in range(1, len(a)):
            for i in range(j + 1):
                if a[i] + i >= j and f[i]:
                    f[j] = True
                    break
            if not f[j]:
                break

        return f[-1]
"""
117. Jump Game II
https://www.lintcode.com/problem/jump-game-ii/description
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
Input : [2,3,1,1,4] Output : 2 Explanation : The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
Challenge
This problem have two method which is Greedy and Dynamic Programming.
The time complexity of Greedy method is O(n). The time complexity of Dynamic Programming method is O(n^2).
"""
    def jump(self, a):
        f = [0] + [sys.maxsize] * (len(a) - 1)

        for j in range(1, len(a)):
            for i in range(j):
                if a[i] + i >= j and f[i] != sys.maxsize:
                    f[j] = min(f[j], f[i] + 1)

        return f[-1]
"""
272. Climbing Stairs II
https://www.lintcode.com/problem/climbing-stairs-ii/description
A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
Input: 3 Output: 4 Explanation: 1 + 1 + 1 = 2 + 1 = 1 + 2 = 3 = 3 , there are 4 ways.
Input: 4 Output: 7 Explanation: 1 + 1 + 1 + 1 = 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 2 + 2 = 1 + 3 = 3 + 1 = 4 , there are 7 ways.
"""
    def climbStairs2(self, n):
        f = [1, 1, 2] + [0] * (n - 2)

        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2] + f[i - 3]

        return f[n]
"""
392. House Robber
https://www.lintcode.com/problem/house-robber/description
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you
from robbing each of them is that adjacent houses have security system connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
Input: [3, 8, 4] Output: 8 Explanation: Just rob the second house.
Input: [5, 2, 1, 3] Output: 8 Explanation: Rob the first and the last house.
Challenge O(n) time and O(1) memory.
"""
    def houseRobber(self, a):
        if not a:
            return 0
        f = [0] + [a[0]] + [0] * (len(a) - 1)

        for i in range(2, len(a) + 1):
            f[i] = max(f[i - 1], f[i - 2] + a[i - 1])

        return f[-1]
"""
602. Russian Doll Envelopes
https://www.lintcode.com/problem/russian-doll-envelopes/description
Give a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
Find the maximum number of nested layers of envelopes.
Input：[[5,4],[6,4],[6,7],[2,3]] Output：3 Explanation：the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Input：[[4,5],[4,6],[6,7],[2,3],[1,1]] Output：4 Explanation：the maximum number of envelopes you can Russian doll is 4 ([1,1] => [2,3] => [4,5] / [4,6] => [6,7]).
"""
"""
603. Largest Divisible Subset
https://www.lintcode.com/problem/largest-divisible-subset/description
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj)
of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
"""
    def largestDivisibleSubset(self, a):
        a, n, ans, t = sorted(a), len(a), [], 0 #sort为了先计算完小数字的答案，因为大数字的答案从小数字得出
        f, p = [0] * n, [-1] * n

        for i in range(1, n):
            for j in range(i):
                if a[i] % a[j] == 0 and f[j] + 1 > f[i]:
                    f[i], p[i] = f[j] + 1, j

                    if f[i] > f[t]:
                        t = i

        while t != -1:
            ans.append(a[t])
            t = p[t]

        return ans
"""
398. Longest Continuous Increasing Subsequence II #好像不应该叫subsequence, 因为答案要要连续index，应该叫subarray
https://www.lintcode.com/problem/longest-continuous-increasing-subsequence-ii/description
Give you an integer matrix (with row size n, column size m)，
find the longest increasing continuous subsequence in this matrix.
(The definition of the longest increasing continuous subsequence here
can start at any row or column and go up/down/right/left any direction).
Given a matrix:
[
  [1 ,2 ,3 ,4 ,5],
  [16,17,24,23,6],
  [15,18,25,22,7],
  [14,19,20,21,8],
  [13,12,11,10,9]
]
return 25
Challenge O(nm) time and memory.
"""
    def longestContinuousIncreasingSubsequence2(self, A):
        if not A or not A[0]:
            return 0

        n, m = len(A), len(A[0])
        points = []
        for i in range(n):
            for j in range(m):
                points.append((A[i][j], i, j))

        points.sort() #nested loop 执行顺序: ,某一节点的结果取决于之前所有比当前节点小的结果, 所有较小节点的结果要先算出来所以sort, 相当于选择之前最优结果, 之前最优结果只能从最小的开始算

        longest_hash = {}
        for i in range(len(points)):
            key = (points[i][1], points[i][2])
            longest_hash[key] = 1
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                x, y = points[i][1] + dx, points[i][2] + dy
                if 0 <= x < n or 0 <= y < m and A[x][y] < points[i][0]: #周围的邻居且小于当前值
                    longest_hash[key] = max(longest_hash[key], longest_hash[(x, y)] + 1)

        return max(longest_hash.values())
"""
622. Frog Jump
https://www.lintcode.com/problem/frog-jump/description
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone.
The frog can jump on a stone, but it must not jump into the water.
Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog is able to cross the river by landing on the last stone.
Initially, the frog is on the first stone and assume the first jump must be 1 unit.
If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units.
Note that the frog can only jump in the forward direction.
Given stones = [0,1,3,5,6,8,12,17] Input: [0,1,3,5,6,8,12,17] Output: true Explanation: There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,third stone at the 3rd unit, and so on...The last stone at the 17th unit.Return true.
The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Given stones = `[0,1,2,3,4,8,9,11]` Input: [0,1,2,3,4,8,9,11] Output: false Explanation:
Return false. There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
"""
        f = {e : set() for e in a}
        f[0].add(0)

        for e in a:
            for k in f[e]:
                for i in (-1, 0, 1):
                    n_e, n_k = e + k + i, k + i

                    if n_e in f and n_k > 0:
                        f[n_e].add(n_k)

        return len(f[a[-1]]) > 0
