# Testing Strategy - Quick-Calc





### What Was Tested

The test suite covers all four arithmetic operations at the **unit level** (addition, subtraction, multiplication, and division). Also the negate and clear operations were tested. Each operation has at least one standard test and at least one edge case. The division operation additionally tests division by zero (result should be Error in this case). Two **integration tests** simulate real button-click sequences on the Tkinter GUI to verify that the interface and the calculator logic work correctly together.

### What Was Not Tested

Non-functional aspects were not tested. Since non-functional testing covers performance, security, scalability, and availability, it is not necessary for the offline desktop calculator app.



## Lecture Concepts Applied

### 1. The Testing Pyramid

The testing pyramid recommends a large base of unit tests, a smaller layer of integration tests, and minimal end-to-end tests at the top. Tests written for Quick-Calc follow this approach. 12 unit tests form the wide base testing each arithmetic operation, and 2 integration tests form the integration tests layer. No system or acceptance tests were written, because for such a small application it is not necessary.


### 2. Black-box vs White-box Testing

Unit tests are **white-box tests** — written with knowledge of the internal code. For example, `test_divide_by_zero_raises_value_error` specifically tests the division by zero check inside `divide()`.

Integration tests are **black-box tests** — they only interact through `_on_button()` and check the display value, without any knowledge of how the result was calculated internally.

### 3. Functional vs Non-Functional Testing

**Functional testing** is as black-box testing that verifies what the system does by checking if inputs produce the correct outputs. All tests written are functional: they verify that arithmetic operations return correct results, that division by zero raises an error, and that the clear button resets the display to zero.


**Non-functional testing** tests performance, security, scalability, and availability, and it was intentionally not tested. Questions like "how does the application behave under large load?" or "how secure is the application?" do not apply to Quick-Calc.

### 4. Regression Testing

Regression testing confirms that changes do not break existing functionality. It occurs after requirement changes or defect fixes. Any time Quick-Calc is updated, the full suite can be run with:

```
pytest ./
```

Any test that fails immediately shows what broke. The suite covers all operations and edge cases, making it a reliable safety net for future changes.

---

## Test Results Summary

| Test Name | Type | Status |
|---|---|---|
| `test_add_two_positive_numbers` | Unit | ✅ PASS |
| `test_add_negative_numbers` | Unit | ✅ PASS |
| `test_subtract_two_positive_numbers` | Unit | ✅ PASS |
| `test_subtract_resulting_in_negative` | Unit | ✅ PASS |
| `test_multiply_two_positive_numbers` | Unit | ✅ PASS |
| `test_multiply_large_numbers` | Unit | ✅ PASS |
| `test_divide_two_positive_numbers` | Unit | ✅ PASS |
| `test_divide_resulting_in_decimal` | Unit | ✅ PASS |
| `test_divide_by_zero_raises_value_error` | Unit | ✅ PASS |
| `test_negate_positive_number` | Unit | ✅ PASS |
| `test_negate_negative_number` | Unit | ✅ PASS |
| `test_clear_resets_result_to_zero` | Unit | ✅ PASS |
| `test_addition_via_gui_buttons` | Integration | ✅ PASS |
| `test_clear_resets_display_to_zero` | Integration | ✅ PASS |

**Total: 14 tests — 14 passed, 0 failed.**