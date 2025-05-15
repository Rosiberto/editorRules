from barfi import Block
import streamlit as st

email_block = Block(name='E-mail')
email_block.add_option(name='to-display', type='display', value='TO')
email_block.add_option(name='to', type='input')

email_block.add_option(name='from-display', type='display', value='FROM')
email_block.add_option(name='from', type='input')

email_block.add_option(name='subject-display', type='display', value='SUBJECT')
email_block.add_option(name='subject', type='input')

email_block.add_output(name='Text')


def email_block_func(self):
    _to      = self.get_option(name='to-display')
    _from    = self.get_option(name='from-display')   
    _subject = self.get_option(name='subject-display')

    data = """\"action\": { 
                    \"type\": \"email\", 
                    \"template\": \"Meter ${Meter} has pressure ${Pressure} (GEN RULE)\",
                    \"parameters\": {
                            \"to\": \"someone@acme.com\",
                            \"from\": \"cep@acme.com\",
                            \"subject\": \"It's The End Of The World As We Know It (And I Feel Fine)\" 
                            }
                }"""

    self.set_interface(name='Text', value=data)







    

email_block.add_compute(email_block_func)