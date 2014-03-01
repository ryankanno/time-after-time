NOSETESTS ?= nosetests

.PHONY: nosetests nosetests.coverage test test.coverage flake8

test: nosetests flake8
test.coverage: nosetests.coverage flake8

nosetests:
	@$(NOSETESTS) --with-doctest --nocapture

nosetests.coverage:
	@$(NOSETESTS) --with-xcoverage --cover-package=time_after_time --cover-tests --with-doctest

flake8:
	@flake8 time_after_time tests

clean:
	@rm -rf .coverage
	@rm -rf coverage.xml
