import torch


class Hyperparameters():

    data = 'data_thchs30/biaobei_48000'

    max_Ty = max_iter = 200

    # gpu = 1
    device = 'cuda:1'
    # device = 'cpu'

    lr = 0.001
    batch_size = 32   # !!!
    num_epochs = 10000  # !!!
    eval_size = 0
    save_per_epoch = 1
    log_per_batch = 500
    log_dir = 'log/train_{}'

    model_path = None
    optimizer_path = None

    eval_text = '''er2 dui4 lou2 shi4 cheng2 jiao1 yi4 zhi4 zuo4 yong4 zui4 da4 de5 xian4 gou4'''
    # eval_text = '''chua1n pu3 zo3ng to3ng shuo1 ta1 ce2ng ji1ng xia4ng me3i guo2 re2n mi2n che2ng nuo4 jia1ng yo3u yi1 ge4 me3i ha3o de she4ng da4n li3 wu4  sui2 zhe zhe4 yi1 jia3n shui4 fa3 a4n to1ng guo4  ta1 ye3 dui4 xia4n le zhe4 yi1 che2ng nuo4'''
    # eval_text = '''Printing, in the only sense with which we are at present concerned, differs from most if not from all the arts and crafts represented in the Exhibition'''
    ref_wav = 'ref_wav'

    lr_step = [500000, 1000000, 2000000]

    # vocab = "_~ abcdefghijklmnopqrstuvwxyz'.?"  # english
    vocab = "_~ abcdefghijklmnopqrstuvwxyz12345.?"  # chinese
    char2idx = {char: idx for idx, char in enumerate(vocab)}

    E = 256

    # reference encoder
    ref_enc_filters = [32, 32, 64, 64, 128, 128]
    ref_enc_size = [3, 3]
    ref_enc_strides = [2, 2]
    ref_enc_pad = [1, 1]
    ref_enc_gru_size = E // 2

    # style token layer
    token_num = 10
    # token_emb_size = 256
    num_heads = 8
    # multihead_attn_num_unit = 256
    # style_att_type = 'mlp_attention'
    # attn_normalize = True

    K = 16
    decoder_K = 8
    embedded_size = E
    dropout_p = 0.5
    num_banks = 15
    num_highways = 4

    # sr = 22050  # Sample rate.
    sr = 48000  # keda, thchs30, aishell
    n_fft = 4096  # fft points (samples)
    frame_shift = 0.0125  # seconds
    frame_length = 0.05  # seconds
    hop_length = int(sr * frame_shift)  # samples.
    win_length = int(sr * frame_length)  # samples.
    n_mels = 80  # Number of Mel banks to generate
    power = 1.2  # Exponent for amplifying the predicted magnitude
    n_iter = 50  # Number of inversion iterations
    preemphasis = .97  # or None
    max_db = 120
    ref_db = 20
    fmin = 125
    fmax = 7600

    # n_priority_freq = int(3000 / (sr * 0.5) * (n_fft / 2))

    r = 4

    use_gpu = torch.cuda.is_available()


if __name__ == '__main__':
    print(Hyperparameters.char2idx['~'])
