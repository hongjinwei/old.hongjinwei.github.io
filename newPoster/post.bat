del main.json
del backup\main.json

xcopy ..\main.json .
del ..\main.json
xcopy ..\main.json backup\

python poster.py

xcopy main.json ..\