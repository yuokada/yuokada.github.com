function mySendMemo(e) {
    var mail_to = e.namedValues["連絡先"];
    var datetime = e.namedValues["日時"];
    var aite = e.namedValues["会社名・お名前"];
    var renraku = e.namedValues["連絡内容"];
    var shousai = e.namedValues["連絡詳細"];
    var bikou = e.namedValues["折り返し電話番号や補足"];
    var uke = e.namedValues["受けた人"];

    var subject = "【連絡メモ】" + aite + "様";
    var body = "◆日時：\n" + datetime + "\n\n";
    body = body + "◆会社名・お名前：\n" + aite + "様\n\n";
    body = body + "◆連絡内容：\n" + renraku + "\n\n";
    body = body + "◆連絡詳細：\n" + shousai + "\n\n";
    body = body + "◆折り返し電話番号や補足：\n" + bikou + "\n\n";
    body = body + "◆受けた人：\n" + uke + "\n\n";

    MailApp.sendEmail(mail_to, subject, body);
}
