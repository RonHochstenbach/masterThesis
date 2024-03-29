from metrics import Metrics
import json
from keras.models import load_model
from keras import optimizers
from train import initialize_model

def save_model_and_params(model, model_path, hyperparams, hyperparams_features):
    model.save_weights(model_path + "_weights.h5", save_format='h5')
    with open(model_path + '.hp.json', 'w+') as hpf:
        hpf.write(json.dumps({k:v for (k,v) in hyperparams.items() if k!='optimizer'}))
    with open(model_path + '.hpf.json', 'w+') as hpff:
        hpff.write(json.dumps(hyperparams_features))

def load_params(model_path, general_config_path='/Users/ronhochstenbach/Desktop/Thesis/Data/Resources/config.json'):
    with open(model_path + '.hp.json', 'r') as hpf:
        hyperparams = json.loads(hpf.read())
    with open(model_path + '.hpf.json', 'r') as hpff:
        hyperparams_features = json.loads(hpff.read())
    with open(general_config_path) as f:
        config = json.load(f)
    for k in config:
        if k not in hyperparams_features:
            hyperparams_features[k] = config[k]
    hyperparams['optimizer'] = optimizers.Adam(learning_rate=hyperparams['lr'], #beta_1=0.9, beta_2=0.999, epsilon=0.0001,
                                   decay=hyperparams['decay'])
    return hyperparams, hyperparams_features

def load_saved_model(model_path, hyperparams):
    metrics_class = Metrics(threshold=hyperparams['threshold'])
    dependencies = {
    'f1_m': metrics_class.f1_m,
    'precision_m': metrics_class.precision_m,
    'recall_m': metrics_class.recall_m,
    }
    loaded_model = load_model(model_path + "_model.h5", custom_objects=dependencies)
    return loaded_model

def load_saved_model_weights(model_path, hyperparams, hyperparams_features, model_type, h5=False):
    metrics_class = Metrics(threshold=hyperparams['threshold'])
    dependencies = {
    'f1_m': metrics_class.f1_m,
    'precision_m': metrics_class.precision_m,
    'recall_m': metrics_class.recall_m,
    }
    loaded_model = initialize_model(hyperparams, hyperparams_features, model_type)
    loaded_model.summary()
    path = model_path + "_weights"
    by_name = False
    if h5:
        path += ".h5"
        by_name=True
    loaded_model.load_weights(path, by_name=by_name)
    return loaded_model
