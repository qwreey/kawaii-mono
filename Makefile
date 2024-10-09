build:
	@mkdir -p out
	@python3 build.py -B  2> out/err.log || { echo "Build Failed. Please check out/err.log for detailed information"; false; }

install:
	@mkdir -p ~/.local/share/fonts
	@cp out/KawaiiMonoRegularPatched.ttf ~/.local/share/fonts/KawaiiMonoRegular.ttf
	@fc-cache -f -v
