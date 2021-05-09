# Onde estarão todas as funções deste pacote
# Ele é quem vai cooderndar este pacote (gerenciador)



def initialize():
    from carbonmail.email_sender import Email_sender
    
    ems = Email_sender()
    ems.enable_window()