<h1 align="center">
  <br>
  <a href="https://github.com/Crocodile-Coding-Club/ldtklib"><img src="https://raw.githubusercontent.com/Crocodile-Coding-Club/ldtklib/refs/heads/main/LDtklib.png" alt="LDtklib logo" width="2301px"></a>
</h1>

<p align="center">
  <a href="https://github.com/Crocodile-Coding-Club/ldtklib/commits/main/"><img src="https://img.shields.io/github/last-commit/Crocodile-Coding-Club/ldtklib?style=for-the-badge"></a>
  <a href="https://github.com/Crocodile-Coding-Club/ldtklib/releases/latest"><img src="https://img.shields.io/github/v/release/Crocodile-Coding-Club/ldtklib?style=for-the-badge"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Language-Python-FFD43B?style=for-the-badge"></a>
  <a href="https://flit.pypa.io/en/stable/"><img src="https://img.shields.io/badge/Tool-Flit-31c79a?style=for-the-badge"></a>
  <a href="https://en.wikipedia.org/wiki/MIT_License"><img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge"></a>
</p>

<h2 align="center">An unofficial python package that can read <a href="https://ldtk.io/">LDtk's</a> .ldtk files.</h2>

## Table of Contents
- [About](#rocket-about)
- [License](#page_with_curl-license)
- [How to Build](#construction-how-to-build)
- [Install LDtklib](#arrow_down-install-ldtklib)

## :rocket: About

**LDtklib** is an unofficial python package that can read .ldtk files that are generated by the LDtk level editor.  
This project is founded by [@dalmatheo](https://github.com/dalmatheo), a French developer that is part of the Crocodile Coding Club, which is a coding club in France. Here are the goals of the project:

- **Usability**: We want this library to be usable by everyone and anyone, not regarding the tool that they use to render graphics. To do that, we will not create methods to display the content, but classes to extract the content data and make the package user able to use that data easily.
- **Performance**: We want the project to be performant because it will be at the core of multiple games, which means that we will have to refactor the code and optimize it often.
- **Maintainability**: Dispite wanting to make the project performant, we also have to make the code readable and easy to understand so that anyone that wants to contribute to the project, or fork it can easily edit the code of the package.

## :page_with_curl: License

This project is available under the [MIT license](https://en.wikipedia.org/wiki/MIT_License). You can review the full license agreement at the following link: [The MIT License](https://opensource.org/license/mit).

## :construction: How to Build

To build LDtklib you will have to follow theses steps:

### Installing Flit

Flit is a simple tool that makes you able to build python packages, and to publish them to Pypi. To install it, you will have to execute this command in your terminal:

```shell
pip install flit
```

### Clone the repository

Then, you'll have to clone the repository to get the source code on your machine and you'll have to open the directory in your terminal.

```shell
git clone https://github.com/Crocodile-Coding-Club/ldtklib
cd ldtklib
```

### Build the project

Finally, you'll have to execute the command to build the project.

```shell
flit build
```


## :arrow_down: Install LDtklib

### Install it from Pypi

LDtk is currently not available on pypi.org.

### Install it from the latest Github release

You will find in [that page](https://github.com/Crocodile-Coding-Club/ldtklib/releases/latest) the latest release of LDtklib. This release contain the .whl file that you need to get the package locally. Download it and run in your download directory:

```shell
pip install ./file.whl
```

### Install it from a local build

You can [build the package](#construction-how-to-build) to then install it by using this command:
```shell
pip install ./dist/file that was created.whl
```
