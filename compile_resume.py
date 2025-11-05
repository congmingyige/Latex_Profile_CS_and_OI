#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动从resume-zh_CN.tex中提取\outputFileName变量值，并使用它作为jobname编译
使用方法：python compile_resume.py
"""

import re
import sys
import subprocess
import os

def extract_output_filename(tex_file='resume-zh_CN.tex'):
    """
    从LaTeX文件中提取\outputFileName变量的值
    考虑JobIndex的条件分支
    """
    if not os.path.exists(tex_file):
        print(f"错误：找不到文件 {tex_file}")
        return None
    
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 首先尝试提取JobIndex的值
    job_index_match = re.search(r'\\def\\JobIndex\{(\d+)\}', content)
    job_index = 0
    if job_index_match:
        job_index = int(job_index_match.group(1))
    
    print(f"检测到 JobIndex = {job_index}")
    
    # 查找\ifcase\JobIndex...\or...\or...的模式
    ifcase_section = re.search(r'\\ifcase\\JobIndex(.*?)\\fi', content, re.DOTALL)
    
    if ifcase_section:
        ifcase_content = ifcase_section.group(1)
        # 分割\or和\else
        # 使用更精确的分割，考虑\or和\else
        parts = re.split(r'(\\or|\\else)', ifcase_content)
        
        # 构建case列表：第一个是case 0，然后是\or后的case 1，以此类推
        cases = []
        current_case = []
        
        for i, part in enumerate(parts):
            if part in [r'\or', r'\else']:
                if current_case:
                    cases.append(''.join(current_case))
                    current_case = []
            else:
                current_case.append(part)
        
        if current_case:
            cases.append(''.join(current_case))
        
        # JobIndex对应的case索引
        if job_index < len(cases):
            case_content = cases[job_index]
            filename_match = re.search(r'\\def\\outputFileName\{([^}]+)\}', case_content)
            if filename_match:
                return filename_match.group(1)
        elif len(cases) > 0:
            # 如果超出范围，使用\else分支（最后一个）
            filename_match = re.search(r'\\def\\outputFileName\{([^}]+)\}', cases[-1])
            if filename_match:
                return filename_match.group(1)
    
    # 如果找不到，使用默认值（在\ifcase之前定义的）
    default_match = re.search(r'^\\def\\outputFileName\{([^}]+)\}', content, re.MULTILINE)
    if default_match:
        return default_match.group(1)
    
    return None

def compile_latex(tex_file='resume-zh_CN.tex', jobname=None):
    """
    使用xelatex编译LaTeX文件
    """
    if jobname is None:
        jobname = extract_output_filename(tex_file)
    
    if jobname is None:
        print("错误：无法提取outputFileName，使用默认jobname")
        jobname = os.path.splitext(tex_file)[0]
    
    print(f"提取的文件名：{jobname}")
    print(f"开始编译 {tex_file}，jobname={jobname}...")
    
    # 构建xelatex命令
    cmd = [
        'xelatex',
        f'-jobname={jobname}',
        '-synctex=1',
        '-interaction=nonstopmode',
        '--shell-escape',
        tex_file
    ]
    
    try:
        # 执行编译（需要运行两次以确保交叉引用正确）
        result1 = subprocess.run(cmd, check=False, capture_output=True, text=True)
        result2 = subprocess.run(cmd, check=False, capture_output=True, text=True)
        
        if result1.returncode == 0 and result2.returncode == 0:
            print(f"✓ 编译成功！输出文件：{jobname}.pdf")
            return True
        else:
            print(f"✗ 编译失败")
            if result2.stderr:
                print("错误信息：")
                print(result2.stderr)
            return False
    except FileNotFoundError:
        print("错误：找不到xelatex命令，请确保已安装TeX发行版并配置PATH")
        return False
    except Exception as e:
        print(f"错误：{e}")
        return False

if __name__ == '__main__':
    # 支持命令行参数指定tex文件
    tex_file = sys.argv[1] if len(sys.argv) > 1 else 'resume-zh_CN.tex'
    compile_latex(tex_file)

