root_dir = root_dir = "/Users/ronhochstenbach/Desktop/Thesis/Data"

hyperparams_features = {
    "max_features": 20002,
    "embedding_dim": 300,
    "vocabulary_path": root_dir + '/Resources/vocab.pickle',
    "nrc_lexicon_path" : root_dir + "/Resources/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt",
    "liwc_path": root_dir + '/Resources/LIWC2007.dic',
    "stopwords_path": root_dir + '/Resources/stopwords.txt',
    "embeddings_path": "Resources/glove.840B.300d.txt"#,
    #"liwc_words_cached": "data/liwc_categories_for_vocabulary_erisk_clpsych_stop_20K.pkl"
}

hyperparams = {
    "trainable_embeddings": True,

    "lstm_units": 128,

    "dense_bow_units": 20,
    "dense_sentence_units": 0,
    "dense_numerical_units": 20,


    "filters": 100,
    "kernel_size": 5,

    "lstm_units_user": 32,
    "dense_user_units": 0,

    "filters_user": 10,
    "kernel_size_user": 3,

    "transfer_units": 20,

    "dropout": 0.1,
    "l2_dense": 0.00011,
    "l2_embeddings": 0.0000001,
    "l2_bert": 0.0001,
    "norm_momentum": 0.1,

    "ignore_layer": ["bert_layer"
                    ],

    "decay": 0.001,
    "lr": 0.00005,
    "reduce_lr_factor": 0.5,
    "reduce_lr_patience": 55,
    "scheduled_reduce_lr_freq": 95,
    "scheduled_reduce_lr_factor": 0.5,
    "freeze_patience": 2000,
    "threshold": 0.5,
    "early_stopping_patience": 5,

    "positive_class_weight": 2,

    "maxlen": 256,
    "posts_per_user": 0,
    "post_groups_per_user": 0,
    "posts_per_group": 50,
    "batch_size": 32,
    "padding": "pre",
    "hierarchical": True,
    "sample_seqs": False,
    "sampling_distr": "exp",
}