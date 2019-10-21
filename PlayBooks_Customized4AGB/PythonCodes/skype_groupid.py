from skpy import Skype, SkypeChats

sk = Skype("ayenyeinaung666@gmail.com", "leepallox123")
skc = SkypeChats(sk)
print(skc.recent())
