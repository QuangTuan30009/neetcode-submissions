class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # 1. Đếm tần suất bằng dictionary: {giá_trị: số_lần_xuất_hiện}
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # 2. Chuyển dict thành danh sách các cặp (giá_trị, tần_suất)
        # và sắp xếp giảm dần theo tần suất (x[1])
        items = list(freq.items())
        items.sort(key=lambda x: x[1], reverse=True)

        # 3. Lấy k phần tử đầu tiên (chỉ lấy giá trị số x[0])
        result = []
        for i in range(k):
            result.append(items[i][0])

        return result