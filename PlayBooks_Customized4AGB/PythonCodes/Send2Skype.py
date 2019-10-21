from skpy import Skype
fname = raw_input("Type the file name to send out: ")
f = open(fname, "r")
if f.mode == 'r':
  contents =f.read()
print contents
sk = Skype("ayenyeinaung666@gmail.com", "leepallox123") # connect to Skype
sk.user # you
sk.contacts # your contacts
sk.chats # your conversations
#ch = sk.chats.create(["joe.4", "daisy.5"]) # new group conversation
ch = sk.contacts["minnthuwinn"].chat # 1-to-1 conversation
ch1 = sk.chats["19:6829bf3d48ad452fbf64bea221c903f2@thread.skype"] #AGB SysTeam's Group
ch.sendMsg(contents) # plain-text message
ch1.sendMsg(contents)
#ch.sendFile(open("song.mp3", "rb"), "song.mp3") # file upload
#ch.sendContact(sk.contacts["daisy.5"]) # contact sharing
ch.getMsgs() # retrieve recent messages
