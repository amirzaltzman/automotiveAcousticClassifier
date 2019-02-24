# automotiveAcousticClassifier

Authors
- Amir Zaltzman (<amirzaltzman@mail.tau.ac.il>)
- Ofir Brenner (<ofirbrenner@mail.tau.ac.il>)

Table of Contents
=================
1. [Introduction](#1-introduction)
2. [Installation](#2-installation)
3. [Usage](#3-usage)
4. [Results](#4-usage)

==================

1. Introduction

Autonomous automotive field has widely researched over the last decade, along the growth of researches and applications in deep learning. Our innovation is to make use of the sound inside and outside of the car, to help making high level of confidence autonomous decisions. We intend to classify 10 classes of sonunds that have critical meanning for us at getting atounomous decisions regarding saftey situations.

Here are the clsssess and their main porpuse:

| Class                | Purpose      |
|----------------------|--------------|
| Cat                  |  Forgotten animal\child in the car sound      |
| Dog                  |  Forgotten animal\child in the car sound      |
| Crying baby          |  Forgotten animal\child in the car sound      |
| Car                  |  Driver behavior sound                        |
| Sneezing             |  Driver behavior sound                        |
| Snoring              |  Caution\awareness sound                      | 
| Car horn             |  Caution\awareness sound                      |
| Siren                |  Caution\awareness sound                      | 
| Footsteps            |  Caution\awareness sound                      |
| Rain                 |  Weather sound                                |
| Wind                 |  Zero-reference sound                         |


2. Installation

Requiered Python 3.7
Tensorflow 1.7 and above.

3. Usage

Here are the.py scripts of the project (in the following order) description and how to run them properly– 

recordToSpectogram.py
This function get as an input python script – “parameters.py” which includes the parameters to set to the recordToSpectogram.py script.
In the parameters.py you need to adjust the following parameters (presented as <>) – 
•	PREFIX = <source dir>
Set the source main directory.
•	DATA_PATH = PREFIX + <data dir>
Set the subfolder name in the source, where the data is placed.
•	WAV_DATA_TRAIN = DATA_PATH + <wav dir>
Set the subfolder in the data directory with the wav files.
The wav files need to be divided to subfolders named by the label of the class of the sound in it.
•	IMAGES_DATA_TRAIN = DATA_PATH + <jpg dir>
Set the the subfolder in the data directory, where you want the jpg converted images to be saved in.
•	SAMPLES_PER_CLASS = <positive intiger>

Number of samples to convert per class.

retrain_new.py and retrain_new_dropout.py
This script is based on Google’s transfer learning code (https://github.com/tensorflow/hub/raw/master/examples/image_retraining/retrain.py) .
This code is training our classified image dataset based on pre-trained image classification model (which trained on different dataset and different labels).  
We added new features to the code – 
•	Calculating and plotting confusion-matrix of the tested network and the training session.
•	Added option of 2 layers of dropout regularization and ReLu activation before the embedded softmax layer (that already exists in the original code).
In order to run the code properly you to write in the terminal the following parsers (you need to change the <>)– 
python retrain_new.py  \
--how_many_training_steps <number of steps> \
--output_graph <Dir to save output graph pb file> \
--output_labels <Dir to save output labels text file > \
--image_dir  <Dir where the images dataset is stored (classified to subfolders named by the class)>   \                        
--bottleneck_dir <Dir to save the bottelnecks text files of the image data set> \
--learning_rate <Learning rate> \
--summaries_dir <Dir to save the training and validation log files >    \                                                
--model_dir < Dir to save where the pre-trained model will be stored (if it is not already exists) >         
--tfhub_module <Tensorflow hub URL that includes the pre-trained model trained network files>

(*Example to import MobileNet_v1 to the retrain_new.py is to set tf_hub parser to https://tfhub.dev/google/imagenet/mobilenet_v1_100_224/feature_vector/1)
If you wish to retrain your model with dropout regularization, just change the python file to retrain_new_dropout.py (instead of retrain_new.py ).
 
label_image.py
This code classifies your image according to trained labels of the network.
Follow these parsers - 
python label_image.py \
--graph <output network trained graph pb file> \
--image <image dir>


4. Results

Our test confusion matrix result - 

![alt text](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)

Here is the labeling on car horn sound recorded from Youtube - 

| Class                | Purpose      |
|----------------------|--------------|
| Cat                  |  71.9 %      |
| Dog                  |  62.0 %      |
| Crying baby          |  83.9 %      |
| Car                  |  75.7 %      |
| Sneezing             |  85.6 %      |
| Snoring              |  65.9 %      |
| Car horn             |  76.6 %      |
| Siren                |  79.4 %      |
| Footsteps            |  61.3 %      |
| Rain                 |  85.2 %      |
| Wind                 |  96.1 %      |

