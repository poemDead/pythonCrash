def show_messages(msgs):
    while msgs:
        msg = msgs.pop()
        print(f"current sending {msg}...")
        send_msgs.append(msg)

def send_messages(send_msgs):
    print("\nHere's the messages have been showed.")
    for msg in send_msgs:
        print(msg)

msgs = ['hello','this','beautiful','stupid','world']
send_msgs = []
show_messages(msgs)
send_messages(send_msgs)