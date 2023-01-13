/**
 * Create a function which takes in a string and checks if 
 * the brackets are valid
 * 
 * "{ [] ( ) }" should return **`True`**
- "{ [(] ) }" should return **`False`**
- "{ [ }" should return **`False`**
 */

function bracketValidate(string: String): boolean {
  let bracketsArray = new Array();
  // Loop through the string
  for (let i = 0; i < string.length; i++) {
    if (string[i] !== " ") bracketsArray.push(string[i]);
  }

  /**
   * If the bracketsArray is odd, it is false since only even amount
   * of brackets is deemed valid.
   * If the brackets are even, the startIndex++ == endIndex--
   */
  //   console.log(bracketsArray);
  let limit = bracketsArray.length;

  if (limit % 2 !== 0) return false;

  let startIndex = 0;
  let endIndex = limit - 1;
  while (startIndex < limit / 2 && endIndex > limit / 2) {
    if (!isBracketPair(bracketsArray[startIndex], bracketsArray[endIndex])) {
      if (
        !isBracketPair(
          bracketsArray[startIndex],
          bracketsArray[startIndex + 1]
        ) ||
        !isBracketPair(bracketsArray[endIndex - 1], bracketsArray[endIndex])
      )
        return false;
    }
    startIndex++;
    endIndex--;
  }

  return true;
}

function isBracketPair(startBracket: string, endBracket: string): boolean {
  console.log(startBracket + " " + endBracket);
  if (
    (startBracket == "{" && endBracket == "}") ||
    (startBracket == "[" && endBracket == "]") ||
    (startBracket == "(" && endBracket == ")")
  )
    return true;
  return false;
}

console.log(bracketValidate("{ () {] }"));
