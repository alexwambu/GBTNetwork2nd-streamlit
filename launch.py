import streamlit as st
import json
from web3 import Web3

st.set_page_config(page_title="GBTNetwork Layer 1", layout="wide")

st.image("static/logo.png", width=150)
st.title("GBTNetwork Layer 1 Dashboard")

rpc_url = "https://GBTNetwork"
web3 = Web3(Web3.HTTPProvider(rpc_url))

if web3.isConnected():
    st.success(f"Connected to GBTNetwork at {rpc_url}")
    chain_id = web3.eth.chain_id
    st.write(f"Chain ID: {chain_id}")
    latest_block = web3.eth.block_number
    st.write(f"Latest Block: {latest_block}")
else:
    st.error("Connection failed. Check RPC URL or Streamlit logs.")
