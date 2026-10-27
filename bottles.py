def bottles(n):
	# "2 bottles", "1 bottle", "no more bottles"
	if n == 0:
		return "no more bottles"
	if n == 1:
		return "1 bottle"
	return f"{n} bottles"


def verse(n, start):
	if n == 0:
		return (
			"No more bottles of beer on the wall, no more bottles of beer.\n"
			f"Go to the store and buy some more, {bottles(start)} of beer on the wall."
		)
	return (
		f"{bottles(n)} of beer on the wall, {bottles(n)} of beer.\n"
		f"Take one down and pass it around, {bottles(n - 1)} of beer on the wall."
	)


def bottle_song(start=99):
	# Loop version
	for n in range(start, -1, -1):
		print(verse(n, start))


def bottle_song_recursive(n=99, start=None):
	# No-loop version: each call prints one verse, then calls itself with one fewer bottle
	if start is None:
		start = n
	print(verse(n, start))
	if n > 0:
		bottle_song_recursive(n - 1, start)


bottle_song()
