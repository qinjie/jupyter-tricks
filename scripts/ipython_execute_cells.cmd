ECHO OFF

REM Run all cells in jupyter notebooks and save results
REM --ExecutePreprocessor.timeout=600 extends timeout from 30s to 600s
REM --inplace save result in the same notebook
REM --allow-errors continue execution if any error occurs in a cell. Default it will stop execution of that notebook

jupyter nbconvert --ExecutePreprocessor.timeout=600 --ExecutePreprocessor.iopub_timeout=120 --allow-errors --to notebook --inplace --execute *.ipynb
