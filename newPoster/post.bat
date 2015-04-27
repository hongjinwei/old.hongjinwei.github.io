del main.json
del backup\main.json

xcopy ..\main.json .
xcopy ..\main.json .\backup\

python poster.py

del ..\main.json
xcopy main.json ..\
PAUSE