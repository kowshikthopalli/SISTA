# Single-Shot Domain Adaptation via Target-Aware Generative Augmentations
[![arXiv](https://img.shields.io/badge/arXiv-2210.16692-b31b1b.svg)](https://arxiv.org/abs/2210.16692)

This is the PyTorch implementation of [Single-Shot Domain Adaptation via Target-Aware Generative Augmentations](https://arxiv.org/pdf/2210.16692.pdf).

>**Abstract:**<br>
The problem of adapting models from a source domain using data from any target domain of interest has gained prominence, thanks to the brittle generalization in deep neural networks. While several test-time adaptation techniques have emerged, they typically rely on synthetic data augmentations in cases of limited target data availability. In this paper, we consider the challenging setting of single-shot adaptation and explore the design of augmentation strategies. We argue that augmentations utilized by existing methods are insufficient to handle large distribution shifts, and hence propose a new approach SiSTA (Single-S hot T arget A ugmentations), which first fine-tunes a generative model from the source domain using a single-shot target, and then employs novel sampling strategies for curating synthetic target data. Using experiments with a state-of-the-art domain adaptation method, we find that SiSTA produces improvements as high as 20% over existing baselines under challenging shifts in face attribute detection, and that it performs competitively to oracle models obtained by training on a larger target dataset.

## Data Augmentation

## Citation
If you use this code or ideas from our paper, please cite our paper:
```
@article{chong2021jojogan,
  title={JoJoGAN: One Shot Face Stylization},
  author={Chong, Min Jin and Forsyth, David},
  journal={arXiv preprint arXiv:2112.11641},
  year={2021}
}
```

## Acknowledgments
This code borrows from [StyleGAN2 by rosalinity](https://github.com/rosinality/stylegan2-pytorch), [e4e](https://github.com/omertov/encoder4editing) [StyleGAN-NADA](https://github.com/rinongal/StyleGAN-nada) [NRC](https://github.com/Albert0147/NRC_SFDA), [MEMO](https://github.com/zhangmarvin/memo/) and [RandConv](https://github.com/wildphoton/RandConv). 

We thank the authors of the respective works for publicly sharing their code.
