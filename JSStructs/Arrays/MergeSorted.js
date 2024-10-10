function mergeSortedArrays(arr1, arr2) {
    if (arr1.length === 0) return arr2;
    if (arr2.length === 0) return arr1;

    const mergedArray = [];
    let i = 0;
    let j = 0;
    while (arr1[i] !== undefined && arr2[j] !== undefined) {
        if (arr1[i] < arr2[j]) {
            mergedArray.push(arr1[i]);
            i++;
        } else {
            mergedArray.push(arr2[j]);
            j++;
        }
    }

    return mergedArray;
}

const r1 = [0, 3, 4, 31, 87, 913]
const r2 = [4]

console.log(mergeSortedArrays(r1, r2));