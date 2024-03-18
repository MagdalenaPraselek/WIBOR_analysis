#author: Magdalena Prasełek

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
sns.set_palette('pastel')

df_raw_6M = pd.read_csv(r'C:\Users\prius\OneDrive\Pulpit\Data Analysis Projects\Wibor\plopln6m_d.csv', index_col = 'Data')
df_6M = df_raw_6M['Zamkniecie'].copy()
df_6M.rename('6M', inplace = True)

df_raw_3M = pd.read_csv(r'C:\Users\prius\OneDrive\Pulpit\Data Analysis Projects\Wibor\plopln3m_d.csv', index_col = 'Data')
df_3M = df_raw_3M['Zamkniecie'].copy()
df_3M.rename('3M', inplace = True)

df_raw_1M = pd.read_csv(r'C:\Users\prius\OneDrive\Pulpit\Data Analysis Projects\Wibor\plopln3m_d.csv', index_col = 'Data')
df_1M = df_raw_1M['Zamkniecie'].copy()
df_1M.rename('1M', inplace = True)


df_raw_inflation = pd.read_csv(r'C:\Users\prius\OneDrive\Pulpit\Data Analysis Projects\Wibor\cpiypl_m_m.csv', index_col = 'Data')
df_inflation = df_raw_inflation['Zamkniecie'].copy()
df_inflation.rename('Inflation', inplace = True)

df_raw_interest_rate = pd.read_csv(r'C:\Users\prius\OneDrive\Pulpit\Data Analysis Projects\Wibor\inrtpl_m_d.csv', index_col = 'Data')
df_interest_rate = df_raw_interest_rate['Zamkniecie'].copy()
df_interest_rate.rename('Interest rate', inplace = True)


df = pd.concat([df_6M, df_3M, df_1M, df_inflation, df_interest_rate], axis = 1)
df = df.reset_index()




df.Data = pd.to_datetime(df['Data'])
df.rename(columns = {'Data': 'Date'}, inplace = True)
date_ticks = np.array(['2014-01-02', '2016-01-02', '2018-01-02', '2020-01-02', '2022-01-02', '2023-12-29'])
date_ticks_labels = ['2014', '2016', '2018', '2020', '2022', '2024']

print(df.info())
sns.set_context('poster', font_scale = 1)

#Figure 1
fig1, ax1 = plt.subplots(3)
fig1.suptitle('WIBOR indicators comparsion')
fig1.set_figwidth(13)
fig1.set_figheight(10)
plt.subplots_adjust(hspace = 0.6)


plt.setp(ax1, xticks = pd.to_datetime(date_ticks), xticklabels = date_ticks_labels, xlabel = 'Year')

sns.lineplot(df, x = 'Date', y = '6M', ax = ax1[0])
sns.lineplot(df, x = 'Date', y = '3M', ax = ax1[1])
sns.lineplot(df, x = 'Date', y = '1M', ax = ax1[2])

#Figure 2
fig2 = plt.figure()
fig2.suptitle('WIBOR indicators comparsion')
fig2.set_figwidth(13)
fig2.set_figheight(10)
sns.lineplot(df, x = 'Date', y = '6M', label = '6M')
plt.legend()
sns.lineplot(df, x = 'Date', y = '3M', label = '3M')
plt.legend()
sns.lineplot(df, x = 'Date', y = '1M', label = '1M')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Wibor 6M')




#Figure 3
fig3, ax3 = plt.subplots()
fig3.suptitle('Interest rate and WIBOR')
fig3.set_figwidth(13)
fig3.set_figheight(10)
plt.setp(ax3, xlabel = 'Wibor 3M')
sns.lineplot(df, x = 'Date', y = 'Interest rate', label = 'Interest rate')
sns.lineplot(df, x = 'Date', y = '3M', label = 'Wibor 3M')
plt.legend()

#Figure 4
fig4, ax4 = plt.subplots(2)
fig4.suptitle('Factors influencing WIBOR')
fig4.set_figwidth(13)
fig4.set_figheight(10)
plt.subplots_adjust(hspace = 0.4)
plt.setp(ax4, xticks = pd.to_datetime(date_ticks), xticklabels = date_ticks_labels, xlabel = 'Year')
sns.lineplot(df, x = 'Date', y = 'Inflation', ax = ax4[0])
sns.lineplot(df, x = 'Date', y = 'Interest rate', ax = ax4[1])

sns.set_context('paper', font_scale = 1.2)
fig5 = plt.figure()
fig5.set_figwidth(15)
fig5.set_figheight(13)
sns.lmplot(df, x='3M', y='Interest rate')
plt.title('Correlation between interest rate and WIBOR 3M') 
plt.xlabel('Wibor 3M')


