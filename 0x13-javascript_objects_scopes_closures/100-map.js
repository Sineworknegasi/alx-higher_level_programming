#!/usr/bin/node
const list = require('./100-date').list;
console.log(list);
const mapped = list.map((n, i) => n * i);
console.log(mapped);
