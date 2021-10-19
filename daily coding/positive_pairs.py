"""
This problem was asked by Jane Street.

Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:

a + b = M
a XOR b = N

"""
for M in range(1, 1000):
    # M = int(input("Enter the first number "))
    # N = int(input("Enter the second number "))
    N = 10
    print('value of M and N', M, N)
    for a in range((M//2+1)):
        b = M - a
        if a ^ b == N:
            print(a, b)

    input('enter for next ')        




'''
type Pair struct {
	A, B int
}

// PositiveIntegerPairs returns all candidates
// that satisfy the following conditions:
// a + b = M
// a XOR b = N
func PositiveIntegerPairs(m, n int) []Pair {
	var pairs []Pair

	for a := 0; a < (m/2)+1; a++ {
		b := m - a
		if a^b == n {
			pairs = append(pairs, Pair{A: a, B: b})
		}
	}

	return pairs
}
'''