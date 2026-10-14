for (i = 10; i >= 1; i--) {
    console.log(i)
}
console.log("==================")

let x = 5
let fact = 1
for (i = 1; i <= x; i++) {
    fact *= i;
}
console.log("Factorial =", fact)
console.log("==================")


for (i = 1; i <= 50; i++) {
    if (i % 5 === 0)
        console.log(i)
}
console.log("==================")


let evensum = 0
for (i = 0; i <= 100; i += 2) {
    evensum += i
}
console.log(evensum)
console.log("=========================")


let base = 2;
let exponent = 3;

let result = 1;

for (let i = 1; i <= exponent; i++) {
    result *= base;
}

console.log(`${base}^${exponent} = ${result}`);
``
console.log("==================")


for (i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0)
        console.log(i)
}


