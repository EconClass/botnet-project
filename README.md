# Python Botnet

This project utilizes BYOB (Build Your Own Botnet) framework linked [here](https://github.com/malwaredllc/byob). The purpose of this project is purely educational. In the realm of cyber security there are many features and nuances that contribute to the success or failure of a company's security procedure. By exploring a couple of the possible attack vectors that hackers use, and see them through a hacker's eyes we can create more robust defenses against said attack vectors.

## B.Y.O.B. Modules Used

The BYOB frameworks comes with many modules that can exploit various attack vectors. The modules we will focus on are the following:

|  Module  |   Description   |
|----------|-----------------|
| Miner | Can turn a victim's computer into a cryptocurrency miner |
| Port Scanner | Scans the local network for other online devices & open ports |

By focusing on the selected modules we are able to dive a little deeper into the exploit rather than a broad overview of all of the vectors available through the framework.

## Usage

*NOTE:* The following steps are listed under the assumtion that you are properly using virtual environments either through [pipenv](https://docs.pipenv.org/en/latest/) or [virtualenv](https://virtualenv.pypa.io/en/latest/).

1. Clone Repo
1. Run `pip install -r requirements.txt`
