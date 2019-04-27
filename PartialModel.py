#local2partial within the same GPU
import torch

#device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class Partial_Model:
    def __init__(self, state_dict, capacity, global_model):
        """
        capacity = num of local models
        """
        self.capacity = capacity # how many local models specified in the same GPU
        self.state_dict = state_dict # weights of partial model
        self.true_global = global_model


    def partial_updates_sum(self, w_in):
        #w_in represents weights from a local model
        for k in self.state_dict.keys(): # iterate every weight element
            self.state_dict[k] += w_in[k]
        
        return self.state_dict

    def pull_global(self):
        self.true_global = global_model.Update_True()

