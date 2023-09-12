
# S Parameter Generator

LynxAI, Inc

Connect us at support@lynxai.io


## Introduction
Generation of S Parameter files using two reference S parameter files. The reference files correspond to different physical routing attributes such as signal width, signal spacing and use of shields to reduce coupling between nets.
## Background

In order to meet the electrical timing requirements on high performance chiplets, the signal integrity analysis of the channel is required. This requires 2.5D or 3D extraction of S Parameters from the interconnect layout. The overall design optimization cycle could be time consuming and are limited to certain critical signals or topologies
## LynxAI's Solution

LynxAI's solution uses two reference S parameters that correspond to different routing strategies, along with the key routing parameters such as signal width, signal space,  etc. 
The application then generates additional S Parameters using different combination of routing parameters. The benefit here is that simulations can be run with the generated parameters without having to wait for a full 2.5D extraction.
The accompanying pdf illustrates the inputs required to run the application.
[S Parameter Generator](https://github.com/lynxai-eng/S_Parameter_Generator/blob/main/S_Parameter_Generator.pdf)
## Installation
- Python3.9 required
- This is a Linux release of LynxAI app. Please contact LynxAI for other OS support at support@lynxai.io

clone repository

```bash
    git clone https://github.com/lynxai-eng/S_Parameter_Generator.git
```

install packages 
```bash
    cd S_Parameter_Generator
    pip install -r requirements.txt
```

## Usage/Examples

Input file Example

| file_name| Signal_width|Shield_width|Signal_to_shield_spacing|
| ----------------- | ---|------------|----------------------- |
| file_info     |input|input|input|
| Example_1.s4p | 0.8 | 0.4 | 2.4 |
| Example_2.s4p | 2 | 0 | 2 |

-  Execute following command to run the app

```bash
    python3 S_Parameter_Generator.py -s ./example/s_file.csv
```
- After execution new folder will be created as follows: 
```bash
    s-gen{n}    // example s-gen1,s-gen2....
```
- In this folder have s Parameter files, all are auto generated
 
![Logo](https://lynxai.io/wp-content/uploads/2021/11/AynxAi-Logo-design-final-min-1536x1536-1.png)


## Feedback

If you have any feedback, please reach out to us at support@lynxai.io

