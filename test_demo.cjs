const assert=require('node:assert/strict');
const {run}=require('./docs/demo.js');
assert.equal(run({blocked:[]}).distance,22);assert.equal(run({blocked:[[1,0],[0,1]]}).path.length,0);assert.ok(!run({blocked:[[1,0]]}).path.some(p=>p[0]===1&&p[1]===0));
console.log('Browser demo behavior checks passed');
