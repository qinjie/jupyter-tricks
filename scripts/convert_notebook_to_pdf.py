import os, glob
import subprocess

def clear_nb(nb_name):
	# Clear notebook output
	subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--inplace", "--ClearOutputPreprocessor.enabled=True", nb_name])


def convert_nb(nb_name, to_type='html'):
	pre, ext = os.path.splitext(nb_name)
	print('\n', nb_name, '==>', pre + '.' + to_type)
	
	# Execute the notebook
	try:
		subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", nb_name])
	except:
		pass

	# Convert jupyter notebooks to HTML file
	# Remove any cell with tag 'hide-cell'
	# remove input cell for cells with tag 'hide-input'
	# Remove input cell for cells with tag 'hide-output'
	subprocess.run(['jupyter', 'nbconvert', '--to', to_type, nb_name,
        "--TagRemovePreprocessor.remove_cell_tags={'hide-cell'}",
        "--TagRemovePreprocessor.remove_input_tags={'hide-input'}",
        "--TagRemovePreprocessor.remove_all_outputs_tags={'hide-output'}"])



if __name__ == '__main__':

	path = os.path.dirname(os.path.realpath(__file__))

	for file in glob.glob("*.ipynb", recursive=True):
		clear_nb(file)
		convert_nb(file)

	for file in glob.glob("*.html", recursive=True):
		fo = file.replace('.html', '.pdf')
		subprocess.run(["wkhtmltopdf", file, fo])
		os.remove(file)
