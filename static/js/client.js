const socketio = io()

const username = document.getElementById("appbar-username")
const btn_send = document.getElementById("btn-send")
const input_message = document.getElementById("input-message")
const template_message = document.getElementById("tmp-message")
const container_messages = document.querySelector(".messages")

const USER = username.textContent
const MESSAGES = []

function addMessage(message){
  const layout_message = template_message.content.cloneNode(true)
  const user = layout_message.getElementById("user")
  const msg = layout_message.getElementById("message")
  user.textContent = message.user
  msg.textContent = message.message
  container_messages.append(layout_message)
}

socketio.on('connect', () => {
  socketio.emit('event', {message: `${USER} vient de rejoindre le chat`})
})

btn_send.addEventListener('click', (e) =>{
  const msg = input_message.value
  input_message.value = ""
  if (msg){
    const message = {"user": USER, "message": msg }
    addMessage(message)
    socketio.emit("send-msg", message)
  }
})

socketio.on('recv-msg', (msg) => {
  addMessage(msg)
})

