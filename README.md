# 不同分支的介绍和使用
- OI分支：编程竞赛（比如找编程竞赛教练的工作），参见 resume-zh_CN.tex 和 resume-zh_CN.pdf
- CS分支：计算机软件开发/C++开发/后端（比如找一些大中厂的工作），参见 resume-zh_CN.tex 和 resume-zh_CN.pdf
- **使用**:
  - GitHub
    ````
    fork一下
    git clone https://github.com/你的用户名/你的项目.git
    git checkout CS 或者 git checkout OI (选择某个分支)
    git remote set-url origin https://github.com/你的用户名/你的项目.git

    git checkout CS
    git add -A
    git commit -m "你的用户名(你的邮箱)"
    git push https://github.com/你的用户名/你的项目.git CS
    ````
  - TexStudio
    - 运行 resume-zh_CN.tex，生成resume-zh_CN.pdf（有界面）
![陈冠斌_个人简历_2025年6月毕业_CS](陈冠斌_个人简历_2025年6月毕业_CS_Page1.png)
![陈冠斌_个人简历_2025年6月毕业_CS](陈冠斌_个人简历_2025年6月毕业_CS_Page2.png)
![陈冠斌_个人简历_2025年6月毕业_OI](陈冠斌_个人简历_2025年6月毕业_OI.png)

# 自动化脚本
- python script.py
  - 1. PDF修改名字
  - 2. PDF转为PNG
  - 3. 删除一下PNG的部分内容（然后你可以在小红书请教一下人）

# 心得
- 要用数据说话，要写出有震撼力的东西，粗体标注，比如"博客阅读量26万，随笔500篇"。
- 一些比较长的语句，说实话，可能你感觉自己很有感觉，但是可能看的人不care，尽量不重要的地方凝练一下。
- 投什么岗，就要重点展示对应的东西。比如开发所需的技术栈和一些项目开发的经历。
- 平时多参加项目开发(优秀GitHub项目的学习等)，实习(日常实习)。有时候大于很多东西，特别在相对少成果的组。
- 不要觉得你没有什么东西，多从过去的东西找找，并整理和GitHub开源。当然有时间的话，尽量参加一些高质量的东西，自己的东西看起来有点水。比如可以学一下Go和Redis。
- 可以把简历放到实验室同学、小红书那看看，查漏补缺。感谢他们的帮忙！
- 多参加面试，积累经验。这样你才能查漏补缺，补不同的自己没有觉察到的知识点和盲区。多参加一些，哪怕比较困难或者看不上的，都挺好，这些都是宝贵的经历，可以促进你成长的。

# 基于https://hijiangtao.github.io/的修改

- **增加了个人图片（图片在右边），一行个人信息修改为两行个人信息（在图片左边），通过minipage三段的方式以及\textwidth，\vspace，\width参数来修改格式**
- **修改页边距，使得内容在一页范围内，\geometry{a4paper,left=1.5cm,right=1.5cm,top=1.2cm,bottom=1.2cm}**
- **项目修改：基于\textbf{加粗，突出你的关键内容，基于\item一一罗列你的内容**
- 修改了简历顺序（个人总结放前面，注重竞赛，删除了论文和实习经历emmm）
- 多级结构：用若干个\begin{itemize}的方式嵌套。比如"\begin{itemize} \begin{itemize} \begin{itemize}"就有三级结构



# 个人简历

本项目为个人简历 Latex 源码存放，同时包含效果图呈现，简历入口为 resume-zh_CN.tex， 修改自项目 [resume](https://github.com/billryan/resume/)，若不想本地手动编译可以将该源码打包至 zip 直接上传至 ShareLatex 进行在线编译与预览。

## 项目说明

一个优雅的 \LaTeX\ 简历模板, 使用 \XeLaTeX\ 编译, 因为受不了古老的`res`和不太适合作为一页纸简历的`moderncv`, 遂自己动手写了这个模板， 受以下项目启发：

- [zachscrivena/simple-resume-cv](https://github.com/zachscrivena/simple-resume-cv)
- [res](https://www.ctan.org/pkg/res)
- [JianXu's CV](http://www.jianxu.net/en/files/JianXu_CV.pdf)
- [paciorek's CV/Resume template](http://www.stat.berkeley.edu/~paciorek/computingTips/Latex_template_creating_CV_.html)
- [How to write a LaTeX class file and design your own CV (Part 1) - ShareLaTeX](https://www.sharelatex.com/blog/2011/03/27/how-to-write-a-latex-class-file-and-design-your-own-cv.html)

*注：由于使用到 `fontspec` 包，编译器需选择 XeLaTeX。*

## 特性

- 极其容易定制和扩展 (`res`模板中枪倒地...)
- 完善的 Unicode 字体支持, 因为用的是 \XeLaTeX\ 嘛
- 完美的中文支持，使用 Adobefonts
- 支持 FontAwesome 4.3.0 (目前还不支持使用别名)

### 效果输出

![resume-zh_CN.png](./resume.preview.png)

## 使用方法

1. OverLeaf 在线编译
2. 使用较新的 \LaTeX\ 发行版在本地计算机编译

如果确定只需要中文简历的话单独克隆 `master` 分支即可, 需要注意的是该分支包含 Adobe 的宋楷黑仿四套中文字体，压缩包约为37MB。[下载地址](https://github.com/hijiangtao/resume/releases)

```
git clone https://github.com/hijiangtao/resume.git --branch master --depth 1 --single-branch <folder>
```

如果系统已确定安装有 Adobe 的四套中文字型，在文档的开始处使用包`zh_CN-Adobefonts_internal`, 如果没有安装则使用包`zh_CN-Adobefonts_external`, 在 ShareLaTeX 上编译需要使用包`zh_CN-Adobefonts_external`.

其他具体使用可参考给出的范例，都是极其简单易懂的宏，建议先看看 [How to write a LaTeX class file and design your own CV (Part 1) - ShareLaTeX](https://www.sharelatex.com/blog/2011/03/27/how-to-write-a-latex-class-file-and-design-your-own-cv.html) 和 [How to write a LaTeX class file and design your own CV (Part 2) - ShareLaTeX](https://www.sharelatex.com/blog/2013/06/28/how-to-write-a-latex-class-file-and-design-your-own-cv.html) 了解下该模板的简单背景，下面就一些新定义的宏做简要介绍。

### 宏

- `\name`: 姓名
- `\contactInfo`: 联系信息, 需要三项信息，分别是{邮箱}{手机号}{个人主页}
- `\basicContactInfo`: 简要的联系信息, 需要 项信息, 分别是{邮箱}{手机号}, 没有个人主页的用这个
- `\section`: 用于分节, 如教育背景, 实习/项目经历等
- `\subsection`: 用于小节标题, 无日期选项
- `\datedsubsection`: 用于小节标题, 简历中使用最广，第二项为时间区间，自动右对齐
- `\itemize`: 清单列表，简历中应用最广
- `\enumerate`: 枚举列表，数字标号

### FontAwesome

首先在 [Font Awesome Icons](http://fortawesome.github.io/Font-Awesome/icons/) 上选中自己想使用的图标(暂不支持 alias)，然后在 [fontawesome.sty](https://github.com/billryan/resume/blob/zh_CN/fontawesome.sty) 中找到相应的宏, 将其作为普通文本一样使用。

其他的可以自行参考相应 cls 和 tex 文件。

## License

[The MIT License (MIT)](http://opensource.org/licenses/MIT)

Copyrighted fonts are not subjected to this License.
