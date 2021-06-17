# Split_Train_Test_YOLOv5

Split a directory of images into randomised train/test split. This also will generate a yaml file used by YOLOv5.

Input your image frames to a directory inside the directory `/input/`. Run main.py while specifying parameters to excecute split.

## Utilities:

### Perform Split
    
Input the image frames inside directory `/input/<name-of-your-set>/`.

Run main.py like this:


```
python main.py --srcDir /input/<name-of-your-set>/*.<ext-of-img> --rTrain <float between 0-1> --classes <input consecutive strings, eg. a b c> --seed <integer seed for split>
```

An example included with the script:
    
```
python main.py --srcDir input/example/*.tif --rTrain 0.8 --classes d --seed 100
```
    
Split will be outputted to `/output/<name-of-your-set>/`.

Images will be in `/output/<name-of-your-set>/<name-of-your-set>/images/<test/train>/` and there will be an empty label analogue created at `/output/<name-of-your-set>/<name-of-your-set>/labels/<test/train>/`.

The yaml file will be output to `/output/<name-of-your-set>/<name-of-your-set>.yaml`
