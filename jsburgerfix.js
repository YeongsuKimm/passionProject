var menu =  {"burger": 3.99,
         "fries": 1.99,
         "drink": 0.99}
var total = 0

//shows the user the menu and prompts them to select an item
console.log("Menu")
for (var item in menu) {
    console.log(item + "  $" + menu[item].toFixed(2)) //why is toFixed used?
}
//ideally the code should support mutliple items
var item = "burger"
var selection = "burger"
if (selection == item){
    // console.log(menu[selection])
    total += menu[selection]
}
else {
    console.log("Invalid Input")
}
//code should add the price of the menu items selected by the user 
console.log(total)