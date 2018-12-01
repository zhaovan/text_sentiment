// content.js
// chrome.runtime.onMessage.addListener(
//   function(request, sender, sendResponse) {
//     if( request.message === "clicked_browser_action" ) {
//       var firstHref = $("a[href^='http']").eq(0).attr("href");

//       console.log(firstHref);
//     }
//   }
// )

// var firstHref = $("a[href^='http']").eq(0).attr("href");

// var bglog = function(obj) {
// 	if(chrome && chrome.runtime) {
// 		chrome.runtime.sendMessage({type: "bglog", obj: obj});
// 	}
// }

// bglog(firstHref);

//alert("hello world");


// chrome.runtime.onMessage.addListener(
//   function(request, sender, sendResponse) {
//     if( request.message === "clicked_browser_action" ) {
//       var firstHref = $("a[href^='http']").eq(0).attr("href");

//       console.log(firstHref);
//     }
//   }
// );



// var elements = document.getElementsByTagName("div");

// var item1 = $('div._5rpb');
// console.log (item1);
// ==UserScript==
// @name        SampleScript
// @description Clear text of text inputs and write to console
// @author      Matt
// @include     *
// @version     0.1
// @grant       none
// @run-at      document-end
// ==/UserScript==



setInterval(function(){ console.log ("timeout");}, 3000);

var inputs = Array.prototype.slice.call(document.querySelectorAll('input, textarea, span'));

inputs.forEach(function(i) {

  	if (i.tagName.toLowerCase() == 'input' || i.tagName.toLowerCase() == 'textarea') {
      i.addEventListener("input", function(e) {
          e.preventDefault();
          console.log(e.target.value);
      });
    } else {
     	if (i.hasAttribute('data-text')) {
        i.addEventListener("change", function(e) {
          e.preventDefault();
          console.log(e.target.value);
      });
      }
    }
});




// for (var i = 0; i < elements.length; i++){
// 	var element = elements[i]

// 	console.log($("div"));
// 	// for (var j = 0; j < element.childNodes.length; j++){
// 	// 	var node = element.childNodes[j];
// 	// 	console.log(node);
// 	// }
// }
