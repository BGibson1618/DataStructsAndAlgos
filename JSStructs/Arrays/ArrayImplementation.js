class MyArray {
    constructor() {
        this.length = 0;
        this.data = {};
    }

    get(index) {
        return this.data[index];
    }

    push(item) {
        this.data[this.length] = item;
        this.length++;
    }

    pop() {
        const lastItem = this.data[this.length-1];
        delete this.data[this.length-1];
        this.length--;
        return lastItem;
    }

    delete(index) {
        const item = this.data[index];
        this.shiftItems(index);
        return this.pop();
    }

    shiftItems(index) {
        for (let i = 0; i < this.length; i++) {
            this.data[index] = this.data[index + 1];
        }
    }
}

const newArray = new MyArray();
newArray.push('hi');newArray.push('sup');newArray.push('how are you?');
console.log(newArray);
let x = newArray.delete(0);
console.log(newArray);
console.log(x);

// newArray.pop();
// let x = newArray.pop();
// console.log(newArray);
// console.log(x);
