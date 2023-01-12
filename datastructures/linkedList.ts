class LLNode<T> {
  data: T;
  next: LLNode<T> | null = null;

  constructor(data: T) {
    this.data = data;
  }
}

// We should create an interface for all the methods of linkedlist
interface ILinkedList<T> {
  insertInBegin(data: T): LLNode<T>;
  insertAtEnd(data: T): LLNode<T>;
  //   deleteNode(node: LLNode<T>): void;
  traverse(): T[];
  //   size(): number;
  //   search(comparator: (data: T) => boolean): LLNode<T> | null;
}

class LinkedList<T> implements ILinkedList<T> {
  private head: LLNode<T> | null = null;
  constructor(data: T) {
    this.head = new LLNode(data);
  }

  public traverse(): T[] {
    let nodes: T[] = [];
    let curr = this.head;
    while (curr != null) {
      nodes.push(curr.data);
      curr = curr.next;
    }
    return nodes;
  }

  public insertInBegin(data: T): LLNode<T> {
    let tempHead = this.head;
    this.head = new LLNode<T>(data);
    this.head.next = tempHead;
    return this.head;
  }

  public insertAtEnd(data: T): LLNode<T> {
    let curr = this.head;
    while (curr!.next != null) {
      curr = curr!.next;
    }
    curr!.next = new LLNode<T>(data);
    return curr!.next;
  }

  public deleteNode(data: T): void {
    let curr = this.head;
    while (curr?.next != null) {
      // Delete this node
      if (curr!.next.data === data) {
        let deleteNode = curr!.next;
        curr!.next = deleteNode.next;
      }
      curr = curr!.next;
    }
  }
  /**
   * @returns the size of the linked list
   */
  public size(): Number {
    // Note: You can also save this to local state
    let size = 0;
    let curr = this.head;
    while (curr != null) {
      size++;
      curr = curr.next;
    }
    return size;
  }
  /**
   *
   * @param comparator is a callback function specifying what data value we are searching for
   * @returns an LLNode if found data match, else returns null
   */
  public search(comparator: (data: T) => boolean): LLNode<T> | null {
    let curr = this.head;
    while (curr != null) {
      if (comparator(curr.data)) return curr;
      curr = curr.next;
    }
    return null;
  }

  public toString() {
    let nodeData = "";
    while (this.head != null) {
      nodeData += this.head.data;
      this.head = this.head.next;
    }
    return nodeData;
  }
}

let linkedList = new LinkedList<String>("Abdullah Ahmed");
console.log(linkedList.traverse());
console.log(linkedList.insertInBegin("Billy Bob"));
console.log(linkedList.traverse());
console.log(linkedList.insertAtEnd("Hej Monic"));
console.log(linkedList.traverse());
// linkedList.deleteNode("Hej Monic");
console.log(linkedList.traverse());
// linkedList.deleteNode("Abdullah Ahmed");
console.log(linkedList.traverse());
console.log(linkedList.size());
console.log(linkedList.search((string) => string === "Abdullahh Ahmed"));
