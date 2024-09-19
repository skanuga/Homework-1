FXN = function
TXT = file
FMT = img

plot: Trigonometry.py
	python Trigonometry.py $(FXN)

write: Trigonometry.py
	python Trigonometry.py $(TXT)

read: Trigonometry.py
	python Trigonometry.py $(FMT)
