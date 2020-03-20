# Image classification on Terminal using fast.ai 

This tool lets you build an image classifier with a simgle terminal command. 

## Installation

This tool requires fast.ai and Python3 to be installed. Instructions to install fast.ai can be found [here](https://docs.fast.ai/install.html)
<br>
Clone the repo and navigate to the folder on Terminal. 

## Data

Data must be arranged into 3 folders- train test and valid in the form:
<br>
/data<br>
&nbsp;&nbsp;&nbsp;&nbsp;/train<br>
         /class1<br>
         /class2<br>
         /class3<br>
     /valid<br>
         /class1<br>
         /class2<br>
         /class3<br>
    /test <br>

### Organizing data
In order to arrange data in this format simply run organize.py with the pathname of the folder containing the data and the classes of data in the folder. The data folder should be of the form:
/data<br>
	 /class1<br>
	 /class2<br>
	 /class3<br>

```
$ python3 organize.py pathtodata

```

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
