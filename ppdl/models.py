import numpy as np

def transfer_weights(from_model, to_model):
    layers_not_transferred = []
    layers_transferred = []
    for from_layer in from_model.layers:
        try:
            to_layer = to_model.get_layer(from_layer.name)
            from_w = from_layer.get_weights()
            to_w   = to_layer.get_weights()
            if len(from_w)==len(to_w) and np.alltrue([f.shape==t.shape for f,t in zip(from_w, to_w)]):
                to_layer.set_weights(from_w)
                layers_transferred.append(from_layer.name)            
            else:
                layers_not_transferred.append(from_layer.name)            
        except:
            layers_not_transferred.append(from_layer.name)
            continue
    
    print ("layers transferred    ", layers_transferred)
    print ("layers not transferred", layers_not_transferred)