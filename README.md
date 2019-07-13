RGB Image Analysis with Python
==============================

This is a fork of Mark Solter's [rainbow-vision](https://github.com/msolters/rainbow-vision).

Decompose an image file into a 3D color-space visualization

usage:

```console

# --- interactive (default)

foo@bar:~$ visualize_colors.py thedress.jpg 

# --- non-interactive

foo@bar:~$ visualize_colors.py thedress.jpg thedress.analysis.png
foo@bar:~$ feh thedress.analysis.png
```

<img src="thedress.jpg" width="48%"></img>
<img src="thedress.analysis.png" width="48%"></img>


literature
----------

    - [RGB Image Analysis with Python](http://marksolters.com/programming/2015/02/27/rgb-histograph.html) by Martin Solters.
    - [The incredibly challenging task of sorting colours](https://www.alanzucconi.com/2015/09/30/colour-sorting/)


changelog
---------

**0.2.0**

    - fixes: does not work with Python3
    - adds arguments-support: me.py <image_in> [<image_out>]
    - adds doc
