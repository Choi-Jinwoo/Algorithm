function solution(a, b) {
  const [max, min] = a < b ? [b, a] : [a, b];

  let result = 0;
  for (let i = min; i <= max; i += 1) {
    result += i;
  }

  return result;
}
