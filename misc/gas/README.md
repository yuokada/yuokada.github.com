## Overview

https://spreadsheets.google.com

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

### 範囲を取得して先頭から終わりまで一連の処理を実行する。
このコードを覚えてたらこの本の価値は取れてるってコード。

```
var rg      = sh.getDataRange(); <= データがある先頭を見つける。
var rows    = rg.getLastRow();   <= 最終行を取得
var values  = rg.getValues();    <= 先頭のデータを連想配列に代入
var mail_cc = Session.getActiveUser().getEmail();
for (var i = 1; i < rows; i++) {
    var mail_to = values[i][0];
    Browser.msgBox(mail_to);
    // MailApp.sendEmail(mail_to, subject, body, {
    //     cc: mail_cc
    // });
}
```

## 3-3
OK, キャンセルのダイアログの表示

```
Browser.msgBox("Do you  send a mail?", Browser.Buttons.OK_CANCEL);
```

## 3-4 ログ
スクリプトエディタの画面からログを確認できる。
```
Logger.log("Log start: " + Utilities.formatDate((new Date()), "JST", "yyyy/MM/dd HH:mm:ss"));
```

## 4-1

フォームを作ってデータを処理。


## Link

- [Spreadsheet Service  |  Apps Script  |  Google Developers](https://developers.google.com/apps-script/reference/spreadsheet/ "Spreadsheet Service  |  Apps Script  |  Google Developers")
  - [Tutorials  |  Apps Script  |  Google Developers](https://developers.google.com/apps-script/articles "Tutorials  |  Apps Script  |  Google Developers")
  - [URL Fetch Service  |  Apps Script  |  Google Developers](https://developers.google.com/apps-script/reference/url-fetch/ "URL Fetch Service  |  Apps Script  |  Google Developers")
- [「Google Appsでつくる仕事便利ツール」サポートサイト](https://book.mynavi.jp/support/pc/apps/ "「Google Appsでつくる仕事便利ツール」サポートサイト")

### Qiita
- [Google Apps Scriptの開発手法まとめ - Qiita](http://qiita.com/soundTricker/items/4d04c97c499b22886dfd "Google Apps Scriptの開発手法まとめ - Qiita")
- [GASのライブラリを使って楽したい① とりあえず使ってみる_(:3」∠)_ - Qiita](http://qiita.com/soundTricker/items/7bbd86425ae8d0641d50 "GASのライブラリを使って楽したい① とりあえず使ってみる_(:3」∠)_ - Qiita")


## MEMO

### 2017/02/19

- Underscore.js を使えることを知った。 細かい関数とかはこれでいけそう。
  http://qiita.com/soundTricker/items/4d04c97c499b22886dfd
  ```
  Underscore
  ライブラリKey: MGwgKN2Th03tJ5OdmlzB8KPxhMjh3Sh48
  JS用の汎用ライブラリ この名前で検索すれば結構解説が出てくるので解説はそちらに任せます。
  これもGoogleの中の人がGAS用に提供しなおしているものです。
  ```
    - [GASのライブラリを使って楽したい① とりあえず使ってみる_(:3」∠)_ - Qiita](http://qiita.com/soundTricker/items/7bbd86425ae8d0641d50 "GASのライブラリを使って楽したい① とりあえず使ってみる_(:3」∠)_ - Qiita")

- URLFetchAppを使ってみる。
  see: https://developers.google.com/apps-script/reference/url-fetch/url-fetch-app#fetch(String)
  ```
  var options = {
   'method' : 'post',
   'payload' : formData
  };
  UrlFetchApp.fetch('https://httpbin.org/post', options);
  ```
