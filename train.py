import os
import random
import sys

import numpy as np
import tensorflow as tf
from .conf import Parameter

def main():
    parameter = Parameter()
    print(parameter)

if __name__ == "__main__":
    tf.app.run(main=main)