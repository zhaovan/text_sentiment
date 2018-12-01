/**
* A basic Hello World function
* @param {string} name Who you're saying hello to
* @returns {string}
*/
module.exports = async (name = 'world', context, callback) => {

  var PythonShell = require('python-shell');
  let pyshell = new PythonShell('test.py');

  pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    // console.log(message);

    return message;
  });
};
