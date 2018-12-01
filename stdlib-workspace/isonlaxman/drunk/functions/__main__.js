// var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var spawn = require('child_process').spawn;

/**
* A basic Hello World function
* @param {string} arg
* @returns {object}
*/

module.exports = async (arg = "John", context) => {
  // var xmlhttp;
  // xmlhttp = new XMLHttpRequest();
  //
  // // var params = JSON.stringify({}
  // xmlhttp.open("POST", "test.py?word=" + arg, true);
  // xmlhttp.responseType = "JSON";
  // xmlhttp.onload = function(e) {
  //   var arrOfStrings = JSON.parse(xmlhttp.response);
  // }
  // xmlhttp.send();
  // return xmlhttp;

  var pythonP = spawn('python', ['test.py']);
  pythonP.stdout.on('data', (data) => {
    return data;
  })
};
