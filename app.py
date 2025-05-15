from nodes import rule_block, result_block, select_type_block, epl_text_block#, email_block
from barfi import st_barfi, barfi_schemas
import streamlit as st

base_blocks = [rule_block, select_type_block, result_block, epl_text_block]#, email_block]

#load_schema = st.selectbox('Select a saved schema:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=True)

barfi_result = st_barfi(base_blocks, compute_engine=compute_engine)


if barfi_result:
    #st.write(barfi_result)
    st.write(barfi_result['Rule-1']['block'].get_interface(name='Name'))
    st.write(barfi_result['Rule-1']['block'].get_interface(name='Action'))
    st.write(barfi_result['Rule-1']['block'].get_interface(name='Text'))


# streamlit run app.py  