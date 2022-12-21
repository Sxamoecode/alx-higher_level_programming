#!/usr/bin/node
let num = Math.floor(process.argv[2])
console.log(isNaN(num) ? 'Not a number' : `my number: ${process.argv[2]}`);
