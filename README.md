# OTEANN 

This repository is the official implementation of [OTEANN: Estimating the Transparency of Orthographies with an Artificial Neural Network](https://arxiv.org/abs/1912.13321v2).

## Requirements

* Require Ubuntu 18.04, Python 3.6+.

* Download files on your machine
  * git clone https://github.com/marxav/oteann2.git

* Go to the oteann2 main directory
  * cd oteann2 

* Create a virtual environment
  * python3 -m venv oteann 

* Activate virtual environment
  * source oteann/bin/activate

* Load the python librairies needed for GIPFA (e.g. numpy, pandas, torch...) from the requirements file
  * python -m pip install -r requirements.txt
  
* Download the subdatasets (required local free spacesize=334Mo)
  * python download_subdatasets.py

## Evaluation and Training

In order to run this code, you need to:
* Run the [oteann.ipynb](oteann.ipynb) in order to create the ANN model, train it, test it and display the results of the paper.

## Results

OTEANN achieves the following performance:

### 

|orthography| write score| read score |
|-----------|------------|------------|
|    ent    | 99.4 ± 0.2 | 99.3 ± 0.3 |
|    eno    | 00.0 ± 0.0 | 00.0 ± 0.0 |
|    ar     | 83.8 ± 1.3 | 99.4 ± 0.3 |
|    br     | 80.0 ± 1.1 | 76.3 ± 1.7 |
|    de     | 68.9 ± 1.4 | 78.2 ± 1.0 |
|    en     | 36.5 ± 0.6 | 33.0 ± 1.8 |
|    es     | 67.0 ± 1.3 | 85.2 ± 1.2 |
|    fi     | 97.9 ± 0.4 | 92.8 ± 0.8 |
|    fr     | 27.8 ± 0.9 | 78.3 ± 1.2 |
|    fro    | 99.1 ± 0.3 | 89.0 ± 1.2 |
|    it     | 94.9 ± 0.8 | 72.0 ± 1.4 |
|    ko     | 82.0 ± 1.2 | 97.7 ± 0.5 |
|    nl     | 73.1 ± 1.8 | 56.6 ± 1.5 |
|    pt     | 70.7 ± 1.2 | 32.2 ± 1.8 |
|    ru     | 42.4 ± 1.7 | 97.6 ± 0.7 |
|    sh     | 99.1 ± 0.2 | 54.4 ± 2.3 |
|    tr     | 95.5 ± 0.7 | 96.0 ± 0.7 |

## License

OTEANN uses minGTPT (https://github.com/karpathy/minGPT) which is released under the MIT licence.

## Citation
This code was used for the following paper:
```bibtex
@misc{marjou2020oteann,
      title={OTEANN: Estimating the Transparency of Orthographies with an Artificial Neural Network}, 
      author={Xavier Marjou},
      year={2020},
      eprint={1912.13321},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
