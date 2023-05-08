import matplotlib.pyplot as plt


# fig = plt.figure(figsize = (22,13), dpi=360)
# ax = fig.add_subplot(111)
# #ax = new_df.plot(title='Apple Price and BB')
# ax.plot(rutils.mcginley_dynamic_average(data, 20, 'close', True), color='yellow')
# #ax.plot(AAPL_data['Exponential_moving_average'], color='black')
# plt.plot(data['close'].values, linewidth = 1, label='Close Price')
# plt.plot(rutils.supertrend(data)['Final Lowerband'].values,'g', label = 'Final Lowerband')
# plt.plot(rutils.supertrend(data)['Final Upperband'].values, 'r', label = 'Final Upperband')
# #plt.plot(AA)
# ax.fill_between(data.reset_index().index.values, rutils.supertrend(data)['lowerband'].values, rutils.supertrend(data)['upperband'].values, color='red', alpha = 0.4)
#
# ax.grid()
# plt.show()