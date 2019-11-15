function handleImageSelected(ev) {
    var tgt = ev.target;
    var files = tgt.files;
    if (files && files.length) {
        var fileReader = new FileReader();
        fileReader.onload = () => {
            document.getElementById("img-output").src = "";
            document.getElementById("img-input").src = fileReader.result;
        };
        fileReader.readAsDataURL(files[0]);
    }
}

function handleProcessButton(ev) {
    document.getElementById("img-output").src = "";
    pyodide.runPythonAsync(`process_image()`);
}

function handleClearButton(ev) {
    document.getElementById("img-input").src = "";
    document.getElementById("img-output").src = "";
}
