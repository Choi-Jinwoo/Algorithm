// 'use strict';

// function search(maps, visited, y, x, dp) {
//   if (!(y >= 0 && y < maps.length && x >= 0 && x < maps[y].length)) return -1;
//   if (maps[y][x] === 0) return -1;
//   if (y === maps.length - 1 && x === maps[y].length - 1) {
//     return 1;
//   }

//   if (visited.find((item) => item[0] === y && item[1] === x) !== undefined) return -1;

//   visited.push([y, x]);
//   if (dp[y][x] !== 0) {
//     return dp[y][x];
//   }

//   const bottom = search(maps, [...visited], y + 1, x, dp);
//   const top = search(maps, [...visited], y - 1, x, dp);
//   const right = search(maps, [...visited], y, x + 1, dp);
//   const left = search(maps, [...visited], y, x - 1, dp);

//   if (bottom === -1 && top === -1 && right === -1 && left === -1) {
//     return -1;
//   }

//   const arr = [bottom, top, right, left].filter(e => e !== -1);
//   const result = Math.min(...arr);

//   dp[y][x] = result + 1;

//   return result + 1;
// }

// function solution(maps) {
//   const dp = maps.map((map) => {
//     return new Array(map.length).fill(0);
//   });
//   const data = search(maps, [], 0, 0, dp);

//   return data === -1 ? -1 : data;
// }

// console.log(solution([[0]]));

function solution(maps) {
  const search = [[0, 0, 0]];
  const maxY = maps.length;
  const maxX = maps[0].length;

  const visited = maps.map((map) => {
    return new Array(map.length).fill(false);
  });

  const next = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  while (search.length > 0) {
    const [x, y, cnt] = search.shift();

    if (visited[y][x]) {
      continue;
    }

    for (const n of next) {
      const nx = n[0] + x;
      const ny = n[1] + y;

      if (nx === maxX - 1 && ny === maxY) {
        return cnt + 1;
      }

      else if (nx < maxX && nx >= 0 && ny < maxY && ny >= 0 && maps[ny][nx] === 1) {
        search.push([nx, ny, cnt + 1]);
      }
    }

    visited[y][x] = true;
  }

  return -1;
}


console.log(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]));