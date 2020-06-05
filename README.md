# Image classification on Terminal using fast.ai 

This tool lets you build an image classifier with a single terminal command. 

## Installation

This tool requires fast.ai and Python3 to be installed. Instructions to install fast.ai can be found [here](https://docs.fast.ai/install.html)
<br>
Clone the repo and navigate to the folder on Terminal. 

## Data

Data must be arranged into 3 folders, train test and valid, in the form:
<br>
/data<br>
&nbsp;&nbsp;&nbsp;&nbsp;/train<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/class1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/class2<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/class3<br>
&nbsp;&nbsp;&nbsp;&nbsp;/valid<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/class1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/class2<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/class3<br>
&nbsp;&nbsp;&nbsp;&nbsp;/test <br>

### Organizing data
The data folder should be of the form:<br>
/data<br>
&nbsp;&nbsp;&nbsp;&nbsp;/class1<br>
&nbsp;&nbsp;&nbsp;&nbsp;/class2<br>
&nbsp;&nbsp;&nbsp;&nbsp;/class3<br>


## Parameters

* **Path**: Compulsory parameter that specifies path to the folder containing training data.
* **batchsize**: Sets the batchsize(defaults of 4)
* **epochs**: Sets the number of epochs the model will train(defaults to 10)



## Usage

Run the main.py script

```
$ python3 main.py pathtodata 

```

Optionally you can specify a custom batchsize and the number of epochs to train the model. After the model is done training it will be saved as model.pkl. 
