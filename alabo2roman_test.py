# !usr/bin/env python
# Copyright @2020 Yanyu Zhang zhangya@bu.edu
from alabo2roman import alabo2roman

def test_right(): 
	assert alabo2roman(1213) == "MCCXIII"
	assert alabo2roman(20) == "XX"
	assert alabo2roman(384) == "CCCLXXXIV"
	assert alabo2roman(99) == "XCIX"
	assert alabo2roman(999) == "CMXCIX"
	assert alabo2roman(3000) == "MMM"
	assert alabo2roman(100) == "C"
	assert alabo2roman(3999) == "MMMCMXCIX"
	assert alabo2roman(12) == "XII"
	assert alabo2roman(432) == "CDXXXII"

def test_error():
	assert alabo2roman(-1) == "ERROR"
	assert alabo2roman("String") == "ERROR"
	assert alabo2roman(23.4) == "ERROR" 
	assert alabo2roman(-3.4) == "ERROR"
	assert alabo2roman(0.0) == "ERROR"
	assert alabo2roman("-123") == "ERROR"
	assert alabo2roman(-12345) == "ERROR"
	assert alabo2roman("osama") == "ERROR"
	assert alabo2roman(123.5) == "ERROR"
