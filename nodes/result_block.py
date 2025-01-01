from barfi import Block
import streamlit as st
from sklearn import preprocessing


result_block = Block(name='Result')
result_block.add_input(name='getName')
result_block.add_input(name='getAction')
result_block.add_input(name='getText')

def result_block_func(self):
    data  = self.get_interface(name='getName') 
    data1 = self.get_interface(name='getAction')
    data2 = self.get_interface(name='getText')

    print(data)
    print(data1)
    print(data2)
   

result_block.add_compute(result_block_func)