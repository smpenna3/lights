var socket = io.connect(location.origin + '/channel');

function fade(){
    socket.emit('fade')
}