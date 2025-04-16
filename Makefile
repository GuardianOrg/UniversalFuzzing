#TROUBLESHOOTING:
#If error  Failed to upload files: stat python3.13: no such file or directory 
#SOLUTION:
# delete venv folder and rerun make cloud

#If error  ERROR:CryticCompile:Invalid solc compilation Error: Source "test/fuzzing/helpers/postconditions/PostconditionsExchangeConfi
#g.sol" not found: File not found. Searched the following locations: "".
# --> test/fuzzing/FuzzExchangeConfig.sol:4:1:
#SOLUTION:
#add cryticArgs: ["--foundry-compile-all"]


# Default instance type
DEFAULT_INSTANCE = s-4vcpu-8gb-intel

# Default target when you just run 'make'
help:
	@echo "Available targets:"
	@echo "  cloud JOB=<job_index> [INSTANCE=<instance_type>] - Run cloud execution with specified job and instance"
	@echo "  clean - Remove generated output directory"

# Main target for cloud execution
cloud:
	@if [ "$(JOB)" = "" ]; then \
		echo "Usage: make cloud JOB=<job_index> [INSTANCE=<instance_type>]"; \
		echo "Example: make cloud JOB=2"; \
		echo "Example: make cloud JOB=2 INSTANCE=s-8vcpu-16gb-intel"; \
		exit 1; \

test:
	forge test --match-path FoundryPlayground.sol -vvvv $(ARGS)


# Default instance type
DEFAULT_INSTANCE = s-4vcpu-8gb-intel

# Default target when you just run 'make'
help:
	@echo "Available targets:"
	@echo "  cloud JOB=<job_index> [INSTANCE=<instance_type>] - Run cloud execution with specified job and instance"
	@echo "  clean - Remove generated output directory"

# Main target for cloud execution
cloud:
	@if [ "$(JOB)" = "" ]; then \
		echo "Warning: No JOB parameter provided - starting fuzzing from fresh without corpus"; \
		echo "To use existing corpus, provide JOB parameter:"; \
		echo "Example: make cloud JOB=2"; \
		echo "Example: make cloud JOB=2 INSTANCE=s-8vcpu-16gb-intel"; \
	fi
	@INSTANCE=$(or $(INSTANCE),$(DEFAULT_INSTANCE)); \
	mkdir -p output src output/echidna-corpus; \
	touch src/strings.sol; \
	rm -rf output/echidna-corpus; \
	if [ ! -z "$(JOB)" ]; then \
		if [ -d "cloudexec/job-$(JOB)/echidna-corpus" ]; then \
			echo "Preparing Echidna corpus from job $(JOB)..."; \
			cp -r cloudexec/job-$(JOB)/echidna-corpus output/echidna-corpus; \
		else \
			echo "Warning: Corpus directory cloudexec/job-$(JOB)/echidna-corpus not found, skipping corpus preparation"; \
		fi; \
	fi; \
	echo "Launching cloudexec with instance $$INSTANCE..."; \
	cloudexec launch --size $$INSTANCE

# Clean up generated files
clean:
	rm -rf output
	fi
	@INSTANCE=$(or $(INSTANCE),$(DEFAULT_INSTANCE)); \
	echo "Preparing Echidna corpus from job $(JOB)..."; \
	mkdir -p output src output/echidna-corpus; \
	touch src/strings.sol; \
	rm -rf output/echidna-corpus; \
	cp -r cloudexec/job-$(JOB)/echidna-corpus output/echidna-corpus; \
	echo "Launching cloudexec with instance $$INSTANCE..."; \
	cloudexec launch --size $$INSTANCE

# Clean up generated files
clean:
	rm -rf output