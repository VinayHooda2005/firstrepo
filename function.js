// Simple function

function sayHello() {
    console.log("Hello, World!");
}
sayHello();


// Method : function inside object

const person = {
    name: "Vinay",

    greet: function () {
        console.log("Hello, " + this.name);
    }
};

person.greet();


// Method : function outside object

function getGrade(marks) {
    if (marks < 0 || marks > 100) {
        return "Invalid marks";
    }
    if (marks >= 90) {
        return "A";
    } else if (marks >= 80) {
        return "B";
    } else {
        return "C";
    }
}
console.log(getGrade(85));


// function with parameters and return value

function total(a, b) {
    return a + b;
}
console.log(total(5, 10));


// function stored in variable

const multiply = function (x, y) {
    return x * y;
};
console.log(multiply(5, 10));


// Arrow function

const divide = (x, y) => x / y;

console.log(divide(10, 2));


// function with default parameters

function greet(name = "Guest") {
    console.log("Hello, " + name);
}
greet();
greet("Vinay Hooda");


// anonymous function

setTimeout(function () {
    console.log("This is an anonymous function");
}, 2000);
