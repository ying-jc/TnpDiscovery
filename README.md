# TnpDiscovery  
A machine learning-based tool for the discovery of prokaryotic transposases from protein features

## Installation  
Clone TnpDiscovery by  
```
$ git clone https://github.com/ying-jc/TnpDiscovery.git
```  
or
Download TnpDiscovery (ZIP file), move it to a directory where the user wants it installed, and uncompress it.

## Requirements  
TnpDiscovery is an open-source Python-based tool, which operates depending on the Python environment (Python Version ≥ 3.0). Currently, TnpDiscovery has only been tested on the Linux system. Before running TnpDiscovery, the user should make sure all the following packages are installed in their Python environment: click, joblib, pandas (≥ 0.20.1), [scikit-learn](https://scikit-learn.org/stable/install.html "scikit-learn") (0.23.1), and [h2o](http://docs.h2o.ai/h2o/latest-stable/h2o-py/docs/intro.html#installing-h2o-3 "h2o") (≥ 3.30.0.7). In addition, since TnpDiscovery makes predictions based on the results of [iFeature](https://github.com/Superzchen/iFeature "iFeature"), it is also necessary to install iFeature and meet its operational requirements.

## Usage  
### Options  
For details of all options, run:  
```
$ python TnpDiscovery.py --help

Usage: TnpDiscovery.py [OPTIONS]

  TnpDiscovery: A machine learning-based tool for the discovery of
  prokaryotic transposases from protein features

Options:
  --conf TEXT                  Configuration file in plain text format.
                               (Required)

  --seq TEXT                   Protein sequence file in fasta format.
                               (Required)

  --classif [EC-all|GBM-best]  Choose a classifier. [Default: EC-all]
                               (Optional)

  --cutoff FLOAT RANGE         Cutoff value for binary classification.
                               [Default: 0.606] (Optional)

  --n_proc INTEGER RANGE       Number of processes used for feature
                               extraction. [Default: 1] (Optional)

  --terminal [True|False]      Output result to the terminal. [Default: True]
                               (Optional)

  --out TEXT                   The name of the output file in tab-delimited
                               text format. (Optional)

  --help                       Show this message and exit.
```  

### Notes  
#### Sequence of input
The input to TnpDiscovery can be any number of protein sequences in FASTA format. The sequence must not contain the blurred disabilities (such as "X", "Z", "B", "J", "O", "U", and "*"), and the length must be greater than 30bp.

#### Result of output
TnpDiscovery outputs the results to the terminal by default. The user can specify the name of the output file to save the results to a CSV file. In the results, the first column represents the sequence name, the second column represents the estimated probability of a transposase for the corresponding sequence, and the third column represents the classification according to the provided cutoff value.

#### Configuration file
The configuration file must be specified to tell the TnpDiscovery where the iFeature and classifier are located. A template of the configuration file can be found in the directory of TnpDiscovery.

#### Number of processes
Increasing the number of processes can effectively shorten the running time of feature extraction. It is recommended to set the number as 15.  

## An example  
All files in the commands can be found in the directory of TnpDiscovery.  
* Set up the configuration file.

* Locate to the example folder:
```
$ cd TnpDiscovery/example
```
* Run the following command to predict the sequences in the example with the default settings:
```
$ python ../TnpDiscovery.py --conf ../config.txt --seq example.fasta
```
Note that if the user is not running the program under the TnpDiscovery folder, the path to TnpDiscovery.py and config.txt needs to be provided.

## Citation  
Prediction of prokaryotic transposases from protein features with machine learning approaches. (Under Review)
