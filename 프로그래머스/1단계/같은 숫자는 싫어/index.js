function solution(arr) {
  const stack = [];

  arr.forEach((item) => {
    if (stack.length === 0) {
      stack.push(item);
    } else if (stack[stack.length - 1] !== item) {
      stack.push(item);
    }
  });

  return stack;
}
