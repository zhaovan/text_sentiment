/**
* A basic Hello World function
* @param {string} name Who you're saying hello to
* @returns {string}
*/
module.exports = async (name = 'world', context) => {
  //return `hello ${name}`;
  var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "~/Github/textsentiment/sentiment/sentiment.py", true);
  xhttp.responseType = "JSON";
  xhttp.onload = function(e) {
    var arrOfStrings = JSON.parse(xhttp.response);
  }
  xhttp.send();
};
