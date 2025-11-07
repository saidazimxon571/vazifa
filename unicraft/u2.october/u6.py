sonlar=list(range(0,101))
sonlar.reverse()
boshidagi_10=sonlar[:10]
print('boshidagi 10 ta son = ',boshidagi_10)
uzunlik=len(sonlar)
orta_index=uzunlik//2
boshlangich=orta_index-5
oxrigi_index=orta_index+5
ortadagi_10=sonlar[boshlangich:oxrigi_index]
print('ortadagi 10 ta = ', ortadagi_10)
oxri_10=sonlar[-11:]
print('oxridagi 10 ta son = ',oxri_10)