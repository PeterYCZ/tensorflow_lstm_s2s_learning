"""set parameters of netual network"""

class Parameter(object):
    def __init__(self):
        #default
        #network
        self.num_units = 32
        self.num_layers = 2
        self.num_encoder_layers = None
        self.num_decoder_layers = None
        self.unit_type = 'lstm'
        self.encoder_type = 'uni'
        self.residual = False
        self.time_major = False
        self.num_embeddings_partitions = 0
        self.dropout = 0.2
        #train
        self.optimizer = 'sgd',
        self.num_train_steps = 12000,
        self.batch_size = 128,
        self.init_op = 'uniform',
        self.init_weight = 0.1,
        self.max_gradient_norm = 5.0,
        self.learning_rate=1.0,
        self.warmup_steps = 0,
        self.warmup_scheme = "t2t",
        self.decay_scheme = "",
        self.colocate_gradients_with_ops = True,
        #users set parameter
        self.set_parameter()

    def set_parameter(self):
        with open('./conf/neural_network.conf', 'r') as f:
            for eachline in f:
                this_line = eachline.strip().split(" ")
                if this_line[0][0] != '#':
                    if 'num_units' == this_line[0]:
                        self.num_units = int(this_line[1])
                    if 'num_layers' == this_line[0]:
                        self.num_layers = int(this_line[1])
                    if 'num_encoder_layers' == this_line[0] and this_line[1] != 'None':
                        self.num_encoder_layers = int(this_line[1])
                    if 'num_decoder_layers' == this_line[0] and this_line[1] != 'None':
                        self.num_decoder_layers = int(this_line[1])
                    if 'encoder_type' == this_line[0]:
                        self.encoder_type = this_line[1]
                    if 'residual' == this_line[0] and this_line[1] == 'True':
                        self.residual = True
                    if 'time_major' == this_line[0] and this_line[1] == 'True':
                        self.time_major = True
                    if 'num_embeddings_partitions' == this_line[0]:
                        self.num_embeddings_partitions = int(this_line[1])


