// yeah i know this isn't pretty but i'm definitely not an expert on the java scripts
function pythonLauncher() {
    languagePluginLoader.then(() => {
        console.log(pyodide.runPython(`import sys\nsys.version`));
        var req = new XMLHttpRequest();
        req.open("GET", "python/hello_world.py");
        req.addEventListener("load", () => {
            if (req.status != 200) {
                console.error("failed to retrieve script");
            } else {
                pyodide.loadPackage(["micropip", "numpy", "matplotlib"]).then(() => {
                    pyodide.runPythonAsync(req.responseText).then(() => {
                        pyodide.runPythonAsync(`bootstrap()`);
                    });
                });
            }
        });
        req.send();
    });
}
