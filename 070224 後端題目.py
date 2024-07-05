import json

#assume file name is trades.json
filename = 'trades.json'
with open(filename, 'r') as file:
    data = json.load(file)

#extract the relevant 'data' part
trades = data['data']

balance = 8000
total_pnl = 0
wins = 0
losses = 0
total_trades = 0
cumulative_pnl = [] #need for max_drawdown
net_pnl_list = []   #store each net_pnl for profit factor

#calculate net PnL base on the given file and it's format
for row in trades:
    fill_pnl = float(row['fillPnl'])
    fee = float(row['fee'])
    net_pnl = fill_pnl - fee
    net_pnl_list.append(net_pnl)
    cumulative_pnl.append(total_pnl + net_pnl)
    total_pnl += net_pnl
    total_trades += 1
    if net_pnl > 0:
        wins += 1
    elif net_pnl < 0:
        losses += 1

#roi
roi = (total_pnl / balance) * 100

#win_rate
win_rate = (wins / total_trades) * 100 if total_trades > 0 else 0

#max_drawdown
max_drawdown = 0
for i, pnl in enumerate(cumulative_pnl):
    max_cumulative = max(cumulative_pnl[:i+1])
    drawdown = max_cumulative - pnl
    if drawdown > max_drawdown:
        max_drawdown = drawdown

#odds_ratio
odds_ratio = (wins / losses) if losses > 0 else 0

#profit_factor
total_profit = sum(pnl for pnl in net_pnl_list if pnl > 0)
total_loss = -sum(pnl for pnl in net_pnl_list if pnl < 0)
profit_factor = (total_profit / total_loss) if total_loss > 0 else 0

#sharpe_ratio
risk_free_rate = 0.01
daily_returns = [pnl / balance for pnl in net_pnl_list]
mean_daily_return = sum(daily_returns) / len(daily_returns) if daily_returns else 0

if len(daily_returns) > 1:
    variance = sum((r - mean_daily_return) ** 2 for r in daily_returns) / (len(daily_returns) - 1)
    std_daily_return = variance ** 0.5
else:
    std_daily_return = 0

sharpe_ratio = (mean_daily_return - risk_free_rate) / std_daily_return if std_daily_return > 0 else 0


# Print results
print(f"ROI: {roi:.2f}%")
print(f"Win Rate: {win_rate:.2f}%")
print(f"Maximum Drawdown (MDD): {max_drawdown:.2f} USDT")
print(f"Odds Ratio: {odds_ratio:.2f}")
print(f"Profit Factor: {profit_factor:.2f}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")