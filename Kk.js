
const num = 8;
const obj = {
  num: 10,
  inner: {
    num: 6,
    getNum: function() {
      return this.num;
    }
  }
};
console.log(obj.inner.getNum());
const getNum = obj.inner.getNum;
console.log(getNum());
