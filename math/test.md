# why time series forecasting is a dynamique systeme :

A time series represents a set of data points collected or recorded over time, often with temporal dependencies. These dependencies capture trends, seasonality, and randomness, which are inherently dynamic.
Forecasting models like ARIMA, LSTM, Prophet, or Exponential Smoothing are designed to adapt to the changes in patterns of the data.

![fig 1](image.png)

---
# why we should chose a Past Dateset :

- Use When:

Your focus is on understanding historical trends, building and evaluating models, or performing academic research.
You want a simpler setup for training models without worrying about live data feeds.

- Pros:

Easier to work with since the data is static and well-structured.
Allows for extensive feature engineering and experimentation without the need for real-time infrastructure.

- Cons:

Not suitable for real-time applications like live trading.

- Example Sources:

Publicly available datasets from Kaggle, Quandl, or government resources.
Historical gold price datasets available online.

---
# Understanding ARIMA Models

## What Is ARIMA?
ARIMA stands for **Auto-Regressive Integrated Moving Average**. It’s a statistical model used to analyze and forecast time series data by identifying patterns in past data points.

### Simple Explanation:
ARIMA is like a tool that helps predict the future by:
- Looking at past values (**Auto-Regression** or AR).
- Making the data stable by removing trends (**Integration** or I).
- Correcting errors from past predictions (**Moving Average** or MA).

---

## The Three Parts of ARIMA
1. **Auto-Regressive (AR):**
   - Uses past values to predict the current value.
   - Formula:
     \[
     y_t = \phi_1 y_{t-1} + \phi_2 y_{t-2} + \dots + \phi_p y_{t-p} + \epsilon_t
     \]
     - \( y_t \): Current value
     - \( y_{t-1}, y_{t-2}, \dots \): Past values
     - \( \phi_1, \phi_2, \dots \): Coefficients (weights for past values)
     - \( \epsilon_t \): Random error/noise

2. **Integration (I):**
   - Makes the time series **stationary** (i.e., removes trends).
   - Achieved through **differencing**:
     \[
     y'_t = y_t - y_{t-1}
     \]
     - This can be repeated multiple times if necessary.

3. **Moving Average (MA):**
   - Uses past errors (residuals) to improve predictions.
   - Formula:
     \[
     y_t = \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \dots + \theta_q \epsilon_{t-q} + \epsilon_t
     \]
     - \( \epsilon_{t-1}, \epsilon_{t-2}, \dots \): Past errors
     - \( \theta_1, \theta_2, \dots \): Coefficients for the errors

---

## ARIMA Parameters: \((p, d, q)\)
- **\(p\):** Number of past values (lags) to include (AR part).
- **\(d\):** Number of differencing steps to make the series stationary (I part).
- **\(q\):** Number of past errors to include (MA part).

### Steps to Use ARIMA
1. **Make the series stationary:**
   - Use differencing (\(d\)) if needed.
   - Perform a statistical test like the **Augmented Dickey-Fuller (ADF) test** to confirm stationarity.

2. **Determine \(p\) and \(q\):**
   - Use **ACF (Autocorrelation Function)** and **PACF (Partial Autocorrelation Function)** plots to decide the values of \(p\) and \(q\).

3. **Fit the ARIMA model:**
   - Use the chosen \(p, d, q\) values to train the model.

4. **Evaluate the model:**
   - Use metrics like **Mean Absolute Error (MAE)** or **Root Mean Squared Error (RMSE)**.

5. **Forecast future values:**
   - Use the trained model to predict future time points.

---

## Mathematical Formula of ARIMA
The ARIMA equation combines AR, I, and MA components:
\[
  y_t = \phi_1 y_{t-1} + \phi_2 y_{t-2} + \dots + \phi_p y_{t-p} + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \dots + \theta_q \epsilon_{t-q} + \epsilon_t
\]

Where:
- \( y_t \): Current value (after differencing if \(d > 0\))
- \( y_{t-1}, y_{t-2}, \dots \): Past values (AR part)
- \( \epsilon_t \): Current error (random noise)
- \( \phi \): Coefficients for AR terms
- \( \theta \): Coefficients for MA terms

If \( d = 1 \), the series is differenced once:
\[
  y'_t = y_t - y_{t-1}
\]

---

## Example
Let’s say you want to predict gold prices:
1. **Look at the trend:** If prices are steadily increasing, use differencing (\(d = 1\)) to remove the trend.
2. **Check autocorrelation:** If prices depend on the last 2 days, set \(p = 2\).
3. **Check errors:** If errors from 1 day ago influence predictions, set \(q = 1\).
4. **Train ARIMA(2, 1, 1):** Combine these components to fit the model and forecast future prices.

---

## Summary
ARIMA is a powerful tool for time series forecasting that:
- Uses past values (AR) to predict the future.
- Stabilizes the series by removing trends (I).
- Fixes errors using past mistakes (MA).

By understanding \(p, d, q\), you can customize ARIMA to fit your time series data and create accurate forecasts!

---

# the RoadMap :

#### 1 . Exploratory Data Analysis (EDA)
- Data Cleaning
- Summary Statistics
  >Compute basic metrics like mean, median, standard deviation, and percentiles for numerical columns (e.g., price, volume).
- Visualization
  > Candlestick Charts - Correlation Heatmap - Distribution Analysis
  ```python
    import matplotlib.pyplot as plt
    df['price'].plot(figsize=(10, 5), title='Gold Price Over Time')
    plt.show()
    ```
- Trends and Seasonality
- Normalization/Scaling

#### 2 . Feature Engineering (if we have time)

- Calculate moving averages (e.g., 7-day, 30-day).
- Add indicators like Relative Strength Index (RSI) or Bollinger Bands for financial time series.

#### 3 . ARIMA Modeling

##### Steps:  

##### 3.1. Stationarity Check:  
- Use the Augmented Dickey-Fuller (ADF) test to check stationarity.  
- If the data is not stationary, apply differencing (e.g., `df.diff()`) to make it stationary.  

##### 3.2. Order Selection:  
- Plot Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) to determine the ARIMA order (p, d, q):  
  - **p**: Number of autoregressive terms.  
  - **d**: Differencing order (to make data stationary).  
  - **q**: Number of moving average terms.  

##### 3.3. Model Fitting:  
- Train the ARIMA model:  
    ```python  
    from statsmodels.tsa.arima.model import ARIMA  
    model = ARIMA(df['price'], order=(p, d, q))  
    results = model.fit()  
    ```  

##### 3.4. Evaluation:  
- Split the data into training and testing sets.  
- Validate predictions using metrics like Mean Absolute Error (MAE), Mean Absolute Percentage Error (MAPE), or Root Mean Square Error (RMSE):  
    ```python  
    from sklearn.metrics import mean_absolute_error  
    mae = mean_absolute_error(y_test, y_pred)  
    print(f'MAE: {mae}')  
    ```  

##### 3.5. Forecasting:  
- Use the model to predict future prices:  
    ```python  
    forecast = results.forecast(steps=30)  # Predict next 30 steps  
    ```

#### 4 . Visualization of Predictions
Showcase the results visually for better understanding.

#### 5 . Insights and Reporting


    

