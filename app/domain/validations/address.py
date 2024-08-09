import re

from fastapi import HTTPException, status


def postal_code_validator(value: str):
    passed = re.search(r'^\d{8}$', value.strip())
    if not passed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Postal code must be exactly 8 digits long."
        )
    return passed


def number_validator(value: str):
    passed = re.search(r'^\d+$', value.strip())
    if not passed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Number must have only digits."
        )
    return passed
