#!/usr/bin/env python
#The Annotated Transformer v2022
#https://nlp.seas.harvard.edu/annotated-transformer

#prelims
from os.path import exists
import math, copy, time
from tkinter import N
from warnings import filterwarnings
import spacy, GPUtil
import pandas as pd
import altair as alt
import torch.nn as nn
from torch.nn.functional import log_softmax, pad
from torch.utiuls.data.distributed import DistributedSampler
import torch.distributed as dist
import torch.multiprocessing as mp
from torch.optim import Optimizer
from torch.nn.parallel import DistributedDataParallel as ddp
from torchtext.data.functional import to_map_style_dataset
from torch.utils.data import DataLoader
from torchtext.vocab import build_vocab_from_iterator
import torchtext.datasets as datasets

#set to false to skip notebook exec
filterwarnings("ignore")
RUN_EXAMPLES = True

#convinience helper
def is_interactive_notebook():
    return __name__ == "__main__"

def show_example(fn, args=[]):
    if __name__ == "__main__" and RUN_EXAMPLES:
        return fn(*args)

def execute_example(fn, args=[]) -> None:
    if __name__ == "__main__" and RUN_EXAMPLES:
        fn(*args)

class DummyOptimizer(Optimizer):

    def __init__(self) -> None:
        self.param_groups = [{"lr": 0}]

    def step(self) -> None:
    
    def zero_grad(self, set_to_none = False) -> None:

class DummyScheduler:
    
    def step(self) -> None:
        

#model architecture
#encoder and decoder stacks
def clones(module, N):
    return nn.ModuleList([copy.deepcopy(module for _ in range(N))])

class Encoder(nn.Module):

    def __init__(self) -> None:
        super().__init__()