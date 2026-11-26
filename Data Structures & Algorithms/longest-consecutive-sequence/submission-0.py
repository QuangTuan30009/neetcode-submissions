class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0
        #tìm điểm bắt đầu của chuỗi
        for x in num_set:
            # kiểm tra xem x - 1 có trong chuỗi k,
            #nếu có tức là nó là giữa chuỗi hoặc cuối chuỗi
            if (x - 1) not in num_set:
                cur = x 
                length  = 1 
                while (cur + 1) in num_set:
                    cur += 1
                    length += 1
                if length > best:
                    best = length
        return best