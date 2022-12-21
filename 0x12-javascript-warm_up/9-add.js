#!/usr/bin/node
function add (a, b) {
  if (Number(process.argv[2] === undefined || process.argv[3]) === undefined) {
    console.log(NaN);
  }
  console.log(Number(process.argv[2]) + Number(process.argv[3]));
}
add();
