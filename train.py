import os
import random
import sys

import numpy as np
import tensorflow as tf
from conf.Parameter import Parameter

def main(argv):
    parameter = Parameter()
    print(parameter)
    print(argv)

if __name__ == "__main__":
    tf.app.run(main=main)