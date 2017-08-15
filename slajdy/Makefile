prezentacja.pdf: prezentacja.latex styles.tex gpio.tex ampy.tex Makefile 
	latex -output-format=pdf prezentacja.latex

styles.tex: Makefile
	pygmentize -S manni -f latex > styles.tex

gpio.tex: gpio.pycon Makefile
	pygmentize -l pycon -o gpio.tex gpio.pycon

ampy.tex: ampy.sh-session Makefile
	pygmentize -l console -o ampy.tex ampy.sh-session
