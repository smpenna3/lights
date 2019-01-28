var socket = io.connect(location.origin + '/channel');

function send(){
    socket.emit('fade')
}