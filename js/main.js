function handleImageSelected(ev) {
    var tgt = ev.target;
    var files = tgt.files;
    if (files && files.length) {
        var fileReader = new FileReader();
        fileReader.onload = () => {
            // clear output contents
            document.getElementById("img-output").src = null;
            // set preview window contents
            document.getElementById("img-input").src = fileReader.result;
            // inform python land image is ready
            pyodide.runPythonAsync(`handle_image_loaded()`);
        };
        fileReader.readAsDataURL(files[0]);
    }
}
