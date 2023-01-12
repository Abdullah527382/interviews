import { LinkedList, LLNode } from "./linkedList";

function mergeSort(list: LinkedList<String>): LinkedList<String> {
  // Base case:
  let n = list.size();
  if (n == 1) return list;
  // Create left and right halfs of the array

  let mid = Math.floor(n.valueOf() / 2);
  let leftData = list.getHead()!.data;
  let rightData = list.getNodeAtIndex(mid)!.data;

  let left = new LinkedList(leftData);
  let right = new LinkedList(rightData);
  let count = 1;
  let curr = list.getHead()?.next;
  while (curr != null) {
    if (count < mid) {
      left.insertAtEnd(curr.data);
    } else {
      // Skip mid
      if (count > mid) right.insertAtEnd(curr.data);
    }
    count++;
    curr = curr.next;
  }
  left = mergeSort(left);
  right = mergeSort(right);
  return merge(left, right);
}
/**
 * @param ListA First half of the list
 * @param ListB Second half of the list
 */
function merge(
  listA: LinkedList<String>,
  listB: LinkedList<String>
): LinkedList<String> {
  // The first element of linked list is the minimum of the 2 first index
  console.log(
    "Merging lists: " + listA.toString() + " | AND | " + listB.toString() + "\n"
  );
  let minStartIndex =
    listA.getHead()!.data < listB.getHead()!.data
      ? listA.getHead()!.data
      : listB.getHead()!.data;

  //   console.log("Starting node: " + minStartIndex);

  let currA = listA.getHead();
  let currB = listB.getHead();
  let countA = 0;
  let countB = 0;

  //This might be an issue when facing duplicates
  if (minStartIndex === listA.getHead()!.data) {
    countA++;
    currA = currA!.next;
  } else {
    countB++;
    currB = currB!.next;
  }

  let sortedLinkedList = new LinkedList(minStartIndex);
  while (currA != null && currB != null) {
    if (compare(currA, currB)) {
      countB++;
      sortedLinkedList.insertAtEnd(currB.data);
      currB = currB.next;
    } else if (compare(currB, currA)) {
      countA++;
      sortedLinkedList.insertAtEnd(currA.data);
      currA = currA.next;
    }
  }
  // Append the remaining elements of the linked lists if any
  while (countA < listA.size()) {
    sortedLinkedList.insertAtEnd(currA!.data);
    currA = currA!.next;
    countA++;
  }
  while (countB < listB.size()) {
    sortedLinkedList.insertAtEnd(currB!.data);
    currB = currB!.next;
    countB++;
  }
  //   console.log("uccessfully merged !!! " + sortedLinkedList.toString());
  return sortedLinkedList;
}

/**
 * @param ListA First node to compare
 * @param ListB Second node to compare
 * @returns true if nodeA > nodeB
 */
function compare(nodeA: LLNode<String>, nodeB: LLNode<String>): boolean {
  return nodeA.data > nodeB.data;
}

let list = new LinkedList<String>("Abdullah Ahmed");

// Sort the lislet linkedList = new LinkedList<String>("Abdullah Ahmed");
list.insertAtEnd("Hej Monic");
list.insertAtEnd("Billy Bob");
list.insertAtEnd("Zed Shaws");
list.insertAtEnd("Ligma Man");
list.insertAtEnd("Abz Man");

let sortedList = mergeSort(list);
console.log(sortedList!.toString());
