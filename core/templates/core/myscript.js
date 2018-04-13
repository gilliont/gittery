debugger;
var nameList = [];
var choice = '';

function askOption() {
choice = prompt("Choose an option: add, remove, display, quit");
}

var start = prompt("Do you want to start the program? y/n");


if (start === 'y') {
askOption();
console.log('Added: ', choice);
while (choice === 'add' || 'remove' || 'display') {
    console.log('whiel choice: ', choice);
    if (choice === 'add') {
        var newNameAdd = prompt("Type a new name to add to the list:");
        if (newNameAdd.length > 0) {
            nameList.push(newNameAdd);
            console.log('Added: ', newNameAdd);
            askOption()
        }
        }
    else if (choice === 'remove'){
        var newNameRemove = prompt("Type an index to remove from the list:");
        delete nameList[newNameRemove];
        console.log('Removed: ', newNameRemove);
        askOption()
    }
    else if (choice === 'display'){
        console.log('Names: ', nameList);
        askOption()
    }
    else if (choice === 'quit'){
        console.log('Quited');
    }

}
}