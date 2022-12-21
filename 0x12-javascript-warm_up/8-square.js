#!/usr/bin/node
const num = Number(process.argv[2]);
if (isNaN(num) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('x');
    }
    console.log();
  }
}
