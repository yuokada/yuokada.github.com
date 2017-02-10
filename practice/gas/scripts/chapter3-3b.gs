function myFunction() {
  Logger.log("Log start: " + Utilities.formatDate((new Date()), "JST", "yyyy/MM/dd HH:mm:ss"));
  Browser.msgBox("Hello World!");
  Logger.log("Log end: " + Utilities.formatDate((new Date()), "JST", "yyyy/MM/dd HH:mm:ss"));
}
