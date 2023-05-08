import numpy as np
import pandas as pd
from finta import TA
import utilities.utils as utils




def delta(data=None, period=1):             # Working Fine
    """
    Function to calculate  difference between each row and the row behind it by n=period number of days.
    :param data: Stock Data. pd.Dataframe is applicable
    :param period: The period for which difference in features is to be obtained.
    :return: Dataframe with delta calculated for each numerical feature and initial n=period number of rows will be filled with np.nan
    """
    if data is None:
        return "You have not given data, please provide data in form of pandas dataframe"
    # elif str(type(data)) is not "<class 'pandas.core.frame.DataFrame'>":
    #     return "The input given is not of type pandas dataframe"

    return data - data.shift(period)


def moving_average(data=None, period=2):             # Working Fine
    """
    Function to calculate average between each row and all the rows behind it by n=period number of days or less.
    :param data: Stock Data. pd.Dataframe is applicable
    :param period: The period for which average in features is to be obtained.
    :return: Dataframe with moving_average calculated for each numerical feature and initial n=period number of rows will be filled with np.nan
    """
    if data is None:
        return "You have not given data, please provide data in form of pandas dataframe"
    # elif str(type(data)) is not "<class 'pandas.core.frame.DataFrame'>":
    #     return "The input given is not of type pandas dataframe"

    return data.rolling(period).mean()


def mcginley_dynamic_average(data=None, lookback=20, feature=None, return_list=False):             # Working Fine
    """
    Function to calculate mcginley dynamic average between each row and all the rows behind it by n=period number of days or less.
    :param data: Stock Data. pd.Dataframe is applicable
    :param lookback: The lookback period.
    :param feature: The feature on which mcginley dynamic average is to be calculated. Supposed to be numerical in nature.
    :return: Dataframe with mcginley_dynamic_average calculated for specified numerical feature.
    """
    if data is None:
        return "You have not given data, please provide data in form of pandas dataframe"
    # elif str(type(data)) is not "<class 'pandas.core.frame.DataFrame'>":
    #     return "The input given is not of type pandas dataframe"
    data1 = data.copy().reset_index()
    data1['mcginley_avg'] = np.zeros(data1.shape[0])
    data1.loc[0, 'mcginley_avg'] = data1.loc[0, feature]
    for idx in range(1, (data1.shape[0])):
        if data1.loc[idx - 1, 'mcginley_avg'] == 0:
            data1.loc[idx, 'mcginley_avg'] = data1.loc[idx, feature]

        elif data1.loc[idx - 1, 'mcginley_avg'] > 0:
            data1.loc[idx, 'mcginley_avg'] = data1.loc[idx - 1, 'mcginley_avg'] + (
                        (data1.loc[idx, feature] - data1.loc[idx - 1, 'mcginley_avg']) / (
                        0.6 * lookback * (data1.loc[idx, feature] / data1.loc[idx - 1, feature]) ** 4))

    if return_list is False:
        return data1
    elif return_list is True:
        return data1['mcginley_avg'].values

    return None


def get_atr(data=None, period=10):           # Working Fine
    tr1 = data['high'] - data['low']
    tr2 = data['high'] - data['close'].shift(1)
    tr3 = data['low'] - data['close'].shift(1)

    dt = pd.DataFrame({'tr1': tr1, 'tr2': tr2, 'tr3': tr3}).max(axis=1)
    atr= dt.rolling(period).mean()

    return atr.values


def supertrend(data=None, multiplier=2, period=10):    # Working Fine but ideation is to be improved

    hl2 = (data['high'] + data['low']) / 2

    data['atr'] = get_atr(data, period=period)

    # upperband and lowerband calculation
    # notice that final bands are set to be equal to the respective bands
    final_upperband = upperband = hl2 + (multiplier * data['atr'])
    final_lowerband = lowerband = hl2 - (multiplier * data['atr'])

    # initialize Supertrend column to True
    supertrend = [True] * len(data)

    for i in range(1, len(data.index)):
        curr, prev = i, i - 1

        # if current close price crosses above upperband
        if data['close'][curr] > final_upperband[prev]:
            supertrend[curr] = True
        # if current close price crosses below lowerband
        elif data['close'][curr] < final_lowerband[prev]:
            supertrend[curr] = False
        # else, the trend continues
        else:
            supertrend[curr] = supertrend[prev]

            # adjustment to the final bands
            if supertrend[curr] == True and final_lowerband[curr] < final_lowerband[prev]:
                final_lowerband[curr] = final_lowerband[prev]
            if supertrend[curr] == False and final_upperband[curr] > final_upperband[prev]:
                final_upperband[curr] = final_upperband[prev]

        # to remove bands according to the trend direction
        if supertrend[curr] is True:
            final_upperband[curr] = np.nan
        else:
            final_lowerband[curr] = np.nan

    return pd.DataFrame({
        'Supertrend': supertrend,
        'Final Lowerband': final_lowerband,
        'Final Upperband': final_upperband,
        'upperband': upperband,
        'lowerband': lowerband
    }, index=data.index)


def exponential_moving_average(data, period=10):
    return TA.EMA(data, period).values

