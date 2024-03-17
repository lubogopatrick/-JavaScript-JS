
const string = "hello world";
const result = string.split("").filter((char, index) => index % 2 === 0).join("");
console.log(result);
