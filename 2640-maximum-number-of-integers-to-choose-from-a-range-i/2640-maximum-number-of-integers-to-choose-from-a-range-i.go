func maxCount(banned []int, n int, maxSum int) int {
    // Create a set (map in Go) to store banned numbers for quick lookup
    bannedSet := make(map[int]bool)
    for _, num := range banned {
        bannedSet[num] = true
    }

    totalSum := 0
    count := 0

    // Iterate over numbers from 1 to n
    for i := 1; i <= n; i++ {
        if bannedSet[i] { // Check if the number is in the banned set
            continue
        }
        totalSum += i
        if totalSum > maxSum { // Stop if the sum exceeds maxSum
            break
        }
        count++
    }

    return count
}