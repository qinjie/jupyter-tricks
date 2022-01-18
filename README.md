# Jupyter Learning Notes

Some random learning notes about using Jupyter Notebook

## Install Jupyter Notebook

```
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install
```

### Enable Use extensions

```
# zenmode: Give Zenmode functionality to the IPython notebook
jupyter nbextension enable zenmode/main
# Move selected cells: Allow move selected cell(s) using keyboard shortcuts Alt-up and Alt-down
jupyter nbextension enable move_selected_cells/main
# Hinterland: Enable code autocompletion menu for every keypress in a code cell, instead of only enabling it with tab
jupyter nbextension enable hinterland/hinterland
# Table of Contents (2): Enable to collect all running headers and display them in a floating window
jupyter nbextension enable toc2/main
# Runtools: Shortcuts to run multiple cells
jupyter nbextension enable runtools/main
# Tree filter: Search files inside Jupyter Notebook
jupyter nbextension enable tree-filter/index
# Snippet menu: let you insert code and markdown snippets
jupyter nbextension enable snippets/main
# Codefolding: allows code folding in code cells using the shortcut Alt+F
jupyter nbextension enable codefolding/main
```
