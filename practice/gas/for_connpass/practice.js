function main2() {
    var ss = SpreadsheetApp.getActiveSheet();
    var range = ss.getDataRange();
    var last_row = range.getLastRow();
    var values = range.getValues();

    var recent_events = [];
    for each(v in values) {
        if (v[0] == "Users") { // 見出し行のスキップ
            continue;
        }
        var row = [Math.random() * 100];
        recent_events.push(row);
    }
    // B2から終わりの行までの範囲を取得して値をセット
    var srange = ss.getRange(2, 2, last_row - 1, 1);
    Logger.log(srange.getValues());
    srange.setValue(recent_events);
}
