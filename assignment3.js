// Question 1
console.log("Hello World");


// Question 2
let NAME = "Rahul";
let age = 20;
const city = "Rohtak";

console.log(NAME);
console.log(age);
console.log(city);


// Question 3
let num1 = 20;
let num2 = 30;

let sum = num1 + num2;
let sub = num2 - num1;
let mul = num1 * num2;
let div = num2 / num1;
console.log(sum);
console.log(sub);
console.log(mul);
console.log(div);


// Question 4
let a = 5;
const b = 10;
console.log(a);
console.log(b);


// Question 5
let marks = 75;
let greater = marks >= 40;
console.log(greater);


// Question 6
let num = 5;
let square = num ** 2;
console.log("Square of", num, "=", square);


// Question 7
let length = 10;
let breadth = 5;
let area = length * breadth;
console.log("Area of rectangle =", area);


// Question 8
let value = 14;
let remainder = value % 3;
console.log("Remainder =", remainder);


// Question 9
let course = "JavaScript";
let version = 6;
let isAvailable = true;
console.log(typeof course);
console.log(typeof version);
console.log(typeof isAvailable);


// Question 10
let obtainedMarks = 85;
let totalMarks = 100;
let percentage = (obtainedMarks / totalMarks) * 100;
console.log("Percentage =", percentage + "%");


// Question 11
let num3 = 7;

if (num3 % 2 === 0) {
    console.log("Even")
} else {
    console.log("Odd")
}


// Question 12
num = 20;

if (num > 0) {
    console.log("Positive number")
} else if (num < 0) {
    console.log("Negative number")
} else {
    console.log("Zero")
}


// Question 13
num1 = 45;
num2 = 50;

if (num1 > num2) {
    console.log(num1, "is greater")
} else if (num2 > num1) {
    console.log(num2, "is greater")
} else {
    console.log("Both are equal")
}


// Question 14
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


// Question 15
age = 18;

if (age >= 18) {
    console.log("Eligible for vote")
} else {
    console.log("Not eligible for vote")
}


// Question 16
for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0)
        console.log(i)
}


// Question 17
marks = 85

if (marks >= 90) {
    console.log("Grade A")
} else if (marks >= 80) {
    console.log("Grade B")
} else if (marks >= 70) {
    console.log("Grade C")
} else {
    console.log("Fail")
}


// Question 18
let year = 2024;
if (year % 4 === 0) {
    console.log(year, "is a leap year")
} else {
    console.log(year, "is not a leap year")
}


// Question 19
let amount = 2500;
let finalAmount;

if (amount >= 2000) {
    let discount = amount * 0.1;
    finalAmount = amount - discount;
    console.log("Final amount after discount:", finalAmount);
} else {
    console.log("No discount applied. Final amount:", amount);
}


// Question 20
num = 35;
if (num >= 10 && num <= 50) {
    console.log(num, "is between 10 and 50")
} else {
    console.log(num, "is not between 10 and 50")
}



