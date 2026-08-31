# === Standard Library Imports ===
import os
import re
import json
import time
from datetime import datetime, timezone, timedelta


# === Third-Party Libraries ===
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap


def get_market_details_by_slug(market_slug):
    def iso_to_unix(iso_str):
        if not iso_str:
            return None
        try:
            dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
            return int(dt.timestamp())
        except Exception:
            return None

    url = f"https://gamma-api.polymarket.com/markets/slug/{market_slug}"
    response = requests.get(url)
    m = response.json()

    start_str = m.get("eventStartTime")
    end_str = m.get("endDate") or m.get("closeDate")

    clob = m.get("clobTokenIds")
    if isinstance(clob, str) and clob.strip().startswith("["):
        try:
            m["clobTokenIds"] = json.loads(clob)
        except json.JSONDecodeError:
            pass

    start_ts_val = iso_to_unix(start_str)
    m["start_time_iso"] = start_str
    m["end_time_iso"] = end_str
    m["start_ts"] = start_ts_val
    m["end_ts"] = iso_to_unix(end_str)

    return m


def get_price_history(market_info):
    base_url = "https://clob.polymarket.com/prices-history"
    start_ts = market_info["start_ts"]
    end_ts = market_info["end_ts"]
    clob_ids = market_info["clobTokenIds"]

    if not clob_ids or len(clob_ids) < 2:
        raise ValueError("CLOB IDs missing or invalid in market_info")

    yes_token_id, no_token_id = clob_ids[0], clob_ids[1]

    def fetch_prices(token_id):
        params = {"market": token_id, "startTs": start_ts, "endTs": end_ts}
        r = requests.get(base_url, params=params)
        r.raise_for_status()
        hist = r.json().get("history", [])
        hist.sort(key=lambda x: x["t"])
        return [{"timestamp": int(h["t"]), "price": float(h["p"])}
                for h in hist if "t" in h and "p" in h]

    yes_hist = fetch_prices(yes_token_id)
    no_hist = fetch_prices(no_token_id)

    if not yes_hist or not no_hist:
        raise ValueError("Missing one or both price histories")

    # Align lists by shortest length to avoid mismatch
    min_len = min(len(yes_hist), len(no_hist))
    yes_hist, no_hist = yes_hist[:min_len], no_hist[:min_len]

    # Convert price floats to integer percentages and zip into tuples
    price_series = [
        (int(round(yes["price"] * 100)), int(round(no["price"] * 100)))
        for yes, no in zip(yes_hist, no_hist)
    ]

    return price_series


def market_analyzer(market_slug):
    market = get_market_details_by_slug(market_slug)
    price_series = get_price_history(market)
    yes_prices = np.array([p[0] for p in price_series])
    no_prices = np.array([p[1] for p in price_series])
    n = len(price_series)
    x = np.arange(n)

    output_dir = os.path.join(os.getcwd(), "analyzer-outputs")
    os.makedirs(output_dir, exist_ok=True)
    market_dir = os.path.join(output_dir, market_slug)
    os.makedirs(market_dir, exist_ok=True)
    existing_plots = [f for f in os.listdir(
        market_dir) if f.startswith("plot") and f.endswith(".png")]
    plot_count = len(existing_plots) + 1
    plot_path = os.path.join(market_dir, f"plot{plot_count}.png")

    plt.style.use("seaborn-v0_8-darkgrid")
    fig, axs = plt.subplots(2, 1, figsize=(12, 10))
    plt.suptitle(f"Market Analysis: {market_slug}",
                 fontsize=16, fontweight="bold")







=========================================================================================================

Pay get full soirce code here: 

https://pay.oxapay.com/17944852



=========================================================================================================
