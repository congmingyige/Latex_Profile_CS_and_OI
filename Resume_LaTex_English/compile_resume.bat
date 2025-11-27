@echo off
chcp 65001 >nul
REM 自动从resume-zh_CN.tex中提取\outputFileName变量值，并使用它作为jobname编译
REM 使用方法：双击此文件或在命令行中运行

set TEX_FILE=resume-zh_CN.tex

REM 使用Python脚本提取文件名并编译
if exist compile_resume.py (
    python compile_resume.py %TEX_FILE%
) else (
    echo 错误：找不到 compile_resume.py
    echo 请确保Python已安装并配置PATH
    pause
)

