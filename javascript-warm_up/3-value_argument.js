#!/usr/bin/node
if (!process.argv[2]) {
    console.log('No argument');
    return;
}
console.log(process.argv[2]);
