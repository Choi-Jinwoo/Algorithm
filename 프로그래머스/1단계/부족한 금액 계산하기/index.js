function solution(price, money, count) {
  let sum = 0;

  for (let i = 1; i < count + 1; i += 1) {
    sum += price * i;
  }

  return sum - money < 0 ? 0 : sum - money;
}
