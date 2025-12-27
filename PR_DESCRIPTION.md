# Runner test task

## Summary
Implemented test suite to verify README content correctness and ensure proper spelling of "Transportation".

## Changes
- Added `test_runner.py` with test to verify README contains correct title spelling
- Added `requirements.txt` with pytest dependency for test execution

## Testing
Run tests with:
```bash
pip install -r requirements.txt
pytest test_runner.py -v
```

The test verifies:
- README contains "Transportation" (correct spelling)
- README does not contain "Transposrtation" (typo)

## Related
- Trello Card ID: test
- Board: Transport
- List: In progress
