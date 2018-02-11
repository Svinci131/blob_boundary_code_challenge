run: test
	@echo "------- START EXAMPLE RUN -------"
	python main.py
	@echo "------- END EXAMPLE RUN -------"

test:
	@echo "------- START RUNNING TESTS -------"
	python test_main.py
	@echo "------- END RUNNING TESTS -------"