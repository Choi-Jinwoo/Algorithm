class Graph {
  constructor(size) {
    this.nodes = [];
    for (let i = 0; i < size; i++) {
      this.nodes[i] = new Node(i);
    }
  }

  addEdge(i1, i2) {
    const n1 = this.nodes[i1];
    const n2 = this.nodes[i2];

    if (!n1.adjacent.includes(n2)) {
      n1.adjacent.push(n2);
    }

    if (!n2.adjacent.includes(n1)) {
      n2.adjacent.push(n1);
    }
  }

  bfs(index) {
    const root = this.nodes[index];
    const queue = [];
    queue.push(root);
    root.visited = true;

    while (queue.length !== 0) {
      const r = queue.shift();
      for (const n of r.adjacent) {
        if (n.visited === false) {
          n.visited = true;
          queue.push(n);
        }
      }

      console.log(r.data);
    }
  }

  dfs(index) {
    const root = this.nodes[index];
    const stack = [];
    stack.push(root);
    root.visited = true;

    while (stack.length !== 0) {
      const r = stack.pop();
      for (const n of r.adjacent) {
        if (n.visited === false) {
          n.visited = true;
          stack.push(n);
        }
      }

      console.log(r.data);
    }
  }
}

class Node {
  constructor(data) {
    this.adjacent = [];
    this.visited = false;
    this.data = data;
  }
}

function main() {
}

const graph = new Graph(9);
graph.addEdge(0, 1)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(2, 4)
graph.addEdge(2, 3)
graph.addEdge(3, 4)
graph.addEdge(3, 5)
graph.addEdge(5, 6)
graph.addEdge(5, 7)
graph.addEdge(6, 8)
graph.bfs(0);