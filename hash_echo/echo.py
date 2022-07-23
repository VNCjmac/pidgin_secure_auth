import friar
import sys

if len(sys.argv) < 3:
	print("python3 echo.py [word] [hb<1-3>]")

else:
	valid=["hb1", "hb2", "hb3"]

	word=sys.argv[1]
	mode=sys.argv[2]

	if mode.strip().lower()=="hb1":
		enc=friar.hashbrowns1()(word)
		print(enc)
	if mode.strip().lower()== "hb2":
		enc=friar.hashbrowns2()(word)
		print(enc)
	if mode.strip().lower()== "hb3":
		enc=friar.hashbrowns3()(word)
		print(enc)
	if mode.strip().lower() not in valid:
		sys.exit(f"ModeError: '{mode}' is not a supported hashbrown type.")