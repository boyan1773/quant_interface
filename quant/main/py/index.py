def ema(data, period=9):
<<<<<<< HEAD
    ema_data = data['收盤價'].str.replace(',', '').astype(float).tolist()
    
    smoothing_factor = 2 / (period + 1)
    
    ema = [ema_data[0]]
    
    for i in range(1, len(ema_data)):
        ema.append((ema_data[i] * smoothing_factor) + (ema[i - 1] * (1 - smoothing_factor)))
    
=======
    ema_data = [float(x)for x in data['收盤價']]
    smoothing_factor = 2 / (period + 1)
    ema = [ema_data[0]]
    for i in range(1, len(ema_data)):
        ema.append((ema_data[i] * smoothing_factor) + (ema[i-1] * (1 - smoothing_factor)))
>>>>>>> 7ae95e4c65da82c73c62e44da7f7287e67fcec24
    data['ema'] = ema
    return data

def ma5(data):
<<<<<<< HEAD
    data['ma5'] = round(data['收盤價'].str.replace(',', '').astype(float).rolling(window=5).mean(), 2)
    return data

def ma20(data):
    data['ma20'] = round(data['收盤價'].str.replace(',', '').astype(float).rolling(window=20).mean(), 2)
    return data

def bias(data):
    close = data["收盤價"].str.replace(',', '').astype(float)
    ema = data["ema"].astype(float)
    return round((close - ema) / ema * 100, 2)

def kd(data, window=9, a=3):
    high = data["最高價"].str.replace(',', '').astype(float)
    low = data["最低價"].str.replace(',', '').astype(float)
    close = data["收盤價"].str.replace(',', '').astype(float)
    
    highest_high = high.rolling(window).max()
    lowest_low = low.rolling(window).min()
    
    rsv = ((close - lowest_low) / (highest_high - lowest_low)) * 100
    
    factor = 2 / a
    k_line = [50]
    d_line = [50]
    
    for i in range(len(rsv) - 14):
        k_line.append(round(k_line[i] * factor + (1 - factor) * rsv[i + 14], 2))
        d_line.append(round(d_line[i] * factor + (1 - factor) * k_line[i + 1], 2))
    
    return k_line, d_line

def cdp(data):
    high = data["最高價"].str.replace(',', '').astype(float)
    low = data["最低價"].str.replace(',', '').astype(float)
    close = data["收盤價"].str.replace(',', '').astype(float)
    
    cdp = round((high + low + close * 2) / 4, 2)
    r1 = round((2 * cdp) - low, 2)
    r2 = round(cdp + (high - low), 2)
    s1 = round((2 * cdp) - high, 2)
    s2 = round(cdp - (high - low), 2)
    
    return cdp, r1, r2, s1, s2

def volume_ratio(data):
    volume = data["成交股數"].str.replace(',', '').astype(float)
    volume_ma5 = volume[-5:].mean()
    
    return round((volume.iloc[-1] - volume_ma5) / volume_ma5 * 100, 2)

def rsi(data, period=5):
    close = data["收盤價"].str.replace(',', '').astype(float)
    diff = close.diff(1).dropna()
    
    diff_percent = (diff / close.shift(1)) * 100
    up = diff_percent.where(diff_percent > 0, 0)
    down = -diff_percent.where(diff_percent < 0, 0)
    
    avg_gain = up.rolling(window=period).mean()
    avg_loss = down.rolling(window=period).mean()
    
    rsi = 100 * (avg_gain / (avg_gain + avg_loss))
    
    smooth_rsi = rsi.rolling(window=3).mean().fillna(0)
    
=======
    data['ma5'] = round(data['收盤價'].rolling(window=5).mean(),2)
    return(data)

def ma20(data):
    data['ma20'] = round(data['收盤價'].rolling(window=20).mean(),2)
    return(data)

def bias(data):
    close = data["收盤價"].astype(float)
    ema = data["ema"].astype(float)
    return(round((close-ema)/ema*100,2))

def kd(data , window=9,a=3):
    high = data["最高價"].astype(float)
    low = data["最低價"].astype(float)
    close = data["收盤價"].astype(float)
    highest_high = high.rolling(window).max()
    lowest_low = low.rolling(window).min()
    rsv = ((close - lowest_low) / (highest_high - lowest_low))*100
    factor = 2/a
    k_line = [50]
    d_line = [50]
    for i in range(len(rsv)-14):
        k_line.append(round(k_line[i]*factor+(1-factor)*rsv[i+14],2))
        d_line.append(round(d_line[i]*factor+(1-factor)*k_line[i+1],2))
    return k_line,d_line

def cdp(data):
    high = data["最高價"].astype(float)
    low = data["最低價"].astype(float)
    close = data["收盤價"].astype(float)
    cdp = round((high+low+close*2)/4,2)
    r1 = round((2*cdp)-low,2)
    r2 = round(cdp+(high-low),2)
    s1 = round((2*cdp)-high,2)
    s2 = round(cdp-(high-low),2)
    return(cdp,r1,r2,s1,s2)

def volume_ratio(data):
    volume = data["成交股數"].astype(float)
    volume_ma5=sum(volume[-5:])/5
    return(round((volume.iloc[-1]-volume_ma5)/volume_ma5*100,2))

def rsi(data, period=5):
    close = data["收盤價"].astype(float)
    diff = close.diff(1).dropna()
    diff_percent = (diff/close.shift(1))*100
    up = diff_percent.where(diff_percent > 0, 0)   
    down = -diff_percent.where(diff_percent < 0, 0)
    avg_gain = up.rolling(window=period).mean()
    avg_loss = down.rolling(window=period).mean()
    rsi = 100*(avg_gain/(avg_gain+avg_loss))
    smooth_rsi = rsi.rolling(window=3).mean().where((rsi!=0),0).where((rsi.shift(1)!=0),rsi).where((rsi.shift(2)!=0),rsi)
>>>>>>> 7ae95e4c65da82c73c62e44da7f7287e67fcec24
    return smooth_rsi

def calculate_average_growth_rate(eps_data):
    growth_rates = []
<<<<<<< HEAD
    
    for i in range(1, len(eps_data)):
        growth_rate = ((eps_data[i] - eps_data[i - 1]) / eps_data[i - 1]) * 100
        growth_rates.append(growth_rate)
    
    average_growth_rate = sum(growth_rates) / len(growth_rates) if growth_rates else 0
    return average_growth_rate
=======
    for i in range(1, len(eps_data)):
        growth_rate = ((eps_data[i] - eps_data[i-1]) / eps_data[i-1]) * 100
        growth_rates.append(growth_rate)
    average_growth_rate = sum(growth_rates) / len(growth_rates)
    return average_growth_rate
>>>>>>> 7ae95e4c65da82c73c62e44da7f7287e67fcec24
