PYTHON = python3
TARGET_DIR = *


test:
	$(eval TARGET_FILES:=$(wildcard $(TARGET_DIR)/*.json))
	$(PYTHON) validator.py $(TARGET_FILES)
