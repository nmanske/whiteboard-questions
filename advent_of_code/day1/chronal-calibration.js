const { readFileSync } = require('fs')
const path = require('path')

function sumFrequencyChanges(file) {
  let frequency_changes = readFileSync(file).toString().split('\n')
  let sum = 0
  for (let i of frequency_changes) {
    sum += parseInt(i)
  }
  return sum
}

let frequency = sumFrequencyChanges(path.join(__dirname, 'day1.txt'))
console.log(frequency)
