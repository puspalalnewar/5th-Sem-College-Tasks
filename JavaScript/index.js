let myName = "Puspalal Newar Tirtha "
const arr = myName.split(" ");
console.log(arr)
let firstEle = arr.map((ele)=> {
    return ele[0]
})
let convertToStr = firstEle.join("")

console.log(convertToStr)