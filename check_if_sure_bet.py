odd1 = float(input('First odd: '))
odd2 = float(input('Second odd: '))

def convert(odd):
    if odd > 0:
        return (odd/100 + 1)
    if odd < 0:
        return (1 - (100/odd))
        
odd1 = round(convert(odd1),2)
odd2 = round(convert(odd2),2)
print(f"Decimal odd1: {odd1}")
print(f"Decimal odd2: {odd2}")

if (1/odd1 + 1/odd2 < 1): print('This is a sure bet')
roi = round((1 - (odd1/(odd1+odd2)))*100*odd1 - 100, 2) 
print(f"ROI: {roi}%")