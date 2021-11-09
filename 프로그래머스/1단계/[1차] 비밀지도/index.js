function solution(n, arr1, arr2) {
  const result = [];
  for (let row = 0; row < n; row += 1) {
    let col = (arr1[row] | arr2[row]).toString(2).padStart(n, 0);

    col = col.replace(/0/g, " ");
    col = col.replace(/1/g, "#");

    result.push(col);
  }

  return result;
}
