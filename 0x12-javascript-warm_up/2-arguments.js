#!/usr/bin/node
const len = process.argv.length;
if (len === 2) {
  console.log('No Argument');
} else if (len === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
