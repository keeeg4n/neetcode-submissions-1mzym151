func topKFrequent(nums []int, k int) []int {
	count := make(map[int]int)
    for _, n := range nums {
        count[n]++
    }
    
    freq := make([][]int, len(nums)+1)
    for num, frequency := range count {
        freq[frequency] = append(freq[frequency], num)
    }
    
    result := []int{}
    for i := len(freq) - 1; i > 0; i-- {
        for _, num := range freq[i] {
            result = append(result, num)
            
            if len(result) == k {
                return result
            }
        }
    }
    
    return result 
}
