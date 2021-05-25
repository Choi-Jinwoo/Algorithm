function solution(s) {
  const strNumbers = s.split(' ')
  const numbers = strNumbers.map(e => parseInt(e));

  const min = Math.min(...strNumbers)
  const max = Math.max(...strNumbers)

  return `${min} ${max}`
}