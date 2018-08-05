from natto import MeCab # Documentation: https://github.com/buruzaemon/natto-py/wiki
from sklearn.feature_extraction.text import TfidfVectorizer # Documentation: http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
from tinysegmenter import TinySegmenter # Documentation: http://tinysegmenter.tuxfamily.org/
from argparse import ArgumentParser # Documentation: https://docs.python.org/3/library/argparse.html
from os import listdir # Documentation: https://docs.python.org/3/library/os.html
from os.path import isfile, join # Documentation: https://docs.python.org/3/library/os.path.html

"""
Default constants for interesect_mecab_noun_list_and_sklearn_vocab_list()
"""
DEFAULT_INPUT_ENCODING = "utf-8"
DEFAULT_OUTPUT_ENCODING = "utf-8"
DEFAULT_OUTPUT_PATH = "sample_output.txt"
DEFAULT_INPUT_DIRECTORY = "sample_input"

"""
Default constants for output_results()
"""
NOUN_LIST_HEADER = "======= Noun List ======="
VOCAB_LIST_HEADER = "==== Vocabulary List ===="
INTERSECTION_HEADER = "=== List Intersection ==="

"""
Generator function that yields the handles for reading the input files one at a time
	corpus (list [str]): List of file paths representing the input files that make up the corpus
	encoding (str): Encoding to use when parsing the input files
	yield (io.TextIOWrapper): Object that reads from the next successive input file
"""
def file_contents_generator(corpus, encoding):
	for file_path in corpus:
		with open(file_path, "rb") as handle:
			yield handle.read().decode(encoding)

"""
Extracts all nouns from the corpus by using MeCab
Range of posids that correspond to nouns were found here: https://taku910.github.io/mecab/posid.html
	corpus (list [str]): List of file paths representing the input files that make up the corpus
	encoding (str): Encoding to use when parsing the input files
	return (list [str]): The nouns found in the corpus (repeats included)
"""
def get_noun_list(corpus, encoding):
	with MeCab() as nm:
		return [
			n.surface 
			for input_text in file_contents_generator(corpus, encoding)
			for n in nm.parse(input_text, as_nodes=True) 
			if n.posid in range(36, 68)
		]

"""
Extracts all vocabulary words from the corpus by using sklearn's TfidfVectorizer with TinySegmenter's tokenizer
	corpus (list [str]): List of file paths representing the input files that make up the corpus
	encoding (str): Encoding to use when parsing the input files
	return (list [str]): The vocabulary found in the corpus (repeats included)
"""
def get_vocab_list(corpus, encoding):
	segmenter = TinySegmenter()
	vectorizer = TfidfVectorizer(tokenizer=segmenter.tokenize)
	X = vectorizer.fit_transform(file_contents_generator(corpus, encoding))
	return [
		feature.strip() 
		for feature in vectorizer.get_feature_names() 
		if feature.strip()
	]

"""
Calculates the set intersection of two lists:
	list_1 (list): Data input
	list_2 (list): Data input
	return (set): Intersection of the two lists (repeats excluded)
"""
def get_list_intersection(list_1, list_2):
	return set(list_1) & set(list_2)

"""
Outputs the results to a text file
	noun_list (list [str]): The noun list from MeCab
	vocab_list (list [str]): The vocabulary list from sklearn
	intersection (set [str]): The set intersection of the above two lists
	encoding (str): Encoding to use when writing the output file
"""
def output_results(noun_list, vocab_list, intersection, encoding, output_path):
	with open(output_path, "wb") as handle:
		output_section(handle, NOUN_LIST_HEADER, noun_list, encoding)
		output_section(handle, VOCAB_LIST_HEADER, vocab_list, encoding)
		output_section(handle, INTERSECTION_HEADER, intersection, encoding)

"""
Helper function for writing each of the three results sections
	handle (io.BufferedWriter): Object that writes to the output file location
	header (str): Text header for this section
	item_list (list [str]): Strings to write line-by-line
	encoding (str): Encoding to use when writing the output file
"""
def output_section(handle, header, item_list, encoding):
	handle.write((header + "\n").encode(encoding))
	for item in item_list:
		handle.write((item + "\n").encode(encoding))

"""
Parses the MeCab nouns and sklearn vocabulary from a corpus, calculates their intersection, and outputs all data to a .txt file
	input_directory (str): Path to a folder containing the .txt files to be used for the corpus
	input_encoding (str): Encoding to use when parsing the input files
	output_encoding (str): Encoding to use when writing the output file
	output_path (str): Path to write the output to
"""
def interesect_mecab_noun_list_and_sklearn_vocab_list(input_directory=DEFAULT_INPUT_DIRECTORY, input_encoding=DEFAULT_INPUT_ENCODING, 
														output_encoding=DEFAULT_OUTPUT_ENCODING, output_path=DEFAULT_OUTPUT_PATH):
	corpus = [
		join(input_directory, child) 
		for child in listdir(input_directory) 
		if isfile(join(input_directory, child))
	]
	noun_list = get_noun_list(corpus, input_encoding)
	vocab_list = get_vocab_list(corpus, input_encoding)
	intersection = get_list_intersection(noun_list, vocab_list)
	output_results(noun_list, vocab_list, intersection, output_encoding, output_path)

"""
Argument parsing from the command line

usage: japanese_nlp.py [-h] [-ie INPUT_ENCODING] [-oe OUTPUT_ENCODING]
                       [-op OUTPUT_PATH] [-id INPUT_DIRECTORY]

Solution to Python Homework for Innovatech Studio - by Kevin Edelmann

optional arguments:
  -h, --help            show this help message and exit
  -ie INPUT_ENCODING, --input_encoding INPUT_ENCODING
                        Output encoding. Default is '{INPUT_ENCODING}'.
  -oe OUTPUT_ENCODING, --output_encoding OUTPUT_ENCODING
                        Output encoding. Default is '{OUTPUT_ENCODING}'.
  -op OUTPUT_PATH, --output_path OUTPUT_PATH
                        Output file destination. Default is
                        '{OUTPUT_PATH}'.
  -id INPUT_DIRECTORY, --input_directory INPUT_DIRECTORY
                        Path to a folder containing the .txt files to be used
                        for the corpus. Default is '{INPUT_DIRECTORY}'
"""
if __name__ == "__main__":
	parser = ArgumentParser(description="Solution to Python Homework for Innovatech Studio - by Kevin Edelmann")

	parser.add_argument(
		"-ie", "--input_encoding", 
		help="Input encoding. Default is '{}'.".format(DEFAULT_INPUT_ENCODING), 
		default=DEFAULT_INPUT_ENCODING
	)
	parser.add_argument(
		"-oe", "--output_encoding", 
		help="Output encoding. Default is '{}'.".format(DEFAULT_OUTPUT_ENCODING), 
		default=DEFAULT_OUTPUT_ENCODING
	)
	parser.add_argument(
		"-op", "--output_path", 
		help="Output file destination. Default is '{}'.".format(DEFAULT_OUTPUT_PATH), 
		default=DEFAULT_OUTPUT_PATH
	)
	parser.add_argument(
		"-id", "--input_directory", 
		help="Path to a folder containing the .txt files to be used for the corpus. Default is '{}'".format(DEFAULT_INPUT_DIRECTORY), 
		default=DEFAULT_INPUT_DIRECTORY
	)

	args = parser.parse_args()

	interesect_mecab_noun_list_and_sklearn_vocab_list(
		input_directory=args.input_directory, 
		input_encoding=args.input_encoding, 
		output_encoding=args.output_encoding, 
		output_path=args.output_path
	)