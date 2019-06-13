#!/usr/bin/env python
# -*- coding: utf-8 -*-

# モデル操作に関する処理

import os
import glob


def model_compile(model, loss, optimizer):
    model.compile(loss=loss, optimizer=optimizer, metrics=["accuracy"])
    return


def model_load(model, model_folder, idx):
    model_files = glob.glob(os.path.join(
        model_folder, "weights_" + str(idx) + "_*"))
    model_fpath = model_files[-1]
    model.load_weights(model_fpath)
    return


def model_delete(model, model_folder, idx):
    model_files = glob.glob(os.path.join(
        model_folder, "weights_" + str(idx) + "_*"))
    for model_fpath in model_files[:-1]:
        os.remove(model_fpath)
    return