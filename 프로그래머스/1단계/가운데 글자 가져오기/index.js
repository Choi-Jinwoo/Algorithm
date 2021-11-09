function solution(s) {
  return s.length % 2 === 0
    ? s.slice(s.length / 2, s.length / 2 + 2)
    : s[Math.floor(s.length / 2)];
}
