class Solution:
    def createSortedArray(self, instructions:list) -> int:
        sortedArray = []
        sortedArray.append(instructions[0])
        result = 0
        for num in instructions[1:]:
            l = len(sortedArray)
            i = 0
            j = l - 1
            count = 0
            for _ in range(l):
                if num <= sortedArray[i]:
                    sortedArray.insert(i, num)
                    result += count
                    break
                if num >= sortedArray[j]:
                    sortedArray.insert(j+1, num)
                    result += count
                    break
                i += 1
                j -= 1
                count += 1
        return result

    def createSortedArray2(self, instructions:list) -> int:
        sortedArray = []
        num_dic = {
            instructions[0] : 1
        }
        sortedArray.append(instructions[0])
        result = 0
        temp_list = []
        for idx, num in enumerate(instructions[1:]):
            index = idx + 1
            temp_list.append(num)
            if index + 1 < len(instructions) and instructions[index + 1] == num:
                continue
            if num_dic.get(num) is not None:
                left = sortedArray.index(num) # 1, 3, 3
                right = len(sortedArray) - (left + num_dic.get(num))
                result += min(left, right)
                sortedArray = sortedArray[0: left] + temp_list + sortedArray[left:]
                # sortedArray.insert(left, num)
                num_dic[num] += len(temp_list)
                temp_list = []
                continue
            l = len(sortedArray)
            i = 0
            j = l - 1
            count = 0
            for _ in range(l):
                if num <= sortedArray[i]:
                    num_dic[num] = len(temp_list)
                    sortedArray = sortedArray[0: i] + temp_list + sortedArray[i:]
                    # sortedArray.insert(i, num)
                    result += count
                    temp_list = []
                    break
                if num >= sortedArray[j]:
                    num_dic[num] = len(temp_list)
                    sortedArray = sortedArray[0: j+1] + temp_list + sortedArray[j+1:]
                    # sortedArray.insert(j+1, num)
                    result += count
                    temp_list = []
                    break
                i += 1
                j -= 1
                count += 1
        return result

solution = Solution()
print(solution.createSortedArray2([1,3,3,3,2,4,2,1,2]))

