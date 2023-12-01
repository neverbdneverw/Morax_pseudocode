START
FROM io IMPORT BytesIO
IMPORT base64
IMPORT random
IMPORT string

Module convert_to_base64(file: BytesIO)
	SET base64_content = base64.b64encode(file.getvalue()).decode('utf-8')

	RETURN base64_content

Module generate_unique_code(self)
	SET res = ''.join(random.choices(
            	string.ascii_letters +
           	string.digits
            	, k=8))

	RETURN str(res)

CREATE LIST accepted_months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December",
    
    "Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

CREATE DICTIONARY currency_symbols = {
    "PHP": "₱",
    "USD": "$",
    "EU" : "€"
}
END
