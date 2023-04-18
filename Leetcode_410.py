nums = [7, 2, 5, 10, 8]
size = len(nums)
k = 2

# min_ans -> k = size (largest element in list)
# max_ans -> k = 1 (sum of elements in list)

start = max(nums)
end = sum(nums)

while start < end:

    mid = int(start + (end - start)//2)

    sum = 0
    pieces = 1
    for num in nums:
        if sum+num > mid:
            sum = num
            pieces += 1
        else:
            sum += num

    if pieces > k:
        start = mid+1
    else:
        end = mid

print(end)

