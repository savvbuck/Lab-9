function updateGame(el){
    game_id = el.value
    fetch('/ready/' + game_id, {
        method: 'patch', 
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'ready': el.checked})
    })
}
function createGame(){
    let name = document.getElementById('name').value
    let year = document.getElementById('year').value
    fetch('/game', {
        method: 'post', 
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'name': name || 'Пустое', 'year': year || '0000', 'ready': false})
    })
}