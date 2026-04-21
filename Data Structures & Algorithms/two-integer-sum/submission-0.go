func twoSum(nums []int, target int) []int {
    set := make(map[int]int)

	for i, val := range nums {
		diff := target - val
		if j, exists := set[diff]; exists {
			return []int{j, i} 
		}
		set[val] = i
	}

	return []int{}
}
