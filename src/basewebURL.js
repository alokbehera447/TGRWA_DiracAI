let basewebURL;
let meetingbasewebURL;


if (window.location.host === "localhost:3000") {
  basewebURL = "http://127.0.0.1:8000";
  meetingbasewebURL = "http://localhost:3000";
}


/*
if (window.location.host === "localhost:3000") {
  basewebURL = "http://192.168.129.12:8000";
  meetingbasewebURL = "http://localhost:3000";
}
*/



if (window.location.host === "192.168.29.12:3000") {
  basewebURL = "http://192.168.29.12:8000";
  meetingbasewebURL = "http://localhost:3000";
}



if (window.location.host === "127.0.0.1:8000") {
  basewebURL = "http://127.0.0.1:8000";
  meetingbasewebURL = basewebURL;
}

if (window.location.host === "tgrwa.in") {
  basewebURL = "https://tgrwa.in";
  meetingbasewebURL = basewebURL;
}


export default basewebURL;

export { meetingbasewebURL };
