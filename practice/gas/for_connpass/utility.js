// curl -s https://connpass.com/api/v1/event/?nickname=yudai_nakayama&cont=100
function getUserInfo(nickname){
  var base_url = 'https://connpass.com/api/v1/event/';
  var options = ["nickname=" + nickname, "count=100"];
  fetch_url = base_url + "?" + options.join("&");
  var response = UrlFetchApp.fetch(fetch_url);
  var response_json = response.getContentText();
  Browser.msgBox("results_available is" + response_json["results_available"]);
}

// Make a POST request with a JSON payload.
var data = {
  'name': 'Bob Smith',
  'age': 35,
  'pets': ['fido', 'fluffy']
};
var options = {
  'method' : 'post',
  'contentType': 'application/json',
  // Convert the JavaScript object to a JSON string.
  'payload' : JSON.stringify(data)
};
UrlFetchApp.fetch('https://httpbin.org/post', options);
