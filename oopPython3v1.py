#mini project oop python3
class email_sender:
    def __init__(self, email, subjek, pesan):
        self.email = email
        self.subjek = subjek
        self.pesan = pesan

print("Sender Email")
cEmail = str(input("To :"))
cSubjek = str(input("Subjek :"))
cPesan = str(input("Pesan :"))

goto_send = email_sender(cEmail,cSubjek,cPesan)

print("kamu telah mengirim email ke: %s , subjek: %s, dengan pesan: %s" % (goto_send.email, goto_send.subjek, goto_send.pesan))
    
