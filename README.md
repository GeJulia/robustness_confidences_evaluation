# Robust Models are less Over-Confident
Julia Grabinski, Paul Gavrikov, Janis Keuper, Margret Keuper
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

Presented at: Thirty-sixth Conference on Neural Information Processing Systems (NeurIPS)

[Paper]() | [ArXiv]() | [HQ Poster]() | [Talk]()


Abstract: *We empirically show that adversarially robust models are less over-confident then their non-robust counterparts.
Abstract: Regardless of the success of convolutional neural networks (CNNs) in many academic benchmarks of computer vision tasks, their application in real-world is still facing fundamental challenges, like the inherent lack of robustness as unveiled by adversarial attacks. These attacks target to manipulate the network's prediction by adding a small amount of noise onto the input. In turn, adversarial training (AT) aims to achieve robustness against such attacks by including adversarial samples in the trainingset. However, a general analysis of the reliability and model calibration of these robust models beyond adversarial robustness is still pending. In this paper, we analyze a variety of adversarially trained models that achieve high robust accuracies when facing state-of-the-art attacks and we show that AT has an interesting side-effect: it leads to models that are significantly less overconfident with their decisions even on clean data than non-robust models. Further, our analysis of robust models shows that not only AT but also the model's building blocks (activation functions and pooling) have a strong influence on the models' confidence.*


[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


## Model Zoo


## Citation

Would you like to reference our evaluation? \
Then consider citing our [paper]():


```bibtex
@inproceedings{grabinski2022robust,
  title     = {Robust Models are less Over-Confident},
  author    = {Grabinski, Julia and Gavrikov, Paul and Keuper, Janis and Keuper, Margret},
  booktitle = {Advances in Neural Information Processing Systems},
  publisher = {Curran Associates, Inc.},
  year      = {2022},
  volume    = {35},
  url       = {}
}
```

### Legal
This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa]. Please note that [robust](https://github.com/RobustBench/robustbench/blob/master/LICENSE) and [normal imagenet](https://github.com/rwightman/pytorch-image-models#licenses) models are not provided by us are licensed differently. 
