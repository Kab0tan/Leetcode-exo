def two_sum(nums, target)
    i = 0
    while i < nums.length
        j = i+1
        while j < nums.length
            if nums[i]+nums[j] == target 
                return [i,j]
            end
            j+=1
        end
        i+=1
    end
end
