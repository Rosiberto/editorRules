from barfi import Block
import streamlit as st

epl_text_block = Block(name='EPL Text')
epl_text_block.add_option(name='display-name', type='display', value='Enter with EPL text.')
epl_text_block.add_option(name='text_epl', type='input')

epl_text_block.add_output(name='Text')


def epl_text_block_func(self):
    data = self.get_option(name='text_epl')   
    self.set_interface(name='Text', value=data)
    

epl_text_block.add_compute(epl_text_block_func)