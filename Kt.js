
const obj = {
  value: 42,
  getValue: function() {
    return () => {
      console.log(this.value);
    };
  }
};

const getValue = obj.getValue();
getValue();
