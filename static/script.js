const form = $('#form');
form.on('submit',checkData);

function checkData(){
    const allInputs = $("[type=text]");
    const fields = [];
    let not_empty_check = 0;
    let lessThan3Chars = 0;
    for(let i=0;i<allInputs.length;i++){
        fields.push(allInputs[i].name);
    }

    let i, l = fields.length;
    let fieldname;
    for (i = 0; i < l; i++) {
        fieldname = fields[i];
        const val = document.forms["form"][fieldname].value;
        if ( val!= "") {
            not_empty_check += 1;
        }
        if (val.length>=3) {
            lessThan3Chars += 1;
        }
    }

    if(not_empty_check < l) {
        alert("Some fields are missing...");
        e.preventDefault();
    }
    else if(lessThan3Chars < l){
        alert("Some fields should be at least 3 characters long...");
        e.preventDefault();
    }
}
