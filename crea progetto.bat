@echo off
type nul > main.py
mkdir classi
cd classi
type nul > __init__.py
echo "--------------------------"

set /p n="Inserisci il numero dei file da creare: "

setlocal enabledelayedexpansion
SET VAR=Hello
FOR /L %%a in (1,1,%n%) do (
 set /p s="Inserisci il NOME del file da creare: "
type nul > !s!.py

)
endlocal

 set /p n="clicca Invio per uscire, i file sono stati creati ^_^   "