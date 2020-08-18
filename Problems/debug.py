#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:54:43 2020

@author: ShuyangFu
"""

class Solution:
    def merge(self, intervals):
        
        def BinSearch(x, intlist) -> int:
            ### Return the smallest index of intervals in intlist of which right endpoint >= x
            n = len(intlist)
            if not intlist or x > intlist[-1][1]:
                return n
            
            i, j = 0, n
            while i < j:
                mid = (i+j) // 2
                if x > intlist[mid][1]:
                    i = mid + 1
                else:
                    j = mid
            return i        
            
                
        merged_int = []
        n = len(merged_int)
        for i, intv in enumerate(intervals):
#             if intv[0] > merged_int[-1][1]:
#                 merged_int.append(intv)
#                 continue
                
            pos = BinSearch(intv[0], merged_int) 
            # The first interval of which right endpoint >= left endpoint of intv
            l = intv[0]
            while pos < len(merged_int):
                l = min(merged_int[pos][0], l)
                if merged_int[pos][1] <= intv[1]:
                    merged_int.pop(pos)
            
            if pos < len(merged_int) and intv[1] >= merged_int[pos][0]:
                merged_int[pos][0] = l
            else:
                merged_int.insert(pos, [l, intv[1]])
                
        return merged_int
            
a = Solution().merge([[1,4],[0,1]])