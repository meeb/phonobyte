python=/usr/bin/env python3


test:
	echo && $(python) -m unittest discover -s tests -v
