import os
import random
import sys

import numpy as np
import tensorflow as tf
from conf.Parameter import Parameter

def create_hparams(flags):
    return tf.contrib.training.HParams(
       # Networks
      num_units=flags.num_units,
      num_layers=flags.num_layers,  # Compatible
      num_encoder_layers=(flags.num_encoder_layers or flags.num_layers),
      num_decoder_layers=(flags.num_decoder_layers or flags.num_layers),
      dropout=flags.dropout,
      unit_type=flags.unit_type,
      encoder_type=flags.encoder_type,
      residual=flags.residual,
      time_major=flags.time_major,
      num_embeddings_partitions=flags.num_embeddings_partitions,

      # Train
      optimizer=flags.optimizer,
      num_train_steps=flags.num_train_steps,
      batch_size=flags.batch_size,
      init_op=flags.init_op,
      init_weight=flags.init_weight,
      max_gradient_norm=flags.max_gradient_norm,
      learning_rate=flags.learning_rate,
      warmup_steps=flags.warmup_steps,
      warmup_scheme=flags.warmup_scheme,
      decay_scheme=flags.decay_scheme,
      colocate_gradients_with_ops=flags.colocate_gradients_with_ops)

def main(argv):
    parameter = Parameter()
    default_hparams = create_hparams(parameter)
    print(default_hparams)

if __name__ == "__main__":
    tf.app.run(main=main)