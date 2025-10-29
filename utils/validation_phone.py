import re

def validation_phone(phone: str) -> str | ValueError:
    formatted_phone_number = re.sub(r"[^\d+]", "", phone)

    if len(formatted_phone_number) != 10:
        raise ValueError(f"Invalid phone number '{phone}'. Must be 10 digits.")

    if len(formatted_phone_number) != 0 and formatted_phone_number[0] != "+":
        prefix = ""

        if formatted_phone_number.startswith("80"):
            prefix = "3"
        elif formatted_phone_number.startswith("0"):
            prefix = "38"

        formatted_phone_number = f"+{prefix}{formatted_phone_number}"

    return formatted_phone_number
