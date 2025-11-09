from typing import Tuple, Dict

oquvchilar = ['Ali', 'Vali', 'Hali']

baho: Dict[str, Tuple[int, ...]] = {
    'Ali': (4, 5),
    'Vali': (3, 4, 5),
    'Hali': (4, 3, 2)
}

malumot = {
    'Ali': '19/03/2007',
    'Vali': "12/07/2007",
    'Hali': '04/01/2007'
}

ism = None

while ism not in oquvchilar:
    if ism is not None:
        if input("Bizda bunday o'quvchilar yo'q. Uni qo'shasizmi, ha/yo'q: ").lower() == "ha":
            oquvchilar.append(ism)
            baho[ism] = tuple(
                int(i)
                for i
                in input(f"{ism}ning baholarini ',' belgisi bilan ajratib kiriting. Masalan 3,4,5: ").split(",")
                if i.isdigit()
            )
            malumot[ism] = input(f"{ism} tugilgan sanasini kun/oy/yil kabi kiriting: ")
            break
    ism = input(f'Qaysi oquvchining malumotlarini qidiryabsz {oquvchilar}, birini ismini yozing = ').title()

mal = input(f'{ism} ning qaysi malumotlar kerak bizda (baholar), (tugulgan sanasi) = ').lower()

if mal == 'baholar':
    print(f"{ism} ning baholari: {baho[ism]}")
elif mal == 'tugulgan sanasi':
    print(f"{ism} ning tug‘ilgan sanasi: {malumot[ism]}")
else:
    print("Bunday ma'lumot turi yo‘q.")
