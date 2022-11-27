class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

       
        # at each point you have two choices 
        jobs = sorted(zip(startTime, endTime, profit))

        def binary_search(nums, idx):

            l, r = 0, len(nums)-1
            while l <= r:

                mid = (l + r) //2
                if nums[idx][1] <= nums[mid][0]: #valid interval ?

                    r = mid-1
                else:
                    l = mid+1

            return r


        @lru_cache(None)
        def dfs(index = 0 ):

            if index >= len(jobs):
                return 0

            # befor selctting this interval find next valid interval 
            #since it is sorted we can use binary seach 
            next_non_overlaping_index = binary_search(jobs, index)
            take = jobs[index][2] + dfs(next_non_overlaping_index+1)
            dont_take = dfs(index+1)

            return max(take, dont_take)

        return dfs()
                

            