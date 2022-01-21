# mrasimzahid.github.io

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas) - sum(cost) < 0):
            return -1
        
        gas_tank, start_index = 0, 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0
            
        return start_index
        
        
        
#         len_gas = len(gas)
#         gas = gas + gas
#         cost = cost + cost
#         tank = 0
#         for index in range(len_gas): 
#             tank = 0
#             for i in range(index, index+len_gas):
#                 tank += gas[i]
#                 fule_burn = cost[i]
#                 tank = tank - fule_burn -> 1
#                 if tank < 0:
#                     if index is (index+len_gas):
#                         flag = True
#                     else:
#                         flag = False
#                         break
#                 if index is (index+len_gas):
#                     flag = True
#             if flag:
#                 return index
#         return -1