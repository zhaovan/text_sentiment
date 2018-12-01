// background.js

// Called when the user clicks on the browser action.
chrome.browserAction.onClicked.addListener(function(tab) {

	// reloads stuff
	localStorage.tabToReload = tab.id;
    chrome.runtime.reload();


	// Send a message to the active tab
	chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
	
	var activeTab = tabs[0];
	chrome.tabs.sendMessage(activeTab.id, {"message": "clicked_browser_action"});
	});
});


function reloadTab() {
    var tabID = localStorage.tabToReload;
    if (tabID) {
        chrome.tabs.reload(parseInt(tabID));
        delete(localStorage.tabToReload);
    }
}
reloadTab();