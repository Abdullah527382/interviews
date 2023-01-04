function solution(statues) {

    // This problem is just finding out how many numbers will it take to fill in the missing. 
    let sortedArr = statues.sort();
    console.log(sortedArr)
    let missing = 0
    for (i = 1; i < statues.length; i ++){
        let difference = statues[i] - statues[i - 1]
        if (difference > 1){
            missing += difference - 1
        }
    }
    return missing
}
