

var firstName = prompt("Please give your First Name.")
var lastName = prompt("Please give your Last Name.")
var age = prompt("Please give your age.")
var pet_name = prompt("Please give your pet's name.")
console.log('firstName',firstName);
console.log('lastName',lastName);
console.log('age',age);
console.log('pet_name',pet_name);

firstNameFirstLetter = firstName[0];
lastNameFirstLetter = lastName[0];
petNameLastLetter = pet_name.slice(-1);
int_age = parseInt(age);
console.log('firstNameFirstLetter',firstNameFirstLetter);
console.log('lastNameFirstLetter',lastNameFirstLetter);
console.log('petNameLastLetter',petNameLastLetter);
console.log('int_age',int_age);

if (firstNameFirstLetter === lastNameFirstLetter && petNameLastLetter === 'y' && 20 < int_age < 30) {
    mymessage = 'Welcome Comrade'
} else {
    mymessage = "Entries successfully saved"
}
console.log('Success: ',mymessage);

