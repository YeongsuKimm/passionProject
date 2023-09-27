// Copy your previous code to built alphabetList here
var alphabet = "abcdefghijklmnopqrstuvwxyz";
var alphabetList = [];

for (var i = 0; i < alphabet.length; i++) {
	alphabetList.push(alphabet[i]);
}

// console.log(alphabetList);
let letterNumber = 5

for (var i = 0; i < alphabetList.length; i++) {
	if (i == letterNumber) {
		console.log(alphabetList[i] + " is letter number " + String(i+1) + " in the alphabet")
	}
}

// Should output:
// "e" is letter number 5 in the alphabet