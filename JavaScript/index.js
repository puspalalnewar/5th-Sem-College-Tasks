// let user = null;
// let name = user || "Guest";
// console.log(name); // "Guest"

// let user = {
//   profile: { name: "Puspalal" },
// };
// console.log(user.profile?.name); // "Puspalal"
// console.log(user.address?.city); // undefined (no error)

// function greet(name = "Puspalal") {
//   return `Hello, ${name}!`;
// }
// console.log(greet("John")); // Hello, Guest!

// let a = 5,
//   b = 10;
// [a, b] = [b, a];
// console.log(a, b); // 10 5

// console.log(!""); //Enter Strings
// console.log(!!!0);
// console.log(![]);

// let obj1 = {a:1, b:2, c : "Kuch v"};
// let obj2 = {b:3, c:4, d:"Hello"};
// let merged = {...obj1, ...obj2};
// console.log(merged); // {a:1, b:3, c:4}

// ! Check if Object is Empty
// let obj = {};
// console.log(Object.keys(obj).length === 0); // true
// Object.freeze(obj);
// console.log(Object.isFrozen(obj))

// ! Default Fallback with Nullish Coalescing (??)
// let userInput = null
// let val = userInput ?? "Default";
// console.log(val); // 0 (not "Default")

// ! Number to String & String to Number
// let num = 123;
// console.log(num + ""); // "123"
// console.log(+"123"); // 123

// Flatten Nested Arrays
// let arr = [1,50,[2, [3, [4]]]];
// console.log(arr.flat(3)); // [1,2,3,4]

// let str = "HeLLo WoRLd";
// let swapped = str.split("").map(ch =>
//   ch === ch.toUpperCase() ? ch.toLowerCase() : ch.toUpperCase()
// ).join("");
// console.log(swapped); // hEllO wOrlD

// const fetchData = async (url) => {
//   try {
//     let res = await fetch(url);
//     let data = await res.json();
//     console.log(data);
//   } catch (err) {
//     console.error("Error:", err);
//   }
// };

const arr = [1, 2, 3, 4, 5];

const chainedArr = arr.map((e)=>e).filter((e)=>e>2).reduce((acc , curr)=> acc * curr, 1)
console.log(chainedArr)

// arr.forEach(element => {
//     console.log(element)
// });

// console.log(arr.filter((ele) => ele > 2));


