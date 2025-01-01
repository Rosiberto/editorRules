from barfi import Block
import streamlit as st

rule_block = Block(name='Rule')

rule_block.add_input(name='text_epl')
rule_block.add_option(name='display-name', type='display', value='Enter the name of the rule.')
rule_block.add_option(name='name_input', type='input')
rule_block.add_input(name='action_type')

rule_block.add_output(name='Name')
rule_block.add_output(name='Action')
rule_block.add_output(name='Text')

def rule_block_func(self): 
   data_epl = self.get_interface(name='text_epl')
   data_name = self.get_option(name='name_input')
   data_action = self.get_interface(name='action_type')

   self.set_interface(name='Text', value=data_epl)
   self.set_interface(name='Name', value=data_name)
   self.set_interface(name='Action', value=data_action)  
  
   

rule_block.add_compute(rule_block_func)