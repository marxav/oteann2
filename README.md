# OTEANN 

This repository is the official implementation of [OTEANN: Estimating the Transparency of Orthographies with an Artificial Neural Network](https://arxiv.org/abs/2006.07573).

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

|-----------|-----------|-----------|
|orthography|write score|read score |
|-----------|-----------|-----------|
|        ent|0.99 ± 0.00|0.99 ± 0.00|
|        eno|0.00 ± 0.00|0.00 ± 0.00|
|         ar|0.84 ± 0.01|0.99 ± 0.00|
|         br|0.80 ± 0.01|0.76 ± 0.02|
|         de|0.69 ± 0.01|0.78 ± 0.01|
|         en|0.37 ± 0.01|0.33 ± 0.02|
|         es|0.67 ± 0.01|0.85 ± 0.01|
|         fi|0.98 ± 0.00|0.93 ± 0.01|
|         fr|0.28 ± 0.01|0.78 ± 0.01|
|        fro|0.99 ± 0.00|0.89 ± 0.01|
|         it|0.95 ± 0.01|0.72 ± 0.01|
|         ko|0.82 ± 0.01|0.98 ± 0.01|
|         nl|0.73 ± 0.02|0.57 ± 0.02|
|         pt|0.71 ± 0.01|0.32 ± 0.02|
|         ru|0.42 ± 0.02|0.98 ± 0.01|
|         sh|0.99 ± 0.00|0.54 ± 0.02|
|         tr|0.95 ± 0.01|0.96 ± 0.01|
|-----------|-----------|-----------|


## License

OTEANN uses minGTPT (https://github.com/karpathy/minGPT) which is released under the MIT licence.

