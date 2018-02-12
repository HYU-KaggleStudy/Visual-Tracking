options = {
    'seed': 666,
    'model_path': './bin/mdnet_vot-otb.pth',
    'img_size': 107,
    'padding': 16,
    'batch_pos': 64,
    'batch_neg': 192,
    'batch_neg_cand': 1024,
    'batch_test': 256,
    'n_samples': 512,
    'trans_f': 0.3,
    'trans_f_expand': 0.9,
    'scale_f': 1.05,
    'n_bbreg': 1000,
    'overlap_bbreg': [0.6, 1],
    'scale_bbreg': [1, 2],
    'n_pos_init': 500,
    'n_neg_init': 5000,
    'n_pos_update': 50,
    'n_neg_update': 200,
    'n_frames_short': 20,
    'n_frames_long': 100,
    'long_interval': 10,
    'lr_init': 0.0001,
    'lr_update': 0.0002,
    'lr_mult': {'fc6': 10},
    'maxiter_init': 30,
    'maxiter_update': 15,
    'overlap_pos_init': [0.7, 1],
    'overlap_neg_init': [0, 0.5],
    'overlap_pos_update': [0.7, 1],
    'overlap_neg_update': [0, 0.3],
    'success_thr': .1,
    'w_decay': 0.0005,
    'momentum': 0.9,
    'grad_clip': 10,
    'ft_layers': ['fc'],
}
