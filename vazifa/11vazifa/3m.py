ombor = {
    'anor': 25,
    'olma': 15,
    'xurmo': 34,
    'anjir': 21,
}
yangi = ''
miqdor = ''

qidirish = input(f'Szga qaysi mahsulot kerak = ')

for k, v in ombor.items():
    if qidirish == k:
        print(f'bizda {qidirish}dan {v} kg bor')
    if qidirish != k:
        yangi = input(f'Afsus bizning omborda bunday mahsulot tugabdi qoshishni istaysizmi ha/yoq = ')
    if yangi == 'ha':
        miqdor = int(input(f'necha kg {qidirish} qoshmoqchisz  = '))
        ombor = {qidirish: miqdor}
