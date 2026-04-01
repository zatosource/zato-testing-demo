# -*- coding: utf-8 -*-

import sys
import time

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

_passed = 0
_failed = 0
_errors = []
_start_time = None

def pytest_sessionstart(session):
    global _start_time
    _start_time = time.time()
    sys.stdout.write('\n')
    sys.stdout.write(f'{Colors.CYAN}{Colors.BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}\n')
    sys.stdout.write(f'{Colors.CYAN}{Colors.BOLD}  ZATO SERVICE TESTS{Colors.RESET}\n')
    sys.stdout.write(f'{Colors.CYAN}{Colors.BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}\n')
    sys.stdout.write('\n')
    sys.stdout.flush()

def pytest_runtest_logreport(report):
    global _passed, _failed, _errors
    if report.when == 'call':
        test_name = report.nodeid.split('::')[-1]
        class_name = report.nodeid.split('::')[-2] if '::' in report.nodeid else ''

        if report.passed:
            _passed += 1
            sys.stdout.write(f'  {Colors.GREEN}✓{Colors.RESET}  {Colors.DIM}{class_name}.{Colors.RESET}{test_name}\n')
        elif report.failed:
            _failed += 1
            _errors.append((report.nodeid, report.longreprtext))
            sys.stdout.write(f'  {Colors.RED}✗{Colors.RESET}  {Colors.DIM}{class_name}.{Colors.RESET}{test_name}\n')
        sys.stdout.flush()

def pytest_sessionfinish(session, exitstatus):
    elapsed = time.time() - _start_time
    total = _passed + _failed

    sys.stdout.write('\n')
    sys.stdout.write(f'{Colors.CYAN}{Colors.BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}\n')

    if _failed == 0:
        word = 'test' if total == 1 else 'tests'
        sys.stdout.write(f'  {Colors.GREEN}{Colors.BOLD}{total} {word} passed{Colors.RESET}  {Colors.DIM}in {elapsed:.2f}s{Colors.RESET}\n')
    else:
        sys.stdout.write(f'  {Colors.RED}{Colors.BOLD}{_failed} FAILED{Colors.RESET}, {Colors.GREEN}{_passed} passed{Colors.RESET}  {Colors.DIM}in {elapsed:.2f}s{Colors.RESET}\n')

    sys.stdout.write(f'{Colors.CYAN}{Colors.BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}\n')
    sys.stdout.write('\n')

    if _errors:
        sys.stdout.write(f'{Colors.RED}{Colors.BOLD}FAILURES:{Colors.RESET}\n')
        sys.stdout.write('\n')
        for nodeid, longrepr in _errors:
            sys.stdout.write(f'{Colors.RED}  {nodeid}{Colors.RESET}\n')
            for line in longrepr.split('\n'):
                sys.stdout.write(f'    {Colors.DIM}{line}{Colors.RESET}\n')
            sys.stdout.write('\n')
    sys.stdout.flush()
