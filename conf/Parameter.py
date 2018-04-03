"""set parameters of netual network"""

class paramster(object):
    def __init__(self):
        #default
        self.num_units = 32
        self.num_layers = 2
        self.num_encoder_layers = None
        self.num_decoder_layers = None
        self.encoder_type = 'uni'
        self.residual = False
        self.time_major = False
        self.num_embeddings_partitions = 0
        #users set parameter
        self.set_parameter()

    def set_parameter(self):
        parameter = {}
        with open('./neural_network.conf', 'r') as f:
            for eachline in f:
                this_line = eachline.strip().split(" ")
                if this_line[0][0] != '#':
                    parameter[this_line[0]] = this_line[1]


