function onOpen() {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var menuEntries = [{
        name: "メール送信",
        functionName: "myFunction"
    }];
    ss.addMenu("拡張", menuEntries);
}

function myFunction() {
    var ret = Browser.msgBox("Do you  send a mail?", Browser.Buttons.YES_NO_CANCEL);
    if (ret == "yes") {
        Browser.msgBox("Finish!");
    } else if (ret == "no") {
        Browser.msgBox("No money Finish!");
    }
}
