
const socketio = io()

socketio.on('connect', () => {
  socketio.emit('event', {data: "this is my data"})
})
