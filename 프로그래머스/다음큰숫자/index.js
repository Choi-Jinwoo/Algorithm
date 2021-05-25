function solution(n) {
  const binaryN = n.toString(2)

  for (var i = 1; i < binaryN.length; i += 1) {
    if (binaryN[i] == '0') {
      binaryN[i] = '1'
    }
  }

  for (var i = binaryN.length - 1; i += 1) {

  }
}


solution(78)