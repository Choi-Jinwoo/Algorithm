function targetNumber(total, numbers, target) {
  if (numbers.length === 0) {
    if (total === target) {
      return 1;
    }

    return 0;
  }

  return targetNumber(numbers[0] + total, numbers.slice(1, numbers.length), target)
    + targetNumber(total - numbers[0], numbers.slice(1, numbers.length), target);
}

function solution(numbers, target) {
  return targetNumber(0, numbers, target)
}