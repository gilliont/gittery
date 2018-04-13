console.log("Connected.");
var restart = document.querySelector("#restart");
var squares = document.querySelectorAll("td");


function clearBoxes() {
    console.log("clearBoxes reached.");
    console.log('squares.length', squares.length);
    for (var i = 0; i < squares.length; i+=1){
        squares[i].textContent = ""
    }
}


restart.addEventListener('click', clearBoxes);

$('td').click(function () {
   // var td = this.id;
   // console.log("td", td);
   if (this.textContent === "") {
       this.textContent = "X"
   }
   else if (this.textContent === "X"){
       this.textContent = "O"
   }
   else if (this.textContent === "O"){
       this.textContent = ""
   }
});