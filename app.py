from func import state
import streamlit as st


def main():
    if not state.count:
        state.count = 0
    state.count += 1
    st.write(state.count)


if __name__ == "__main__":
    main() 