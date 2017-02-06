
## 3-1 onOpen()

シートを開いたときに自動的に実行される関数。
スプレッドシートを開いたときにメニューバーに"拡張"というタブを差し込む例。


- [Class Spreadsheet  |  Apps Script  |  Google Developers](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#addMenu(String,Object)

## 3-2 メール送信

現在のユーザーのメールアドレスを入手してCCに入れて送信する方法まで。

see: [Class Session  |  Apps Script  |  Google Developers](https://developers.google.com/apps-script/reference/base/session "Class Session  |  Apps Script  |  Google Developers")

レンジ処理のコード。これはいろいろ使えるので覚えておきたい。
```
var sh = SpreadsheetApp.getActiveSheet();
var mail_to = sh.getRange("A2").getValue();
// var subject = sh.getRange("B2").getValue();
var subject = sh.getRange(2, 2).getValue();
var body = sh.getRange("C2").getValue();
```

## 3-3
OK, キャンセルのダイアログの表示

```
Browser.msgBox("Do you  send a mail?", Browser.Buttons.OK_CANCEL);
```

## 3-4 ログ

スクリプトエディタの画面からログを確認できる。


## 4-1

フォームを作ってデータを処理。


## Link

- [Spreadsheet Service  |  Apps Script  |  Google Developers](https://developers.google.com/apps-script/reference/spreadsheet/ "Spreadsheet Service  |  Apps Script  |  Google Developers")
- [「Google Appsでつくる仕事便利ツール」サポートサイト](https://book.mynavi.jp/support/pc/apps/ "「Google Appsでつくる仕事便利ツール」サポートサイト")
