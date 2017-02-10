function onOpen() {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var menuEntries = [{
        name: "実行",
        functionName: "myFunction"
    }];
    ss.addMenu("拡張", menuEntries);
}

function myFunction() {
    var sh = SpreadsheetApp.getActiveSheet();
    var mail_to = sh.getRange("A2").getValue();
    // var subject = sh.getRange("B2").getValue();
    var subject = sh.getRange(2, 2).getValue();
    var body = sh.getRange("C2").getValue();

    var rg = sh.getDataRange();
    var rows = rg.getLastRow();
    var values = rg.getValues();
    var mail_cc = Session.getActiveUser().getEmail();
    for (var i = 1; i < rows; i++) {
        var mail_to = values[i][0];
        //    Browser.msgBox(mail_to);
        MailApp.sendEmail(mail_to, subject, body, {
            cc: mail_cc
        });
    }
    Browser.msgBox("Finish!");
}
