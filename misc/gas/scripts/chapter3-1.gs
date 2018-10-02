function onOpen() {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var menuEntries = [{
        name: "実行",
        functionName: "myFunction"
    }];
    ss.addMenu("拡張", menuEntries);
}

function myFunction() {
    Browser.msgBox("Hello World2!");
}
