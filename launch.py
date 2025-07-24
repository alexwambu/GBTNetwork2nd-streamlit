import streamlit as st
from web3 import Web3
import json

# --- GBTNetwork RPC Setup ---
RPC_URLS = [
    "https://GBTNetwork",           # Clean RPC
    "https://GBTNetwork:8545",      # Port-based
    "https://localhost:8545"        # Localhost fallback
]

w3 = Web3(Web3.HTTPProvider(RPC_URLS[0]))

# --- App Title and Logo ---
st.set_page_config(page_title="GBTNetwork Layer 1", page_icon="🪙")
st.image("https://raw.githubusercontent.com/openai-user-assist/GBTNetworkAssets/main/logo.png", width=180)

st.title("GBTNetwork Layer 1 Dashboard")
st.markdown("📡 Live on: `https://GBTNetwork`")

# --- Connection Status ---
if w3.is_connected():
    st.success("✅ Connected to GBTNetwork")
else:
    st.error("❌ Not connected to GBTNetwork")

# --- Wallet & Block Info ---
try:
    latest_block = w3.eth.get_block("latest")
    st.subheader("Latest Block Info")
    st.json({
        "Block Number": latest_block.number,
        "Hash": latest_block.hash.hex(),
        "Gas Limit": latest_block.gasLimit,
        "Timestamp": latest_block.timestamp
    })
except Exception as e:
    st.error(f"Error fetching block: {e}")

# --- Custom Utility: Balance Checker ---
st.subheader("🔍 Check Address Balance")
address = st.text_input("Enter wallet address:")
if address:
    try:
        balance = w3.eth.get_balance(address)
        gbt_balance = w3.from_wei(balance, 'ether')
        st.success(f"Balance: {gbt_balance} GBT")
    except:
        st.error("Invalid address or failed to fetch balance.")

# --- Footer ---
st.markdown("---")
st.caption("🪙 Powered by GBTNetwork Layer 1 — MetaMask Compatible | © 2025")
