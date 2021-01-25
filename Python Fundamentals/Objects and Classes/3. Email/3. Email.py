class Email:
    emails = []

    def __init__(self, sender, receiver, content, is_sent = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


while True:
    command = input()
    if command == 'Stop':
        break
    sender_id, receiver_id, data = command.split()
    email = Email(sender_id, receiver_id, data)
    Email.emails.append(email)

index_id = list(map(int, input().split(', ')))
for i in index_id:
    mail = Email.emails[i]
    mail.send()

for mail in Email.emails:
    print(mail.get_info())
