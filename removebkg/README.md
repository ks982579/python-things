Thanks to https://www.tomshardware.com/how-to/python-remove-image-backgrounds

requirements:
```shell
pip install --upgrade Pillow
pip install rembg easygui
```

When saving the file, save it as a `*.png` to preserve the background removal.
It will take a minute to fire up and it should download some "u2net.onnx".

There are other ways to use the `rembg` package, see the [github README](https://github.com/danielgatis/rembg).