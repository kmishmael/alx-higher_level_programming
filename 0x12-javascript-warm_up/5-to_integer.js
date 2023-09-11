#!/usr/bin/node
if (typeof parseInt(process.argv[2]) !== 'number' || isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(process.argv[2])}`);
}
