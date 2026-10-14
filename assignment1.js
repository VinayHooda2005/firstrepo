let names = "Vinay Hooda"
let age = 21
let city = "Rohtak"

console.log("Name =", names)
console.log("Age =", age)
console.log("City =", city)
console.log("==================")


let a = 15
let b = 5

console.log(a + b)
console.log(a - b)
console.log(a * b)
console.log("=================")


let num = 7

if (num % 2 === 0) {
    console.log("Even")
} else {
    console.log("Odd")
}
console.log("=====================")


age = 18;

if (age >= 18) {
    console.log("Eligible for vote")
} else {
    console.log("Not eligible for vote")
}
console.log("=======================")


let num1 = 45
let num2 = 45

if (num1 > num2) {
    console.log(num1, "is greater")
} else if (num2 > num1) {
    console.log(num2, "is greater")
} else {
    console.log("Both are equal")
}
console.log("=======================")


console.log("10" + 5)
console.log("10" - 5)
console.log(10 == "10")
console.log(10 === "10")
console.log("=====================")


let x = 5

console.log(x++)
console.log(++x)
console.log(x)
console.log("=====================")


num = 20

if (num > 0) {
    console.log("Positive number")
} else if (num < 0) {
    console.log("Negative number")
} else {
    console.log("Zero")
}
console.log("================")


let t = 49
let u = 37
let v = 56

if (t >= u && t >= v) {
    console.log(t, "is greater")
} else if (u >= t && u >= v) {
    console.log(u, "is greater")
} else {
    console.log(v, "is greater")
}
console.log("=======================")


let marks = 85

if (marks >= 90) {
    console.log("Grade A")
} else if (marks >= 80) {
    console.log("Grade B")
} else if (marks >= 70) {
    console.log("Grade C")
} else {
    console.log("Fail")
}
console.log("===================")


for (let i = 1; i <= 10; i++) {
    console.log(i)
}


for (let i = 1; i <= 20; i++) {
    if (i % 2 === 0)
        console.log(i)
}


for (let i = 1; i <= 15; i++) {
    if (i % 2 !== 0)
        console.log(i)
}


let number = 7

for (let i = 1; i <= 10; i++) {
    console.log(`${number} * ${i} = ${number * i}`)
}

let sum = 0
for (i = 1; i <= 10; i++) {
    sum = sum + i
}
console.log("Sum =", sum)


