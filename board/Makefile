PYTHON = python3
TARGET_DIR = *
PY_SRC =

test:
	make do_py PY_SRC=validator

view_point:
	make do_py PY_SRC=boardPointChecker

do_py:
	$(eval TARGET_FILES:=$(wildcard $(TARGET_DIR)/*.json))
	$(PYTHON) $(PY_SRC).py $(TARGET_FILES)
