import nodeGypBuild from 'node-gyp-build'

const serial = nodeGypBuild('.')

//serial.write(0, Buffer.from('what?\n'))
//serial.write(0, 'what?\n')

//console.log(serial.read(1))

const fd = serial.open("/dev/ttyUSB0")

console.log(fd)
serial.write(fd, 'Kx')
console.log(serial.read(fd).toString())
serial.write(fd, 'E')
console.log(serial.read(fd).toString())
console.log(serial.close(fd))
