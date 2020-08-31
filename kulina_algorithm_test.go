package main

import (
	"fmt"
	"strconv"
)

// FUNGSI NOMOR 1 : sockMerchant
func sockMerchant(socks []int) int {
	pairOfSocks := map[int]int{}
	result := 0
	for _, sock := range socks {
		_, isExist := pairOfSocks[sock]
		if isExist {
			pairOfSocks[sock]++
			if pairOfSocks[sock] % 2 == 0 {
				result++
			}
		} else {
			pairOfSocks[sock] = 1
		}
	}

	return result
}

// FUNGSI NOMOR 2 : countingValleys
func countingValleys(steps []string) int {
	level_before := 0
    	level := 0
	result := 0
	for _, step := range steps {
		level_before = level
		if step == "U" {
			level++
		} else if step == "D" {
			level--
			if level_before == 0 {
				result++
			}
		}
	}
	return result
}

// FUNGSI NOMOR 3 : printZeros
func printZeros(num int){
	s :=strconv.Itoa(num)
	length := len(s)-1
	for _, char := range s {
		zeros := ""
		for j := 0; j < length; j++ {
			zeros = zeros + string("0")
		}
		length--
		fmt.Println(string(char)+zeros)
	}
}


func changeBool(n bool) bool {
	if n == true {
		return false
	} else {
		return true
	}
}

// FUNGSI NOMOR 4 : lampSwitch
func lampSwitch(numOfLamps int) []bool {
	lamps := make([]bool, numOfLamps)
	for i := 0; i < numOfLamps; i++ {
		for j := 0; j < numOfLamps; j++ {
			if (j+1) % (i+1) == 0 {
				lamps[j] = changeBool(lamps[j])
			}
		}
	}
	fmt.Println(lamps)
	return lamps
}

func main() {
	// NOMOR 1
	socks := []int{10,20,20,10,10,30,50,10,20}
	fmt.Println(sockMerchant(socks))

	// NOMOR 2
	steps := []string{"U", "D", "D", "U", "U", "D", "D", "U"}
	fmt.Println(countingValleys(steps))

	// NOMOR 3
	number := 1345679
	printZeros(number)

	// NOMOR 4
	numOfLamps := 100
	fmt.Println(lampSwitch(numOfLamps))
}
