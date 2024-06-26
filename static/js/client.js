const socket = io()

const input_message = document.getElementById("input")
const btn_send = document.querySelector(".button-send")
const ul_messages = document.getElementById("messages")
const username = document.getElementById("text-username")


function addMessage(msg){
  const container_messages = document.querySelector(".container-message").content.cloneNode(true)
  const p_username = container_messages.getElementById("username")
  const p_message =container_messages.getElementById("message")
  p_username.textContent = msg.username
  p_message.textContent = msg.message
  ul_messages.appendChild(container_messages)
}

btn_send.addEventListener('click', (e) => {
  e.preventDefault()
  const msg = input_message.value
  input_message.value = ""
  socket.emit("send-msg", {"message": msg, "username": username.textContent })
})

socket.on("recv-msg", (msg) => {
  addMessage(msg)
})
