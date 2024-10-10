function reverse(str) {
    if (!str || typeof str !== 'string') {
        return 'No Bueno'
    }
    else if (str.length < 2) {
        return str
    }
    else {
        const reverseString = [];
        for (let i = str.length - 1; i > -1; i--) {
            reverseString.push(str[i])
        }
        return reverseString.join('')
    }
}

const s = 'hello'
console.log(reverse(s))
console.log(reverse(0))
console.log(reverse('s'))
console.log(s.split('').reverse().join(''))