function onOpen() {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var menuEntries = [];
    menuEntries.push({
        name: "実行",
        functionName: "myFunction"
    });
    menuEntries.push(null); // 線を引く
    menuEntries.push({
        name: "実行2",
        functionName: "myFunction2"
    });
    ss.addMenu("拡張", menuEntries);
}

function myFunction() {
    Browser.msgBox("Hello World!");
}

function myFunction2() {
    Browser.msgBox("Hello World2!");
}
