from barfi import Block
import streamlit as st

select_type_block = Block(name='Select Type')
select_type_block.add_option(name='display-option', type='display', value='Select the type to action.')
select_type_block.add_option(name='select-type', type='select', items=['e-mail', 'post', 'sms', 'update'], value='')
select_type_block.add_output(name='Type')


def select_type_block_func(self):
    data = self.get_option(name='select-type')   
    self.set_interface(name='Type', value=data)

    if data == "e-mail":
      print('Foi selecionado o tipo = '+ data)
      
select_type_block.add_compute(select_type_block_func)