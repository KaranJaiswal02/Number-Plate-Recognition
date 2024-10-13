@echo off
setlocal

REM Define directories
set "TRAINING_DIR=D:\Edge Downloads\Number-Plate-Recognition-Using-OpenCV-main\dataset\images"
set "OUTPUT_DIR=D:\Edge Downloads\Number-Plate-Recognition-Using-OpenCV-main\dataset"
set "LANG=custom_lang"

REM Ensure Tesseract is accessible
set "TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe"
set "TESSDATA_PREFIX=C:\Program Files\Tesseract-OCR\tessdata"

REM Combine the box and image files into .lstmf files
for %%f in ("%TRAINING_DIR%\*.jpg") do (
    "%TESSERACT_PATH%" "%%f" "%%~nf" --psm 6 lstm.train
)

REM Create a list of training files
dir /b "%TRAINING_DIR%\*.lstmf" > "%TRAINING_DIR%\list.train"

REM Check if the list file was created successfully
if not exist "%TRAINING_DIR%\list.train" (
    echo Error: Unable to create list file.
    exit /b 1
)

REM Train the model
lstmtraining ^
  --model_output "%OUTPUT_DIR%\%LANG%.traineddata" ^
  --train_listfile "%TRAINING_DIR%\list.train" ^
  --traineddata "%TESSDATA_PREFIX%\eng.traineddata" ^
  --net_spec "[Lfx256 O1c]" ^
  --target_error_rate 0.01 ^
  --max_iterations 1000

endlocal
