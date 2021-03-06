from elliot.run import run_experiment
import gdown
import os
import shutil

print('MODELS:')
print(u'''
+--------------------------------------------------------------------------------------------------------+----------+--------------------------------------------------------+
|                                                 Paper                                                  |   Name   |                          Link                          |
+--------------------------------------------------------------------------------------------------------+----------+--------------------------------------------------------+
| Neural Graph Collaborative Filtering                                                                   | ngcf     | https://dl.acm.org/doi/10.1145/3331184.3331267         |
| LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation                        | lightgcn | https://dl.acm.org/doi/10.1145/3397271.3401063         |
| Disentangled Graph Collaborative Filtering                                                             | dgcf     | https://dl.acm.org/doi/abs/10.1145/3397271.3401137     |
| Revisiting Graph Based Collaborative Filtering: A Linear Residual Graph Convolutional Network Approach | lr-gccf  | https://ojs.aaai.org//index.php/AAAI/article/view/5330 |
| UltraGCN: Ultra Simplification of Graph Convolutional Networks for Recommendation                      | ultragcn | https://dl.acm.org/doi/10.1145/3459637.3482291         |
| How Powerful is Graph Convolution for Recommendation?                                                  | gfcf     | https://dl.acm.org/doi/abs/10.1145/3459637.3482264     |
+--------------------------------------------------------------------------------------------------------+----------+--------------------------------------------------------+
''')

while True:
    model = input('Insert model name (ngcf, lightgcn, dgcf, lr-gccf, ultragcn, gfcf): ').lower()
    if model in ['ngcf', 'lightgcn', 'dgcf', 'lr-gccf', 'ultragcn', 'gfcf']:
        break
    else:
        print('Sorry, the model should be one of these: ngcf, lightgcn, dgcf, lr-gccf, ultragcn, gfcf')

while True:
    layer = input('Insert number of explored hops (0 for ultragcn and gfcf, 1, 2, 3, 4 for the others): ')
    if layer.lower() in ['0', '1', '2', '3', '4']:
        break
    else:
        print('Sorry, the number of explored hops should be one of these: 0, 1, 2, 3, 4')

print('DATASETS:')
print(u'''
+----------------------+--------+--------+--------------+
|       Dataset        | Users  | Items  | Interactions |
+----------------------+--------+--------+--------------+
| Movielens-1M         |  5,915 |  2,753 |      570,622 |
| Amazon Digital Music |  8,328 |  6,275 |       99,400 |
| Epinions             | 14,341 | 13,145 |      269,170 |
+----------------------+--------+--------+--------------+
''')

while True:
    dataset = input('Insert dataset name (movielens-1m, amazon digital music, epinions): ').lower()
    if dataset in ['movielens-1m', 'amazon digital music', 'epinions']:
        if dataset == 'movielens-1m':
            dataset = 'movielens'
            if not os.path.exists('data/movielens'):
                os.makedirs('data/movielens')
                gdown.download_folder("https://drive.google.com/drive/folders/1ZIAFa63TAP76D5qSRaxltN0jBwO3aPbE",
                                      use_cookies=False)

                files_list = os.listdir('movielens')
                for files in files_list:
                    shutil.move('movielens/' + files, 'data/movielens/')
                os.rmdir('movielens')
        elif dataset == 'epinions':
            if not os.path.exists('data/epinions'):
                os.makedirs('data/epinions')
                gdown.download_folder("https://drive.google.com/drive/folders/1uj7X5PdaHTbES-YcoKnQMEuuiLAjC-_k",
                                      use_cookies=False)
                files_list = os.listdir('epinions')
                os.rmdir('epinions')
                for files in files_list:
                    shutil.move('epinions/' + files, 'data/epinions/')
        else:
            dataset = 'amazon_music'
            if not os.path.exists('data/amazon_music'):
                os.makedirs('data/amazon_music')
                gdown.download_folder("https://drive.google.com/drive/folders/1ABWWOE9PONypZw1qV80VrRu2T7QQicRn",
                                      use_cookies=False)
                files_list = os.listdir('amazon_music')
                for files in files_list:
                    shutil.move('amazon_music/' + files, 'data/amazon_music/')
                os.rmdir('amazon_music')
        break
    else:
        print('Sorry, the dataset should be one of these: movielens-1m, amazon digital music, epinions')

print('\n\n')
run_experiment(f"config_files/{model}_{dataset}_{layer}.yml")