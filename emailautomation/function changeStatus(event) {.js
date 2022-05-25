function changeStatus(event) {
    if ($p_ins_status == "Identified") {
      SETSTATUS('PIdentified');
    }
  
    else if ($p_ins_status == "Completed") {
      SETSTATUS('PCompleted');
    }
  
    else SETSTATUS('NONE');
  }