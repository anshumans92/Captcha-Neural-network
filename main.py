import tensorboard
tensorboard --logdir='log/cnn1-run-%s' % datetime.datetime.now().strftime('%Y%m%d_%H%M%S')