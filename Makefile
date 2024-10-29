PIP = pip

.PHONE: lambda-package-requirements
lambda-package-requirements:
	$(PIP) install --upgrade --target ./package/python/lib/python3.11/site-packages -r $(FILE)

.PHONY: lambda-package
lambda-package:
	$(MAKE) clean

	# 1. Install and copy packages
	mkdir -p package/python/lib/python3.11/site-packages/fair_wizard
	$(MAKE) lambda-package-requirements FILE=./requirements.txt
	cp -R ./src/fair_wizard ./package/python/lib/python3.11/site-packages

	# 2. Package the ZIP and clean
	$(PIP) install --upgrade --target ./package/python/lib/python3.11/site-packages --platform manylinux2014_x86_64 --implementation cp --only-binary=:all: "pydantic"
	$(PIP) install --upgrade --target ./package/python/lib/python3.11/site-packages --platform manylinux2014_x86_64 --implementation cp --only-binary=:all: "pydantic_core"
	cd package && zip -r ../fair-wizard-integration-sdk-lambda-layer.zip .
	rm -rf package

.PHONY: clean
clean:
	find . -type d -name __pycache__ -exec rm -r {} \; >/dev/null || true
	rm -rf package
	rm fair-wizard-integration-sdk-lambda-layer.zip || true
