# Innovatech Studio Homework Solution

This project is offered as a solution to the interview homework described here: [Python Homework](Python%20Homework.docx)

## Prerequisites and Installation

The following items must be installed in order to properly run the program provided.
Please refer to the links below for instruction on how to install and configure each required component.

[Python >= 3.3](https://www.python.org/downloads/)  
[MeCab](http://taku910.github.io/mecab/#install)  
[natto](https://pypi.org/project/natto-py/)  
[numpy + scipy](https://scipy.org/install.html)  
[scikit-learn](http://scikit-learn.org/stable/install.html)  
[tinysegmenter](https://pypi.org/project/tinysegmenter/)

## Setup Test

Once all prerequisites are set up, pull/download the entire repository, open a console/command prompt, and use cd to go inside the folder.
Once there, run the following:

```
python homework_solution.py
```

If successful, no errors should be thrown, and a new file called sample\_output.py will be generated within the project folder.
The output file will contain the output generated from the files located within the sample_input directory.

## Command Line Parameters

Below are details about the command line parameters the script accepts. You can also pass the -h flag to the script to see the information, like so:

```
python homework_solution.py -h
```

```
usage: homework_solution.py [-h] [-ie INPUT_ENCODING] [-oe OUTPUT_ENCODING]
                            [-op OUTPUT_PATH] [-id INPUT_DIRECTORY]

Solution to Python Homework for Innovatech Studio - by Kevin Edelmann

optional arguments:
  -h, --help            show this help message and exit
  -ie INPUT_ENCODING, --input_encoding INPUT_ENCODING
                        Input encoding. Default is 'utf-8'.
  -oe OUTPUT_ENCODING, --output_encoding OUTPUT_ENCODING
                        Output encoding. Default is 'utf-8'.
  -op OUTPUT_PATH, --output_path OUTPUT_PATH
                        Output file destination. Default is
                        'sample_output.txt'.
  -id INPUT_DIRECTORY, --input_directory INPUT_DIRECTORY
                        Path to a folder containing the .txt files to be used
                        for the corpus. Default is 'sample_input'
```

## Default Values

Default values for the command line parameters can be edited in the homework_solution.py file; the constants defining the defaults can be found towards the top of the file:

```
DEFAULT_INPUT_ENCODING = "utf-8"
DEFAULT_OUTPUT_ENCODING = "utf-8"
DEFAULT_OUTPUT_PATH = "sample_output.txt"
DEFAULT_INPUT_DIRECTORY = "sample_input"
```

## Author

* **Kevin Edelmann**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Many thanks to Kengo, Pascal, and Matt of Innovatech Studio for our interview and this homework assignment
