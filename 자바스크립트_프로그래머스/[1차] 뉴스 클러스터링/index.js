function splitStr(str) {
  const arr = [];

  let splitStr = '';
  for (const c of str) {
    if (!((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))) {
      splitStr = '';
      continue;
    }

    splitStr += c;
    if (splitStr.length >= 2) {
      arr.push(splitStr.toUpperCase());
      splitStr = c;
    }
  }

  return arr;
}

function calcUnion(arr1, arr2) {
  arr1 = [...arr1]
  arr2 = [...arr1]
  for (const item in arr1) {
    const idx = arr2.indexOf(item);
    idx !== -1 && arr2.splice(idx, 1);
  }

  const set = new Set([
    ...arr1,
    ...arr2,
  ]);

  return set.size;
}

function calcIntersect(arr1, arr2) {
  arr1 = [...arr1]
  arr2 = [...arr1]
  let count = 0;
  for (const item in arr1) {
    const idx = arr2.indexOf(item);
    if (idx !== -1) {
      arr2.splice(idx, 1);
      count += 1;
    }
  }

  return count;
}

function solution(str1, str2) {
  const splitStr1 = splitStr(str1);
  const splitStr2 = splitStr(str2);


  return (calcIntersect(splitStr1, splitStr2) / calcUnion(splitStr1, splitStr2) * 65536);
}

console.log(solution('FRANCE', 'french'));