from fastai.vision import *
from fastai.metrics import error_rate
from pathlib import Path
import argparse
import os


def main(path, batchsize, epochs):
    path = Path(path)
    path.resolve()
    tfms = get_transforms(do_flip=True, flip_vert=True)
    if batchsize:
        data = ImageDataBunch.from_folder(path, test="test", ds_tfms=tfms, bs=batchsize)
    else:
        data = ImageDataBunch.from_folder(path, test="test", ds_tfms=tfms, bs=4)
    learn = cnn_learner(data, models.resnet50, metrics=error_rate)
    if epochs:
        learn.fit_one_cycle(epochs)
    else:
        learn.fit_one_cycle(10)
    learn.export("model.pkl")

parser = argparse.ArgumentParser(description="CMD implementation of fastai v1")

parser.add_argument("Path", metavar="path", type=str, help="the path to list")
parser.add_argument("-b", "--batchsize", type=int, help="batch size,(4 by default)")
parser.add_argument("-e", "--epochs", type=int, help="number of epochs(10 by default)")
args = parser.parse_args()

if not os.path.isdir(args.Path):
    print("The path specified does not exist")
else:
    main(args.Path, args.batchsize, args.epochs)

