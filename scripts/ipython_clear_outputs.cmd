ECHO OFF
REM clear outputs from all cells

jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace *.ipynb
