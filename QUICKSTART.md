# 🚀 Quick Start Guide

Get the Weather Forecast App running in 5 minutes!

## Step 1: Get Your API Key (2 minutes)

1. Go to https://openweathermap.org/api
2. Click "Sign Up" (it's free!)
3. Verify your email
4. Go to API Keys section in your account
5. Copy your API key

## Step 2: Install (1 minute)

```bash
# Install dependencies
pip install -r requirements.txt
```

## Step 3: Configure (30 seconds)

**Option A: Environment Variable (Recommended)**
```bash
# Windows
set OPENWEATHER_API_KEY=paste_your_key_here

# Mac/Linux
export OPENWEATHER_API_KEY=paste_your_key_here
```

**Option B: Edit the File**
- Open `app.py`
- Line 10: Replace `'your_api_key_here'` with your actual key

## Step 4: Run (30 seconds)

```bash
python app.py
```

## Step 5: Use It! (1 minute)

1. Open browser: http://localhost:5000
2. Type a city name (e.g., "London")
3. Click Search
4. View weather and forecast!

## 🎯 What to Try

- Search for your city
- Check the 5-day forecast
- View your search history
- Try different cities around the world

## ❓ Quick Troubleshooting

**"401 Unauthorized"** → Your API key hasn't activated yet (wait 10 minutes)

**"City not found"** → Try full city name with country (e.g., "Paris,FR")

**"Connection refused"** → Make sure `python app.py` is running

## 📱 Test the API

Run the test script to verify everything works:
```bash
python test_api.py
```

---

**Need help?** Check the full README.md for detailed documentation!
