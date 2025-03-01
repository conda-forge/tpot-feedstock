import sys
from subprocess import call

FAIL_UNDER = "40"
COV = ["coverage"]
RUN = ["run", "--source=tpot", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "--color=yes", "--tb=long", "--pyargs", "tpot"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = []

if SKIPS:
    SKIP_OR = " or ".join(SKIPS)
    K = ["-k", f"not ({SKIP_OR})" if len(SKIPS) > 1 else f"not {SKIPS[0]}"]
    PYTEST += K


if __name__ == "__main__":
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
