
jupyter nbconvert --to html *.ipynb

setlocal EnableExtensions EnableDelayedExpansion
set SEARCHTEXT=.html
set REPLACETEXT=.pdf

for /r %%i in (*.html) do (
    call set string=%%i
    call set modified=%%string:%SEARCHTEXT%=%REPLACETEXT%%%
	echo %modified%
    wkhtmltopdf %%i %modified%
)

