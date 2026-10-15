// Question 21
for (let i = 1; i <= 50; i++) {
    console.log(i)
}


// Question 22
let i = 50;
while (i >= 1) {
    console.log(i);
    i--;
}


// Question 23
for (let i = 2; i <= 100; i += 2) {
    console.log(i);
}


// Question 24
for (let i = 1; i <= 50; i += 2) {
    console.log(i);
}


// Question 25
NUM = 7;
for (i = 1; i <= 10; i++) {
    console.log(`${NUM} * ${i} = ${NUM * i}`)
}


// Question 26
let sum = 0;
for (i = 1; i <= 100; i++) {
    sum = sum + i
}
console.log("Sum of numbers from 1 to 100 =", sum)


// Question 27
let evensum = 0;
for (i = 2; i <= 50; i += 2) {
    evensum += i
}
console.log("Sum of even number from 1 to 50 =", evensum)


// Question 28
let count = 0;
for (i = 1; i <= 100; i++) {
    if (i % 5 === 0)
        count += 1
}
console.log(count, " = that are divisible by 5 between 1 and 100")


// Question 29
for (i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0)
        console.log(i)
}


// Question 30
let num = 5
let factorial = 1;
for (i = 1; i <= num; i++) {
    factorial *= i

}
console.log("Factorial = ", factorial)