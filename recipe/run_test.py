import sys
from subprocess import call

FAIL_UNDER = "74"
COV = ["coverage"]
RUN = ["run", "--source=tpot", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "--color=yes", "--tb=long"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = []

if SKIPS:
    SKIP_OR = " or ".join(SKIPS)
    K = ["-k", f"not ({SKIP_OR})"]
    PYTEST += K


if __name__ == "__main__":
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
