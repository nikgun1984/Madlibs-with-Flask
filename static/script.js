const storyForm = $('#form');
const createStoryForm = $('#create');
storyForm.on('submit',areInputsValid);
createStoryForm.on('submit',isCreateStoryFormValid);

function areInputsValid() {
    let isFormValid = true,
        isNoLessThan3 = true,
        warning1, warning2;
    $("#form input").each(function(){
        if (!$.trim($(this).val()).length){
            warning1 = 'Please fill up all the input fields...'
            isFormValid = isOn($(this),isFormValid);
        }
        else{
            $(this).removeClass("highlight");
        }

        if ($.trim($(this).val()).length < 3 && $.trim($(this).val()).length){
            warning2 = 'Secret word should be at least 3 characters...'
            isNoLessThan3 = isOn($(this),isNoLessThan3);
        }
        else{
            $(this).removeClass("highlight");
        }
        });

        if (!isFormValid) { 
            alert(warning1);
        }

        if (!isNoLessThan3) { 
            alert(warning2);
        }

    return isFormValid && isNoLessThan3;
}  

function isCreateStoryFormValid() {
    let isTitleValid = true,
        isTextAreaValid = true,
        warning1,warning2;
    //Checking title input if it is empty
    const title = $('input#title').val();
    if(!$.trim(title).length) {
        warning1 = "Please add your story title..."
        isTitleValid = isOn($('input#title'),isTitleValid);
    } else {
        $('input#title').removeClass("highlight");
    }
    // Checking the textarea if it is empty or no secret words input
    const textArea = $('textarea').val();
    const regexp = /(?!=\{)\w+[\s\w+]*(?=\})/g;
    arr = textArea.match(regexp) || [];
    if(!arr.length && $.trim(textArea).length){
        warning2 = "Please enter at least one secret word..."
        isTextAreaValid = isOn($('textarea'),isTextAreaValid);
    } else if(!$.trim(textArea).length || textArea == '') {
        warning2 = "Text area is empty..."
        isTextAreaValid = isOn($('textarea'),isTextAreaValid);
    } else {
        $('textarea').removeClass("highlight");
    }

    // Make a warning if wrong or no input
    if(!isTextAreaValid) {
        alert(warning2);
    }

    if(!isTitleValid) {
        alert(warning1);
    }
    return isTextAreaValid && isTitleValid;
}

/* this will return boolean if input is invalid which is false*/
function isOn(input,isInputValid){
    input.addClass("highlight");
    isInputValid = false;
    input.focus();
    return isInputValid;
}

/*message will disappear after few seconds*/
$(document).ready(function(){
    $(".flash").delay(2000).slideUp(300);
});