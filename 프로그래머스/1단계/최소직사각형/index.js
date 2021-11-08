function solution(sizes) {
  let width = 0;
  let height = 0;

  for (const [w, h] of sizes) {
    if (w < h) {
      width = width < h ? h : width;
      height = height < w ? w : height;
    } else {
      width = width < w ? w : width;
      height = height < h ? h : height;
    }
  }

  return width * height;
}
