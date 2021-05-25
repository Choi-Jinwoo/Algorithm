function Location(row, col) {
  this.row = row;
  this.col = col;
}

function bfs(map, isVisited) {
  const queue = [];
  queue.push(new Location(0, 0));
  isVisited[0][0] = 1;
}

function main(maps) {
  const isVisited = [
    [false, false, false, false, false, false],
    [false, false, false, false, false, false],
    [false, false, false, false, false, false],
    [false, false, false, false, false, false],
  ]
}

main(
  [
    [101111],
    [101010],
    [101011],
    [111011],
  ]
)