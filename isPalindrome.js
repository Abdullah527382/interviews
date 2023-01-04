// This probs has complexity O(N/2) which is O(N); fact check this later
function solution(inputString) {
    
    // A palindrome is that of which has symmetric arrangement of letters
    let middleIndex = inputString.length/2
    // Have 2 counters running, one from end and one from start.
    let indexLeft = 0
    let indexRight = inputString.length - 1
    
    let isPalindrome = true
    
    // While the counters haven't reached length/2, continue
    while (indexLeft <= middleIndex && indexRight >= middleIndex){
        if (inputString[indexLeft] !== inputString[indexRight]){
            isPalindrome = false
            break 
        }
        indexLeft++
        indexRight--
    }
    return isPalindrome
}
