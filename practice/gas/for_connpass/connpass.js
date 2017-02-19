function onOpen() {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var menuEntries = [{
        name: "実行",
        functionName: "main"
    }];
    ss.addMenu("拡張", menuEntries);
}


function getRecentEvents(nn) {
    var base_url = "https://connpass.com/api/v1/event/";
    var params = ["nickname=ian", "order=3", "count=100", "event_id=45985"];
    var params = ["nickname=" + nn, "order=3", "count=100", "ym=201701,201702,201703"];
    var fetch_url = base_url + "?" + params.join("&");
    var response_json = UrlFetchApp.fetch(fetch_url);

    var response = JSON.parse(
        response_json.getContentText());
    // Browser.msgBox("results_available is" + response["results_available"]);
    return response["results_available"];
}


function main() {
    var ss = SpreadsheetApp.getActiveSheet();
    var range = ss.getDataRange();
    //var range = ss.getRange("A2");
    var last_row = range.getLastRow();
    // Browser.msgBox("last_row is " + last_row);
    var values = range.getValues();

    var recent_events = [];
    for each(v in values) {
        if (v[0] == "Users") { // 見出し行のスキップ
        recent_events.push(["Users", "recent events"]);

            continue;
        }
        var row = [v[0], getRecentEvents(v[0])];
        recent_events.push(row);
    }
    var srange = ss.getDataRange();
    srange.setValues(recent_events);
//    Browser.msgBox(recent_events.join("    \n"));
}
