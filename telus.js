function needMail(event) { 
    
    if(event.send_to_telus || event.send_to_shaw) {
        sendMail(event);
    }
}

function sendMail(event) {

    var problem = event.short_problem_description;
    var status = event.status;
    var title = event.title
    var updated_at = event.time

    var body = "<p>" +
    "<b>User: </b>" + USERFULLNAME + "<br>" +
    "<b>Title: </b>" + title + "<br>" +
    "<b>Problem: </b>" + problem + "<br>" +
    "<b>Status:</b>" + status + "<br>" +
    "<b>Timestamp: </b>" + updated_at + "<br>" +
    "<b>Location: </b>" + LATITUDE + "," + LONGITUDE + "<br>"
    
    who_to(event);
    return;
}

function who_to(event) {
  if (event.send_to_shaw) {
    window.location.assign('mailto:esankar@nelson.ca?subject=Hello there&body=This is the body'); // test content
  }

  if (event.send_to_telus) {
    window.location.assign('mailto:esankar@nelson.ca?subject=Hello there&body=This is the body');
  }
}