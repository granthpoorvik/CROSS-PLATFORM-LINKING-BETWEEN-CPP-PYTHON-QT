# CROSS –PLATFORM LINKING BETWEEN CPP, PYTHON, QT

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [References used](#references-used)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Output](#output)
- [Contributions](#contributions)
- [License](#license)
- [Contact Information](#contact-information)
- [Acknowledgments](#acknowledgments)

## Introduction

Cross-platform linking between C++, Python, and Qt poses challenges but can be achieved with appropriate approaches. Pybind11 facilitates C++ and Python integration, allowing C++ code exposure as Python modules. Qt provides strong C++ support, enabling seamless integration with its libraries. PyQt and PySide aid Qt and Python integration, utilizing Qt's UI capabilities within Python. Developers must handle platform-specific dependencies, ensuring required libraries are managed during build and deployment. Configuring a build system like CMake correctly is vital for proper compilation and generating platform-specific binaries. API and language compatibility must be maintained to facilitate smooth communication between components. With diligent consideration and leveraging available tools, developers can create unified, cross-platform applications that run seamlessly across different operating systems, providing users with a consistent experience. This integration opens doors for versatile applications with powerful UIs and system-level capabilities.




## References used

-  [PYBind11 documentation](https://pybind11.readthedocs.io/en/stable/)
-  [Pybind11 installation](https://pypi.org/project/pybind11/)
- [OPEN 3D]( https://github.com/isl-org/Open3D)
- [Visual studio code]( https://visualstudio.microsoft.com/downloads/)
- [Qt](https://www.qt.io/download-qt-installer-oss?hsCtaTracking=99d9dd4f-5681-48d2-b096-470725510d34%7C074ddad0-fdef-4e53-8aa8-5e8a876d6ab4)
- [ documentation](https://coderefinery.github.io/mma/03-pybind11/)









## Technologies Used
 -  Visual Studio IDE
-  pybind11
-  cpp
-  python
-  qt application 
- open3d
- numpy python package


### Getting Started

To get the project running on your local machine, follow these steps:

1. ###	Install Visual Studio:
-	Download and install Visual Studio from the official Microsoft website.
-	Choose the appropriate version based on your operating system and requirements.

2. ### Installation steps



#  Pip installations :-
python packages
In terminal 
```cmd
pip install open3d  
pip install numpy
```

# for cpp in visual studio :-through vcpkg
```cmd
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
./bootstrap-vcpkg.sh
./vcpkg integrate install
vcpkg install pybind11:x64-windows
```




 ## Configuration details



1. After  completing the  above steps
2. > In Visual studio code
Under project
	>> Select project_name -> Properties->
  ![Screenshot 1](/1.png)
  Make sure that configuration and platform are set to above config
>> Configuration properties ->c/c++ ->general->Additional Include Directories: -(add the below path)
C:\vcpkg\packages\vtk_x64-windows\include\vtk-9.2
## file struture
![Screenshot 1](/7.png)

---
# some (alternative) steps:
## To directly run the project use the file `final_cross_compiler` which is listed above in repo
## for input files use the file `input_files`
### for source ,target and trans_int_elements field in gui use `input_files`

## Output 
### final_cross_compiler.ui
![Screenshot 1](/2.png)
### Result
Qt GUI Window

![Screenshot 2](/3.png)
### Before applying transformation :
![Screenshot 2](/4.png)
### After applying transformation and IPC stitching:
![Screenshot 2](/5.png)
### The output file 
![Screenshot 2](/6.png)





## Contributions

We welcome contributions from the community. If you want to contribute to the project, please follow these steps:

1. [Include guidelines for contributions]
2. [Explain how to submit pull requests or report issues]

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contact Information

For any questions or feedback, feel free to reach out to us at:
- Email: granth.poorvik@gmail.com
- GitHub: [ GitHub Profile](https://github.com/granthpoorvik)
- linkedin: [profile](https://www.linkedin.com/in/jainpoorvik/)

## Acknowledgments

I would like to acknowledge and express our gratitude to `Central Manufacturing Techenological Institute` [`CMTI`].


