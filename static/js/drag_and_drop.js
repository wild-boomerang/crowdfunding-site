function readFile(input) {
    let boxZone = $(input).parent().parent().find('.preview-zone').find('.box').find('.box-body');
    boxZone.empty();
    document.getElementById("image-count").innerHTML = input.files.length;

    if (input.files && input.files[0]) {
        let wrapperZone = $(input).parent();
        let previewZone = $(input).parent().parent().find('.preview-zone');

        wrapperZone.removeClass('dragover');
        previewZone.removeClass('d-none');

        for (let i = 0; i < input.files.length; i++) {
            // if (!input.files[i].type.startsWith('image/')) {
            //     continue;
            // }

            let reader = new FileReader();

            reader.onload = function (e) {
                let htmlPreview =
                  '<div class="p-2"><img width="200" src="' + e.target.result + '" alt="' + input.files[i].name + '" />' +
                  '<p>' + input.files[i].name + '</p></div>';

                let boxZone = $(input).parent().parent().find('.preview-zone').find('.box').find('.box-body');
                boxZone.append(htmlPreview);
            };

            reader.readAsDataURL(input.files[i]);
        }
    }
}

$(".dropzone").change(function() {
    readFile(this);
});

window.addEventListener('load', function() {
    readFile(document.getElementsByClassName("dropzone")[0]);
});

$('.dropzone-wrapper').on('dragover', function(e) {
    e.preventDefault();
    e.stopPropagation();
    $(this).addClass('dragover');
});

$('.dropzone-wrapper').on('dragleave', function(e) {
    e.preventDefault();
    e.stopPropagation();
    $(this).removeClass('dragover');
});

function reset(e) {
    e.wrap('<form>').closest('form').get(0).reset();
    e.unwrap();
}

$('.remove-preview').on('click', function() {
    let boxZone = $(this).parents('.preview-zone').find('.box-body');
    let previewZone = $(this).parents('.preview-zone');
    // let dropzone = $(this).parents('.form-group').find('.dropzone');

    boxZone.empty();
    previewZone.addClass('d-none');

    document.getElementById("image-count").innerHTML = "";
    document.getElementsByClassName("dropzone")[0].value = "";
    // dropzone.value = '';
    // reset(dropzone);
});
