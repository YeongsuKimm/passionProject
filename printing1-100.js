var newNumbers = []
var i = 0

for (let i = 1; i < 101;i++) {
    if (i % 5 == 0 ||  i % 2 == 0) {
        newNumbers.push(i);
        console.log(newNumbers)
    }
}
console.log(newNumbers) 
