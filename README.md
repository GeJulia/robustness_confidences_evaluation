# Robust Models are less Over-Confident
Julia Grabinski, Paul Gavrikov, Janis Keuper, Margret Keuper

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

Presented at: Thirty-sixth Conference on Neural Information Processing Systems (NeurIPS)

 [Paper](https://openreview.net/pdf?id=5K3uopkizS) <!-- | [ArXiv]() | [HQ Poster]() | [Talk]() -->


Abstract: *We empirically show that adversarially robust models are less over-confident then their non-robust counterparts.
Abstract: Regardless of the success of convolutional neural networks (CNNs) in many academic benchmarks of computer vision tasks, their application in real-world is still facing fundamental challenges, like the inherent lack of robustness as unveiled by adversarial attacks. These attacks target to manipulate the network's prediction by adding a small amount of noise onto the input. In turn, adversarial training (AT) aims to achieve robustness against such attacks by including adversarial samples in the trainingset. However, a general analysis of the reliability and model calibration of these robust models beyond adversarial robustness is still pending. In this paper, we analyze a variety of adversarially trained models that achieve high robust accuracies when facing state-of-the-art attacks and we show that AT has an interesting side-effect: it leads to models that are significantly less overconfident with their decisions even on clean data than non-robust models. Further, our analysis of robust models shows that not only AT but also the model's building blocks (activation functions and pooling) have a strong influence on the models' confidence.*


[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


## Model Zoo
[![Latest Version](https://img.shields.io/pypi/v/robustvsnormalzoo.svg)](https://pypi.python.org/pypi/robustvsnormalzoo)

Install it by:
```bash
pip install git+https://github.com/RobustBench/robustbench.git@v1.0
pip install robustvsnormalzoo
```
and then obtain pretrained models as simple as:
```python
import robustvsnormalzoo

model = robustvsnormalzoo.load_model(dataset, paper_id, robust)
```
Set `robust=True` to download the robust checkpoint, and `False` for the normal one.

Supported combinations can be queried by:

```python
robustvsnormalzoo.list_models()
```
<details>

|dataset |paper_id                            |
|--------|------------------------------------|
|cifar10 |Andriushchenko2020Understanding     |
|cifar10 |Carmon2019Unlabeled                 |
|cifar10 |Sehwag2020Hydra                     |
|cifar10 |Wang2020Improving                   |
|cifar10 |Hendrycks2019Using                  |
|cifar10 |Rice2020Overfitting                 |
|cifar10 |Zhang2019Theoretically              |
|cifar10 |Engstrom2019Robustness              |
|cifar10 |Chen2020Adversarial                 |
|cifar10 |Huang2020Self                       |
|cifar10 |Pang2020Boosting                    |
|cifar10 |Wong2020Fast                        |
|cifar10 |Ding2020MMA                         |
|cifar10 |Zhang2019You                        |
|cifar10 |Zhang2020Attacks                    |
|cifar10 |Wu2020Adversarial_extra             |
|cifar10 |Wu2020Adversarial                   |
|cifar10 |Gowal2020Uncovering_70_16           |
|cifar10 |Gowal2020Uncovering_70_16_extra     |
|cifar10 |Gowal2020Uncovering_34_20           |
|cifar10 |Gowal2020Uncovering_28_10_extra     |
|cifar10 |Sehwag2021Proxy                     |
|cifar10 |Sehwag2021Proxy_R18                 |
|cifar10 |Sitawarin2020Improving              |
|cifar10 |Chen2020Efficient                   |
|cifar10 |Cui2020Learnable_34_20              |
|cifar10 |Cui2020Learnable_34_10              |
|cifar10 |Zhang2020Geometry                   |
|cifar10 |Rebuffi2021Fixing_28_10_cutmix_ddpm |
|cifar10 |Rebuffi2021Fixing_106_16_cutmix_ddpm|
|cifar10 |Rebuffi2021Fixing_70_16_cutmix_ddpm |
|cifar10 |Rebuffi2021Fixing_70_16_cutmix_extra|
|cifar10 |Sridhar2021Robust                   |
|cifar10 |Sridhar2021Robust_34_15             |
|cifar10 |Rebuffi2021Fixing_R18_ddpm          |
|cifar10 |Rade2021Helper_R18_extra            |
|cifar10 |Rade2021Helper_R18_ddpm             |
|cifar10 |Rade2021Helper_extra                |
|cifar10 |Rade2021Helper_ddpm                 |
|cifar10 |Huang2021Exploring                  |
|cifar10 |Huang2021Exploring_ema              |
|cifar10 |Addepalli2021Towards_RN18           |
|cifar10 |Addepalli2021Towards_WRN34          |
|cifar10 |Gowal2021Improving_70_16_ddpm_100m  |
|cifar10 |Dai2021Parameterizing               |
|cifar10 |Gowal2021Improving_28_10_ddpm_100m  |
|cifar10 |Gowal2021Improving_R18_ddpm_100m    |
|cifar10 |Chen2021LTD_WRN34_10                |
|cifar10 |Chen2021LTD_WRN34_20                |
|cifar100|Gowal2020Uncovering                 |
|cifar100|Gowal2020Uncovering_extra           |
|cifar100|Cui2020Learnable_34_20_LBGAT6       |
|cifar100|Cui2020Learnable_34_10_LBGAT0       |
|cifar100|Cui2020Learnable_34_10_LBGAT6       |
|cifar100|Chen2020Efficient                   |
|cifar100|Wu2020Adversarial                   |
|cifar100|Sitawarin2020Improving              |
|cifar100|Hendrycks2019Using                  |
|cifar100|Rice2020Overfitting                 |
|cifar100|Rebuffi2021Fixing_70_16_cutmix_ddpm |
|cifar100|Rebuffi2021Fixing_28_10_cutmix_ddpm |
|cifar100|Rebuffi2021Fixing_R18_ddpm          |
|cifar100|Rade2021Helper_R18_ddpm             |
|cifar100|Addepalli2021Towards_PARN18         |
|cifar100|Addepalli2021Towards_WRN34          |
|cifar100|Chen2021LTD_WRN34_10                |
|imagenet|Wong2020Fast                        |
|imagenet|Engstrom2019Robustness              |
|imagenet|Salman2020Do_R50                    |
|imagenet|Salman2020Do_R18                    |
|imagenet|Salman2020Do_50_2                   |

</details>

## Citation

Would you like to reference our evaluation? \
Then consider citing our paper:


```bibtex
@inproceedings{
  grabinski2022robust,
  title={Robust Models are less Over-Confident},
  author={Julia Grabinski and Paul Gavrikov and Janis Keuper and Margret Keuper},
  booktitle={Advances in Neural Information Processing Systems},
  editor={Alice H. Oh and Alekh Agarwal and Danielle Belgrave and Kyunghyun Cho},
  year={2022},
  url={https://openreview.net/forum?id=5K3uopkizS}
}
```

### Legal
This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa]. Please note that [robust](https://github.com/RobustBench/robustbench/blob/master/LICENSE) and [normal imagenet](https://github.com/rwightman/pytorch-image-models#licenses) models are not provided by us and are licensed differently. 
