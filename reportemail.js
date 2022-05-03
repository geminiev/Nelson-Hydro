// Special Apps Script function to process HTTP POST request
function doPost(e){
    return handleResponse(e);
  }
  
  function handleResponse(e) {
  
    // Parse JSON webhook payload
    var jsonString = e.postData.getDataAsString();
    var payload = JSON.parse(jsonString);
  
    var formId = "12e4ebfc-e023-400b-90ec-db353bf7ebcc";
    var sendTo = "esankar@nelson.ca";
    var title = payload.data.form_values["https://api.fulcrumapp.com/api/v2/forms/12e4ebfc-e023-400b-90ec-db353bf7ebcc.json?token=dbe0b686a36f83a30816a0771d935c2e42a95c4398b40baf0098af982719f23a1ee8efb9208fc348"]; // https://api.fulcrumapp.com/api/v2/forms/YOUR-FORM-ID.json?token=YOUR-TOKEN
    var record_id = payload.data.id;
    var user = payload.data.updated_by;
    var lat = payload.data.latitude;
    var lng = payload.data.longitude;
    // Note: Starting June 11, 2018: All Google Maps Platform API requests must include an API key! More info at https://developers.google.com/maps/documentation/maps-static/intro
    var mapURL = "http://maps.googleapis.com/maps/api/staticmap?center="+lat+","+lng+"&zoom=15&size=300x300&maptype=hybrid&markers=color:red%7C"+lat+","+lng+"&key=dbe0b686a36f83a30816a0771d935c2e42a95c4398b40baf0098af982719f23a1ee8efb9208fc348";
    var updated_at = isoToDate(payload.data.updated_at);
    var subject = "";
  
    // Make sure it's the form we want
    if (payload.data.form_id === formId) {
      // What type of event is it?
      if (payload.type === "record.create") {
        subject = "New Fulcrum record created";
      } else if (payload.type === "record.update") {
        subject = "Fulcrum record updated";
      } else if (payload.type === "record.delete") {
        subject = "Fulcrum record deleted";
      }
      // Send email notification
      sendMail();
    }
  
    function sendMail() {
      // Build email body
      var body = "<p>" +
                    "<b>User: </b>" + user + "<br>" +
                    "<b>Record Title: </b>" + title + "<br>" +
                    "<b>Record ID: </b><a href=\"https://web.fulcrumapp.com/records/" + record_id + "\">" + record_id + "</a><br>" +
                    "<b>Timestamp: </b>" + updated_at + "<br>" +
                    "<p><a href='https://web.fulcrumapp.com/records/" + record_id + "' title='Open in Fulcrum'><img src='" + mapURL + "'></a></p>" +
                  "</p>";
  
      MailApp.sendEmail({
        to: sendTo,
        subject: subject,
        htmlBody: body
      });
    }
  }
  
  // Apps Script can't seem to handle ISO 8601 dates- http://stackoverflow.com/questions/11810441/how-do-i-format-this-date-string-so-that-google-scripts-recognizes-it
  function isoToDate(dateStr) { // argument = date string iso format
    var str = dateStr.replace(/-/, '/').replace(/-/, '/').replace(/T/, ' ').replace(/\+/, ' \+').replace(/Z/, ' +00');
    return new Date(str);
  }