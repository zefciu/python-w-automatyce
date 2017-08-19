prezentacja.pdf: prezentacja.latex styles.tex gpio.tex ampy.tex pwm.tex time.tex Makefile 
	latex -output-format=pdf prezentacja.latex

styles.tex: Makefile
	pygmentize -S manni -f latex > styles.tex

gpio.tex: gpio.pycon Makefile
	pygmentize -l pycon -o gpio.tex gpio.pycon

ampy.tex: ampy.sh-session Makefile
	pygmentize -l console -o ampy.tex ampy.sh-session

pwm.tex: pwm.py Makefile
	pygmentize -l python -o pwm.tex pwm.py

time.tex: time.py Makefile
	pygmentize -l python -o time.tex time.py
