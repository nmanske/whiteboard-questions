// Part 1

const fs = require('fs')
const path = require('path')

function calculateChecksum(file) {
  let ids = fs.readFileSync(file).toString().split('\n')
  let total = [0, 0]

  for (let line of ids) {
    let letters = {}
    for (let c of line) {
      if (letters[c]) letters[c] += 1
      else letters[c] = 1
    }
    if (Object.values(letters).includes(2)) total[0] += 1
    if (Object.values(letters).includes(3)) total[1] += 1
  }

  let checksum = total[0] * total[1]
  return checksum
}

let checksum = calculateChecksum(path.join(__dirname, 'day2.txt'))
console.log(checksum)

// Part 2

