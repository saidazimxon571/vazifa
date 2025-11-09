ismlar=['said','ali','vali','hali']
ismlar.remove('ali')
eliment=ismlar.pop(1)
del ismlar[1]
print(ismlar)
# remove() bu method listdagi royhatning nomiga qarab ochiradi yani nomini yozsangiz osha nomdagi malumotni ochiradi
# pop() bu method indexga qarab malumot turini ochiradi va uni biron bir boshqa siz korsatgan listga saqlab qoyish imkonyatiga ega
# del() bu method esa elimentni index ga qarab ochiradi lekin bu saqlamaydi tagi bilan ochrib tashlaydi