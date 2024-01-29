# A Transformer-Based Approach for Improving App Review Response Generation
In this repo, we release code and data for training a TRRGen model.
You can see our paper [here](https://arxiv.org/pdf/2209.08055.pdf).
## Install
Please prepare a proper tensorflow environment for runing the code
```
pip install tensorflow tensorflow_datasets numpy matplotlib tqdm
```

## Dataset
Download from [here](https://drive.google.com/file/d/1Ycl7AW5jhYHMyPqJT8KimAgdFz8hitjK/view?usp=sharing).

## Train and test
For training the model,
```
python main.py
```
For runing BLEU test,
```
python bleu_de.py
```

## Citation
If you find this repo useful in your research, please consider citing it.
```
@article{zhang2023transformer,
  title={A transformer-based approach for improving app review response generation},
  author={Zhang, Weizhe and Gu, Wenchao and Gao, Cuiyun and Lyu, Michael R},
  journal={Software: Practice and Experience},
  volume={53},
  number={2},
  pages={438--454},
  year={2023},
  publisher={Wiley Online Library}
}
```
