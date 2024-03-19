
const obj = { a: 1, b: 2, c: 3 };
let result = "";
for (const [key, value] of Object.entries(obj)) {
  result += key + value;
}
console.log(result);
