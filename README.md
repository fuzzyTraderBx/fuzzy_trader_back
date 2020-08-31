# Documentation Fuzzy Trader

Fuzzy Trader is an app mixed investment portfolio developed on **Flask/ React** technologies. The main features are related to search, buy and access investments by consulting a previous price. In short, you can simulate how much do you wanna apply and receive all the investments available.  

![Alt Text](https://media.giphy.com/media/SVs1myKhQKNQmG5RK5/giphy.gif)
 -
 ## Table of contents
 * **[Requirements](#requirements)**
 * **[Install](#install)**
* **[Architecture](#architecture)**
* **[Endpoints](#endpoints)**

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

