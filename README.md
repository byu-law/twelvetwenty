# 12Twenty API Python Accessor
This Python script is used to interact with the [12Twenty API](https://12twenty.freshdesk.com/support/solutions/articles/9000152148-api)

## Latest Release
* v0.2-alpha

## Pre-requisites
* [Python 3.7.x Download](https://www.python.org/downloads/)
* [How to Install Python (Windows, Mac, Linux)](https://realpython.com/installing-python/)

> For Windows: Make sure you click the option "Add Python 3.x to PATH", otherwise you will not be able to run `python` commands from the command line

## Quick Start
* Either clone the repository or [download the latest source-code zip](https://github.com/byu-law/twelvetwenty/archive/v0.1-alpha.zip)
    ```bash
    git clone https://github.com/byu-law/twelvetwenty.git
    ```
    
    > If you downloaded the source-code zip, unzip the files (the following examples assume the files are unzipped in the `~/Downloads` directory)
    
#### Windows
1. In a commmand prompt, or powershell, change your directory (using the `cd` command) into the root directory of the Python script
    ```bash
    cd /d %USERPROFILE%
    cd Downloads\twelvetwenty
    ```
    
2. Use `pip` to install the script requirements (or `pip3` if you have Python 2.x installed)
    ```bash
    pip install -r requirements.txt
    ```
    
3. Run the script using `python` (or `python3` if you have Python 2.x installed)
    ```bash
    python main.py
    ```
    
#### Macintosh
> Note: Mac OS usually has Python 2.x installed native. You will need to run the `python3` and `pip3` commands for the script to work.

* For step 1 and 2, choose a directory in the Terminal app that you know (i.e. `cd ~/Downloads`)

1. After installing Python 3.x, you will also need `pip` by opening the Terminal app and using `curl` to download and install python setuptools
    ```bash 
    curl -O https://bootstrap.pypa.io/ez_setup.py
    python3 ez_setup.py
    ```

2. Next you will install `pip3` also using `curl`
    ```bash
    curl -O https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py
    ```
    
3. Change directory into the root of the Python script
    ```bash
    cd ~/Downloads/twelvetwenty/
    ```

4. Use `pip3` to install the script requirements
    ```bash
    pip3 install -r requirements.txt
    ```
    
5. Run the script using `python3`
    ```bash
    python3 main.py
    ```

#### Linux
1. Use a terminal to change directory into the root of the Python script
    ```bash
    cd ~/Downloads/twelvetwenty/
    ```
    
2. Use `pip` to install the script requirements (or `pip3` if you have Python 2.x installed)
    ```bash
    pip install -r requirements.txt
    ```
    
3. Run the script using `python` (or `python3` if you have Python 2.x installed)
    ```bash
    python main.py
    ```
    
## Example Data Sets
### Table 1:
* [Set 1](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set1.csv)
* [Set 2](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set2.csv)
* [Set 3](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set3.csv)
* [Set 4](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set4.csv)
* [Set 5](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set5.csv)
* [Set 6](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set6.csv)
* [Set 7](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set7.csv)
* [Set 8](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set8.csv)
### Table 2:
* [Set 9](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set9.csv)
* [Set 10](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set10.csv)
* [Set 11](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set11.csv)
* [Set 12](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set12.csv)
* [Set 13](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set13.csv)
* [Set 14](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set14.csv)
* [Set 15](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set15.csv)
* [Set 16](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set16.csv)
### Table 3:
* [Set 17](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set17.csv)
* [Set 18](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set18.csv)
* [Set 19](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set19.csv)
* [Set 20](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set20.csv)
* [Set 21](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set21.csv)
* [Set 22](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set22.csv)
* [Set 23](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set23.csv)
* [Set 24](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set24.csv)
### Table 4:
* [Set 25](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set25.csv)
* [Set 26](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set26.csv)
* [Set 27](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set27.csv)
* [Set 28](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set28.csv)
* [Set 29](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set29.csv)
* [Set 30](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set30.csv)
* [Set 31](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set31.csv)
* [Set 32](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set32.csv)
### Table 5:
* [Set 33](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set33.csv)
* [Set 34](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set34.csv)
* [Set 35](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set35.csv)
* [Set 36](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set36.csv)
* [Set 37](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set37.csv)
* [Set 38](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set38.csv)
* [Set 39](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set39.csv)
* [Set 40](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set40.csv)
### Table 6:
* [Set 41](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set41.csv)
* [Set 42](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set42.csv)
* [Set 43](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set43.csv)
* [Set 44](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set44.csv)
* [Set 45](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set45.csv)
* [Set 46](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set46.csv)
* [Set 47](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set47.csv)
* [Set 48](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set48.csv)
### Table 7:
* [Set 49](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set49.csv)
* [Set 50](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set50.csv)
* [Set 51](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set51.csv)
* [Set 52](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set52.csv)
* [Set 53](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set53.csv)
* [Set 54](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set54.csv)
* [Set 55](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set55.csv)
* [Set 56](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set56.csv)
### Table 8:
* [Set 57](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set57.csv)
* [Set 58](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set58.csv)
* [Set 59](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set59.csv)
* [Set 60](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set60.csv)
* [Set 61](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set61.csv)
* [Set 62](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set62.csv)
* [Set 63](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set63.csv)
* [Set 64](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set64.csv)
### Table 9:
* [Set 65](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set65.csv)
* [Set 66](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set66.csv)
* [Set 67](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set67.csv)
* [Set 68](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set68.csv)
* [Set 69](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set69.csv)
* [Set 70](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set70.csv)
* [Set 71](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set71.csv)
* [Set 72](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set72.csv)
### Table 10:
* [Set 73](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set73.csv)
* [Set 74](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set74.csv)
* [Set 75](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set75.csv)
* [Set 76](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set76.csv)
* [Set 77](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set77.csv)
* [Set 78](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set78.csv)
* [Set 79](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set79.csv)
* [Set 80](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set80.csv)
### Table 11:
* [Set 81](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set81.csv)
* [Set 82](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set82.csv)
* [Set 83](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set83.csv)
* [Set 84](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set84.csv)
* [Set 85](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set85.csv)
* [Set 86](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set86.csv)
* [Set 87](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set87.csv)
* [Set 88](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set88.csv)
### Table 12:
* [Set 89](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set89.csv)
* [Set 90](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set90.csv)
* [Set 91](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set91.csv)
* [Set 92](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set92.csv)
* [Set 93](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set93.csv)
* [Set 94](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set94.csv)
* [Set 95](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set95.csv)
* [Set 96](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set96.csv)
### Table 13:
* [Set 97](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set97.csv)
* [Set 98](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set98.csv)
* [Set 99](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set99.csv)
* [Set 100](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set100.csv)
* [Set 101](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set101.csv)
* [Set 102](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set102.csv)
* [Set 103](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set103.csv)
* [Set 104](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set104.csv)
### Table 14:
* [Set 105](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set105.csv)
* [Set 106](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set106.csv)
* [Set 107](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set107.csv)
* [Set 108](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set108.csv)
* [Set 109](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set109.csv)
* [Set 110](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set110.csv)
* [Set 111](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set111.csv)
* [Set 112](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set112.csv)
### Table 15:
* [Set 113](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set113.csv)
* [Set 114](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set114.csv)
* [Set 115](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set115.csv)
* [Set 116](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set116.csv)
* [Set 117](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set117.csv)
* [Set 118](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set118.csv)
* [Set 119](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set119.csv)
* [Set 120](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set120.csv)
### Table 16:
* [Set 121](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set121.csv)
* [Set 122](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set122.csv)
* [Set 123](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set123.csv)
* [Set 124](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set124.csv)
* [Set 125](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set125.csv)
* [Set 126](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set126.csv)
* [Set 127](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set127.csv)
* [Set 128](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set128.csv)
### Table 17:
* [Set 129](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set129.csv)
* [Set 130](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set130.csv)
* [Set 131](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set131.csv)
* [Set 132](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set132.csv)
* [Set 133](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set133.csv)
* [Set 134](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set134.csv)
* [Set 135](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set135.csv)
* [Set 136](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set136.csv)
### Table 18:
* [Set 137](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set137.csv)
* [Set 138](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set138.csv)
* [Set 139](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set139.csv)
* [Set 140](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set140.csv)
* [Set 141](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set141.csv)
* [Set 142](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set142.csv)
* [Set 143](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set143.csv)
* [Set 144](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set144.csv)
### Table 19:
* [Set 145](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set145.csv)
* [Set 146](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set146.csv)
* [Set 147](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set147.csv)
* [Set 148](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set148.csv)
* [Set 149](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set149.csv)
* [Set 150](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set150.csv)
* [Set 151](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set151.csv)
* [Set 152](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set152.csv)
### Table 20:
* [Set 153](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set153.csv)
* [Set 154](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set154.csv)
* [Set 155](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set155.csv)
* [Set 156](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set156.csv)
* [Set 157](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set157.csv)
* [Set 158](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set158.csv)
* [Set 159](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set159.csv)
* [Set 160](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set160.csv)
### Table 21:
* [Set 161](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set161.csv)
* [Set 162](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set162.csv)
* [Set 163](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set163.csv)
* [Set 164](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set164.csv)
* [Set 165](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set165.csv)
* [Set 166](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set166.csv)
* [Set 167](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set167.csv)
* [Set 168](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set168.csv)
### Table 22:
* [Set 169](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set169.csv)
* [Set 170](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set170.csv)
* [Set 171](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set171.csv)
* [Set 172](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set172.csv)
* [Set 173](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set173.csv)
* [Set 174](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set174.csv)
* [Set 175](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set175.csv)
* [Set 176](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set176.csv)
### Table 23:
* [Set 177](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set177.csv)
* [Set 178](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set178.csv)
* [Set 179](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set179.csv)
* [Set 180](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set180.csv)
* [Set 181](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set181.csv)
* [Set 182](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set182.csv)
* [Set 183](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set183.csv)
* [Set 184](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set184.csv)
### Table 24:
* [Set 185](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set185.csv)
* [Set 186](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set186.csv)
* [Set 187](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set187.csv)
* [Set 188](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set188.csv)
* [Set 189](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set189.csv)
* [Set 190](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set190.csv)
* [Set 191](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set191.csv)
* [Set 192](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set192.csv)
### Table 25:
* [Set 193](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set193.csv)
* [Set 194](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set194.csv)
* [Set 195](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set195.csv)
* [Set 196](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set196.csv)
* [Set 197](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set197.csv)
* [Set 198](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set198.csv)
* [Set 199](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set199.csv)
* [Set 200](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set200.csv)
### Table 26:
* [Set 201](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set201.csv)
* [Set 202](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set202.csv)
* [Set 203](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set203.csv)
* [Set 204](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set204.csv)
* [Set 205](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set205.csv)
* [Set 206](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set206.csv)
* [Set 207](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set207.csv)
* [Set 208](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set208.csv)
### Table 27:
* [Set 209](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set209.csv)
* [Set 210](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set210.csv)
* [Set 211](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set211.csv)
* [Set 212](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set212.csv)
* [Set 213](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set213.csv)
* [Set 214](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set214.csv)
* [Set 215](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set215.csv)
* [Set 216](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set216.csv)
### Table 28:
* [Set 217](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set217.csv)
* [Set 218](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set218.csv)
* [Set 219](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set219.csv)
* [Set 220](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set220.csv)
* [Set 221](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set221.csv)
* [Set 222](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set222.csv)
* [Set 223](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set223.csv)
* [Set 224](https://github.com/byu-law/twelvetwenty/releases/download/v0.2-alpha/set224.csv)