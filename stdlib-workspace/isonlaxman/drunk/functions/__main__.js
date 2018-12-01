var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

/**
* A basic Hello World function
* @param {string} url 
* @returns {object}
*/

module.exports = async (url = 'world', context) => {
  var xmlhttp;
  xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", url, true);
  return xmlhttp;
};
