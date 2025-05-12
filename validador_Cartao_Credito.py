import re

def luhn_check(card_number):
    digits = [int(d) for d in card_number if d.isdigit()]
    checksum = 0
    parity = len(digits) % 2
    for i, digit in enumerate(digits):
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0

BANDS = [
    ("Mastercard",    r"^5[1-5][0-9]{14}$"),
    ("Visa",          r"^4[0-9]{12}(?:[0-9]{3})?$"),
    ("American Express", r"^3[47][0-9]{13}$"),
    ("Diners Club",   r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$"),
    ("Discover",      r"^6(?:011|5[0-9]{2})[0-9]{12}$"),
    ("EnRoute",       r"^(2014|2149)[0-9]{11}$"),
    ("JCB",           r"^(?:2131|1800|35\d{3})\d{11}$"),
    ("Voyager",       r"^8699[0-9]{12}$"),
    ("HiperCard",     r"^(606282\d{10}(\d{3})?)|(3841\d{15})$"),
    ("Aura",          r"^50[0-9]{14,17}$"),
]

def get_band(card_number):
    number = re.sub(r"\D", "", card_number)
    for name, pattern in BANDS:
        if re.match(pattern, number):
            return name
    return "Desconhecida"

def validar_cartao(card_number):
    number = re.sub(r"\D", "", card_number)
    valido = luhn_check(number)
    bandeira = get_band(card_number)
    return valido, bandeira

if __name__ == "__main__":
    numero = input("Digite o número do cartão: ")
    valido, bandeira = validar_cartao(numero)
    print(f"Cartão {'válido' if valido else 'inválido'}")
    print(f"Bandeira: {bandeira}")