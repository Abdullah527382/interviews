function solution(inputArray) {

    let largestProduct = -Infinity 
    for (let i = 1; i < inputArray.length; i ++){
        let newlargestProduct = inputArray[i - 1] * inputArray[i]
        if (newlargestProduct > largestProduct){
            largestProduct = newlargestProduct;
        }
    }
    return largestProduct
}
