# Documentation Fuzzy Trader

Fuzzy Trader is an app mixed investment portfolio developed on **Flask/ React** technologies. The main features are related to search, buy and access investments by consulting a previous price. In short, you can simulate how much do you wanna apply and receive all the investments available.  

![Alt Text](https://media.giphy.com/media/SVs1myKhQKNQmG5RK5/giphy.gif)
 -
 ## Table of contents
 * **[Requirements](#requirements)**
 * **[Install](#install)**
* **[Architecture](#architecture)**
* **[Endpoints](#endpoints)**
* **[ExploratoryTests](#tests)**

# Requirements

 - Python3
 - Pip3

# Install

```
$ git clone https://github.com/fuzzyTraderBx/fuzzy_trader_back
```
```
$ cd fuzzy_trader_back
```
```
$ pip install -r requirements.txt
```
```
$ python app.py
```

# Architecture

Below is a schematic of how the solution was thought, according to the peculiarities of each chose technology:

![Imgur](https://i.imgur.com/YwotRxs.png)


# Endpoints
|Method| Path | Body | Response |
|--|--|--|--|
| POST | /signup |  email, password, name | id, name, email
| POST | /login |  email, password | access_token, user
| GET | /list_investments/<max_price> | - | list of investments (name, value, is_criptocurrency) |
| POST | /investments/<user_id> | investment_key | status code |
| GET | /investments/<user_id> | - | total and list of investments of the user |

# Tests
## Exploratory Tests with Tourist Metaphor

It's possible to verify informations about that approach at the scientific paper cited bellow: 

```
@inproceedings{fazzolino2019validation,
  title={Validation process for services produced by digital transformation},
  author={Fazzolino, Rafael and Vincenzi, Auri Marcelo Rizzo and Silva, Sara and de Souza, Let{\'\i}cia and Figueiredo, Rejane MC and Ramos, Cristiane Soares and Ribeiro, Luiz Carlos Miyadaira},
  booktitle={Proceedings of the 29th Annual International Conference on Computer Science and Software Engineering},
  pages={354--364},
  year={2019}
}

```

The test cases were created according to each tour and have the following structure:

[![dsjojR.png](https://iili.io/dsjojR.png)](https://freeimage.host/br)

![dshDYu.md.png](https://iili.io/dshDYu.md.png)

![dsjK3F.md.png](https://iili.io/dsjK3F.md.png)
