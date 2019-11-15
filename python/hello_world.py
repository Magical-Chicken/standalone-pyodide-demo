import base64
import js
import io
import sys
import numpy as np
import matplotlib
import matplotlib.image as mpimg

DATA_PREFIX = "data:image/png;base64,"


def process_image():
    image_data_url = js.document.getElementById("img-input").src
    if image_data_url is None or not image_data_url.startswith("data:"):
        js.window.alert("no image data loaded")
        return
    if not image_data_url.startswith(DATA_PREFIX):
        js.window.alert("invalid image data, only support PNG")
        return
    image_data = base64.b64decode(image_data_url[len(DATA_PREFIX):])
    js.console.log(f"python read raw image data ok, length: {len(image_data)}")
    img = mpimg.imread(io.BytesIO(image_data))
    js.console.log(f"image contents loaded successfully, np array shape: {img.shape} dtype: {img.dtype} range [{img.min()}, {img.max()}]")
    img = img + (np.random.rand(*img.shape) * 0.1) - 0.5
    out_fp = io.BytesIO()
    mpimg.imsave(out_fp, img)
    output_data = DATA_PREFIX + base64.b64encode(out_fp.getvalue()).decode()
    js.console.log("generated updated image, writing output data")
    js.document.getElementById("img-output").src = output_data


def show_loaded_message():
    version_info = {
        "python": sys.version.split("(")[0].strip(),
        "pyodide": js.pyodide.version(),
        "numpy": np.__version__,
        "matplotlib": matplotlib.__version__,
    }
    version_info_str = ", ".join([f"{k}: {v}" for k, v in version_info.items()])
    message = f"Python initialization complete, loaded versions: [{version_info_str}]"
    js.document.getElementById("p-python-loaded-message").innerHTML = message


def main(*args):
    show_loaded_message()


def bootstrap():
    main()
