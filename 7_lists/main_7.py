# Lists Списки з данним, масив

nums = [4, 3, 55, 777, '3', True]
nums[0] = 'Array'
# print(nums[0])

nums_2 = [1, 2, 3, 4, [4, 'Array_2', True]]
# print(nums_2[-1][2])

nums_3 = [22, 3, 56, 11.1, 8, True]

# Функції списків
nums.append(45)  # додавання елем. в кінець списку
nums.insert(1, False)
# nums.extend(nums_2)
nums_3.sort()
nums_3.reverse()
nums_3.pop()
nums_3.remove(22)
# nums_3.clear()

print(nums_3)
print(nums_3.count(22))
print(len(nums_3))
