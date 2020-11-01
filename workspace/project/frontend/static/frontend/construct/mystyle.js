function setImage(target) {
    var reader = new FileReader();
    reader.onload = function (e) {
        document.getElementById("preview").setAttribute('src', e.target.result);
    }
    reader.readAsDataURL(target.files[0]);
};