function telus() { 
    
    if(payload.data.send_to_telus) {
        sendTelusMail();
    }
}

function shaw(){
    if(payload.data.send_to_shaw) {
        sendShawMail();
    }
}

function sendTelusMail() {

    var record_id = payload.data.id;
    var user = payload.data.updated_by;
    var lat = payload.data.latitude;
    var lng = payload.data.longitude;
    var status = payload.data.status;

    var body = "<p>" +
    "<b>User: </b>" + user + "<br>" +
    "<b>Record Title: </b>" + title + "<br>" +
    "<b>Status:</b>" + status + "<br>" +
    "<b>Timestamp: </b>" + updated_at + "<br>" +
    "<b>Location: </b>" + latitude + "," + longitude + "<br>"
    
    window.location.href = 'mailto:esankar@nelson.ca?subject=Hello there&body=This is the body';

}

function sendShawMail() {

    var record_id = payload.data.id;
    var user = payload.data.updated_by;
    var lat = payload.data.latitude;
    var lng = payload.data.longitude;
    var status = payload.data.status;

    var body = "<p>" +
    "<b>User: </b>" + user + "<br>" +
    "<b>Record Title: </b>" + title + "<br>" +
    "<b>Status:</b>" + status + "<br>" +
    "<b>Timestamp: </b>" + updated_at + "<br>" +
    "<b>Location: </b>" + latitude + "," + longitude + "<br>"
    
    window.location.href = 'mailto:esankar@nelson.ca?subject=Nelson Hydro Issue&body=test';

}