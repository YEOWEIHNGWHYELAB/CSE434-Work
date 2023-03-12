import pandas as pd
import matplotlib.pyplot as plt
from pydispatch.dispatcher import senders

df = pd.read_csv("sender-ss.csv", names=['time', 'sender', 'retx_unacked', 'retx_cum', 'cwnd', 'ssthresh'])

# exclude the "control" flow
s = df.groupby('sender').size()
df_filtered = df[df.groupby("sender")['sender'].transform('size') > 100]

time_min = df_filtered.time.min()
cwnd_max = 1.1 * df_filtered[df_filtered.time - time_min >= 2].cwnd.max()
dfs = [df_filtered[df_filtered.sender == senders[i]] for i in range(3)]

fig, axs = plt.subplots(len(senders), sharex=True, figsize=(12, 8))
fig.suptitle('CWND over time')

for i in range(len(senders)):
    if i == len(senders) - 1:
        axs[i].plot(dfs[i]['time'] - time_min, dfs[i]['cwnd'], label="cwnd")
        axs[i].plot(dfs[i]['time'] - time_min, dfs[i]['ssthresh'], label="ssthresh")
        axs[i].set_ylim([0, cwnd_max])
        axs[i].set_xlabel("Time (s)");
    else:
        axs[i].plot(dfs[i]['time'] - time_min, dfs[i]['cwnd'])
        axs[i].plot(dfs[i]['time'] - time_min, dfs[i]['ssthresh'])
        axs[i].set_ylim([0, cwnd_max])

plt.tight_layout();
fig.legend(loc='upper right', ncol=2);
