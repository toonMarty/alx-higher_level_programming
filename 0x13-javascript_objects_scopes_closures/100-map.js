#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map((val, e) => val * e);
console.log(newList);
