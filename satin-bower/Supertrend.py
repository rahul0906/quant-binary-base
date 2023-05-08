import robin.utils as rutils
import utilities.utils as utils
import math


def backtest_supertrend(data, investment, commission=5, share=0, ):        # Working Fine but needs debugging
    data['Supertrend'] = rutils.supertrend(data)['Supertrend']
    is_uptrend = data['Supertrend']
    close = data['close']

    # initial condition
    in_position = False
    equity = investment
    # commission = 5
    # share = 0
    entry = []
    exit = []

    for i in range(2, len(data)):
        # if not in position & price is on uptrend -> buy
        if not in_position and is_uptrend[i]:
            share = math.floor(equity / close[i] / 100) * 100
            equity -= share * close[i]
            entry.append((i, close[i]))
            in_position = True

        # if in position & price is not on uptrend -> sell
        elif in_position and not is_uptrend[i]:
            equity += share * close[i] - commission
            exit.append((i, close[i]))
            in_position = False

    # if still in position -> sell all share
        if in_position:
            equity += share * close[i] - commission
    earning = equity - investment
    roi = round(earning / investment * 100, 2)
    print(f'Earning from investing $100k is ${round(earning, 2)} (ROI = {roi}%)')
    return entry, exit, roi


def backtest_supertrend_with_mcginley(data, investment, lookback=20, commission=5, share=0):              # Working Fine but needs debugging
    data['Supertrend'] = rutils.supertrend(data)['Supertrend']
    is_uptrend = data['Supertrend']
    close = data['close']
    mcginley = rutils.mcginley_dynamic_average(data, lookback=lookback, feature='close', return_list=True)

    # initial condition
    in_position = False
    equity = investment
    # commission = 5
    # share = 0
    entry = []
    exit = []

    for i in range(2, len(data)):
        # if not in position & price is on uptrend -> buy
        if not in_position and is_uptrend[i] and mcginley[i] > close[i]:
            share = math.floor(equity / close[i] / 100) * 100
            equity -= share * close[i]
            entry.append((i, close[i]))
            in_position = True

        # if in position & price is not on uptrend -> sell
        elif in_position and not is_uptrend[i] and mcginley[i] < close[i]:
            equity += share * close[i] - commission
            exit.append((i, close[i]))
            in_position = False

    # if still in position -> sell all share
    if in_position:
        equity += share * close[i] - commission

    earning = equity - investment
    roi = round(earning / investment * 100, 2)
    print(f'Earning from investing $100k is ${round(earning, 2)} (ROI = {roi}%)')
    return entry, exit, roi


def backtest_supertrend_with_ema_and_mcginley(data, investment, commission=5, share=0, period=10, lookback=20):     # Working Fine but needs debugging
    is_uptrend = rutils.supertrend(data)['Supertrend']
    close = data['close']
    mcginley = rutils.mcginley_dynamic_average(data, lookback=lookback, feature='close', return_list=True)
    ema = rutils.exponential_moving_average(data, period=period)

    # initial condition
    in_position = False
    equity = investment
    # commission = 5
    # share = 0
    entry = []
    exit = []

    for i in range(2, len(data)):
        # if not in position & price is on uptrend -> buy
        if not in_position and is_uptrend[i] and mcginley[i] > close[i] and ema[i] > close[i]:
            share = math.floor(equity / close[i] / 100) * 100
            equity -= share * close[i]
            entry.append((i, close[i]))
            in_position = True

        # if in position & price is not on uptrend -> sell
        elif in_position and not is_uptrend[i] and mcginley[i] < close[i] and ema[i] < close[i]:
            equity += share * close[i] - commission
            exit.append((i, close[i]))
            in_position = False

    # if still in position -> sell all share
    if in_position:
        equity += share * close[i] - commission

    earning = equity - investment
    roi = round(earning / investment * 100, 2)
    print(f'Earning from investing $100k is ${round(earning, 2)} (ROI = {roi}%)')
    return entry, exit, roi

## Triple Bullish Region
def triple_bullish_trend(data, investment, multipliers=None, periods=None):         # Working Fine but needs to be debugged
    is_uptrend1 = rutils.supertrend(data, multiplier= multipliers[0], period=periods[0])['Supertrend']
    is_uptrend2 = rutils.supertrend(data, multiplier= multipliers[1], period=periods[1])['Supertrend']
    is_uptrend3 = rutils.supertrend(data, multiplier= multipliers[2], period=periods[2])['Supertrend']
    close = data['close']

    # initial condition
    in_position = False
    equity = investment
    commission = 5
    share = 0
    entry = []
    exit = []

    for i in range(2, len(data)):
        # if not in position & price is on uptrend -> buy
        if not in_position and is_uptrend1[i] and is_uptrend2[i] and is_uptrend3[i]:
            share = math.floor(equity / close[i] / 100) * 100
            equity -= share * close[i]
            entry.append((i, close[i]))
            in_position = True

        # if in position & price is not on uptrend -> sell
        elif in_position and not is_uptrend1[i] and not is_uptrend2[i] and not is_uptrend3[i]:
            equity += share * close[i] - commission
            exit.append((i, close[i]))
            in_position = False

    # if still in position -> sell all share
    if in_position:
        equity += share * close[i] - commission

    earning = equity - investment
    roi = round(earning / investment * 100, 2)
    print(f'Earning from investing $100k is ${round(earning, 2)} (ROI = {roi}%)')
    return entry, exit, roi


def triple_bullish_with_ema(data, investment, multipliers=None, periods=None, ema_period=200):         # Working Fine but needs to be debugged
    is_uptrend1 = rutils.supertrend(data, multiplier= multipliers[0], period=periods[0])['Supertrend']
    is_uptrend2 = rutils.supertrend(data, multiplier= multipliers[1], period=periods[1])['Supertrend']
    is_uptrend3 = rutils.supertrend(data, multiplier= multipliers[2], period=periods[2])['Supertrend']
    # mcginley = rutils.mcginley_dynamic_average(data, lookback=lookback, feature='close', return_list=True)
    ema = rutils.exponential_moving_average(data, period=ema_period)
    close = data['close']

    # initial condition
    in_position = False
    equity = investment
    commission = 5
    share = 0
    entry = []
    exit = []

    for i in range(2, len(data)):
        # if not in position & price is on uptrend and the 200 day EMA is above the closing price-> buy
        if not in_position and is_uptrend1[i] and is_uptrend2[i] and is_uptrend3[i] and ema[i] > close[i]:
            share = math.floor(equity / close[i] / 100) * 100
            equity -= share * close[i]
            entry.append((i, close[i]))
            in_position = True

        # if in position & price is not on uptrend and the 200 day EMA is below the closing price-> sell
        elif in_position and not is_uptrend1[i] and not is_uptrend2[i] and not is_uptrend3[i] and ema[i] < close[i]:
            equity += share * close[i] - commission
            exit.append((i, close[i]))
            in_position = False

    # if still in position -> sell all share
    if in_position:
        equity += share * close[i] - commission

    earning = equity - investment
    roi = round(earning / investment * 100, 2)
    print(f'Earning from investing $100k is ${round(earning, 2)} (ROI = {roi}%)')
    return entry, exit, roi