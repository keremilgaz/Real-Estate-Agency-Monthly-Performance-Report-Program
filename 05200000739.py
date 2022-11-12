#Bütün verilerin değerlerini girmeden önce 0 ladım çünkü başta yazmazsam hata verebiliyor.(Pycharm da sarı dikkat işareti çıkıyor yazmazsam eğer)
ASGARI_UCRET = 2324.70
IKRAMIYE = 1162.35
konut_satis_total = 0
isyeri_satis_total = 0
arsa_satis_total = 0
kira_total = 0
konut_kira_max = 0
emlak_komisyon_total = 0
konut_satis_en_total = 0
arsa_satis_en_total = 0
isyeri_satis_en_total = 0
konut_satis_sayi = 0
isyeri_satis_sayi = 0
arsa_satis_sayi = 0
konut_kira_sayi = 0
arsa_kira_sayi = 0
isyeri_kira_sayi = 0
en_yuksek_satis_rekor = 0
en_yuksek_satis_rekor_isim = "suanyok"
en_yuksek_satis_rekor_tipi = "suanyok"
en_yuksek_kira_rekor = 0
en_yuksek_kira_rekor_isim = "suanyok"
kira_asgariden_yuksek = 0
hic_satis_yapmayan_sayi = 0
en_cok_satis_yapanin_sayi = 0
en_cok_satis_yapanin_isim = "suanyok"
rekor_satis = 0
rekor_satis_isim = "suanyok"
komisyon_dolduran_sayi = 0
primi_maastan_yuksek_sayi = 0
kira_10_veya_25000 = 0
max_prim = 0
yuksek_primli_maas = 0
yuksek_primli_isim = "suanyok"
yuksek_primli_tam_kazanc = 0
min_prim = 999999999
min_primli_maas = 0
min_primli_isim = "suanyok"
toplam_komisyon = 0
min_primli_tam_kazanc = 0
toplam_ucret = 0
# Çalışan sayısını alıp kontrol ettiğim kısım.
calisan_sayi = int(input("Lütfen emlak ofisindeki çalışan sayısını giriniz:"))
while calisan_sayi < 0:
    calisan_sayi = int(input("Çalışan sayısı 0 dan küçük olamaz:"))
# Çalışan sayısı kadar dönecek olan for fonksiyonunu burada kullandım.
for i in range(calisan_sayi):
    kira_fiyati_yuksek_25000 = 0
    satis_adedi = 0
    kira_adedi = 0
    satis_kira_toplam_adet = 0
    konut_satis_total = 0
    isyeri_satis_total = 0
    arsa_satis_total = 0
    kira_total = 0
    konut_kira_max = 0
    satis_komisyon = 0
    emlak_komisyon_total = 0
    kota = 0
    kira_en_az_on = 0
    konut_kira_adeti_tek_kisi = 0
    konut_kira_bedeli = 0
# çalışan kişinin adını ve maaşını alıp kontrol ettim ve maaşına göre kotasını belirledim. Alttaki while döngüsü başka satış olduğu sürece True dönecek.
    isim = input("Emlak danışmanın adını ve soyadını giriniz:")
    maas = float(input("Emlak danışmanının maaşını giriniz:"))
    while maas < ASGARI_UCRET:
        maas = float(input("Maaş asgari ücretten düşük olamaz tekrar giriniz:"))
    kota = float(input("Emlak danışmanının kotasını giriniz:"))
    while kota < maas*10:
        kota = float(input("Kota maaşın 10 katından büyük olmalı:"))
    print("O ay sattığı ya da kiraladığı her emlak için:")
    baska_satis_varmi = True
    while baska_satis_varmi:
        satis_komisyon = 0
# Emlak tipini aldım
        emlak_tipi = input("emlak tipi(Konut, İş yeri, Arsa)(K/k/İ/i/A/a):")
        while emlak_tipi not in ["K", "k", "İ", "i", "A", "a"]:
            emlak_tipi = input("Emlak tipini doğru giriniz:")
#İşlem türünü aldım. Aşağıya satış ve kiraya göre artacak sayaçlar koydum
        islem_turu = input("işlem türü (Satış, Kiralama) (S/s/K/k):")
        while islem_turu not in ["S", "s", "K", "k"]:
            islem_turu = input("işlem türünü doğru giriniz:")
        satis_kira_toplam_adet += 1
        if islem_turu in ["S", "s"]:
            satis_adedi += 1
        else:
            kira_adedi += 1
# Burada yapılan işlemin inputunu aldım eğer satış ise komisyonunu hesapladım
        bedel_ucret = float(input("Satış/kira bedeli(TL):"))
        while bedel_ucret < 0:
            bedel_ucret = float(input("Satış/kira bedeli 0 dan küçük olamaz:"))
        if islem_turu in ["S", "s"]:
            if rekor_satis < bedel_ucret:
                rekor_satis = bedel_ucret
                rekor_satis_isim = isim


        if islem_turu in ["S", "s"]:
            satis_komisyon = (bedel_ucret/100)*4
            emlak_komisyon_total += satis_komisyon

# emlak tiplerine göre satışları hesapladım alttaki if te ise rekor satışı tutacak bir değişken belirlerim
            if emlak_tipi in ["K", "k"] and islem_turu in ["S", "s"]:
                konut_satis_total += bedel_ucret
                konut_satis_en_total += konut_satis_total
                konut_satis_sayi += 1
            elif emlak_tipi in ["İ", "i"] and islem_turu in ["S", "s"]:
                isyeri_satis_total += bedel_ucret
                isyeri_satis_en_total += isyeri_satis_total
                isyeri_satis_sayi += 1
            elif emlak_tipi in ["A", "a"] and islem_turu in ["S", "s"]:
                arsa_satis_total += bedel_ucret
                arsa_satis_en_total += arsa_satis_total
                arsa_satis_sayi += 1
            if en_yuksek_satis_rekor < bedel_ucret:
                en_yuksek_satis_rekor_isim = isim
                en_yuksek_satis_rekor = bedel_ucret
                en_yuksek_satis_rekor_tipi = emlak_tipi
# islem türü kira girilirse ona göre emlak komisyonunu hesapladım kira_en_az_on da ise kira adetini sayan bir değişken koydum
        if islem_turu in ["K", "k"]:
            emlak_komisyon_total += bedel_ucret
            kira_total += bedel_ucret
            kira_en_az_on += 1
            kira_fiyati_yuksek_25000 += bedel_ucret
            if emlak_tipi in ["K", "k"]:
                konut_kira_adeti_tek_kisi += 1
                konut_kira_bedeli += bedel_ucret
# Burada maksimum konut kirasını hesaplayan bir if kullandım fakat bu konut_kira_max bu looptan sonra sıfırlanıyor.
            if konut_kira_max < bedel_ucret and emlak_tipi in ["K", "k"]:
                konut_kira_max = bedel_ucret
#Buradaki en yüksek kira rekor ise sıfırlanmıyor
        if islem_turu in ["K", "k"] and emlak_tipi in ["K", "k"]:
            konut_kira_sayi += 1
            if en_yuksek_kira_rekor < bedel_ucret:
                en_yuksek_kira_rekor = bedel_ucret
                en_yuksek_kira_rekor_isim = isim
        elif islem_turu in ["K", "k"] and emlak_tipi in ["İ", "i"]:
            isyeri_kira_sayi += 1
        elif islem_turu in ["K", "k"] and emlak_tipi in ["A", "a"]:
            arsa_kira_sayi += 1
        if islem_turu in ["K", "k"] and emlak_tipi in["K", "k"] and bedel_ucret > ASGARI_UCRET:
            kira_asgariden_yuksek += 1
        bedel_ucret = 0
        if islem_turu in ["K", "k"] and (kira_en_az_on > 10 or kira_fiyati_yuksek_25000 > 25000):
            kira_10_veya_25000 += 1
# Burada emlak danışmanının o ay içinde başka satış yapıp yapmadığı soran bir input kullandım eğer satış yapmış ise True dönüyor ve loopa giriyor.
        baska_satis_varmi = input("o ay sattığı/kiraladığı başka emlak olup olmadığı(E/e/H/h):")
        while baska_satis_varmi not in ["E", "e", "H", "h"]:
            baska_satis_varmi = input("Lütfen doğru giriniz:")
        if baska_satis_varmi in ["E", "e"]:
            baska_satis_varmi = True
        else:
            baska_satis_varmi = False
    satis_toplam = konut_satis_total + isyeri_satis_total + arsa_satis_total + kira_total
    prim = (emlak_komisyon_total*10)/100
#Burada max primi bulabilip sonra printleyebilmek için değişken kullandım.
    if prim > max_prim:
        max_prim = prim
        yuksek_primli_isim = isim
        yuksek_primli_maas = maas
        if kota < kira_total + emlak_komisyon_total:
            yuksek_primli_tam_kazanc = IKRAMIYE+maas+prim
        else:
            yuksek_primli_tam_kazanc = maas+ prim
    if satis_adedi > en_cok_satis_yapanin_sayi:
        en_cok_satis_yapanin_sayi = satis_adedi
        en_cok_satis_yapanin_isim = isim
    if satis_adedi == 0:
        hic_satis_yapmayan_sayi += 1
#burada ise minimum primli kişiyi buldum ve printlemek için verilerini aldım.
    if prim < min_prim:
        min_prim = prim
        min_primli_isim = isim
        min_primli_maas = maas
        if kota < kira_total + emlak_komisyon_total:
            min_primli_tam_kazanc = IKRAMIYE + maas + prim
        else:
            min_primli_tam_kazanc = maas + prim
#Kaç kişinin priminin maaştan yüksek olup olmadığını anlamak için denklem kurdum ve printlemek için kaydettim
    if prim > maas:
        primi_maastan_yuksek_sayi += 1
    if emlak_komisyon_total > kota:
        komisyon_dolduran_sayi += 1

# Toplam komisyonu bulmak için kullandığım denklem
    toplam_komisyon += emlak_komisyon_total
# Burada sadece o çalışan için printlenecek verileri yazdım buradaki veriler sıkıntı çıkmaması için başka çalışana geçtikten sonra sıfırladım.
    print("Danışmanın adı ve soyadı:" + str(isim))
    print("o ay sattığı emlak adedi:" + str(satis_adedi))
    a = ((satis_adedi/satis_kira_toplam_adet)*100)
    a = format(a, '.2f')
    print("o ay sattığı emlak adedinin oranı: %" + str(a))
    print("o ay kiraladığı emlak adedi:" + str(kira_adedi))
    b = ((kira_adedi/satis_kira_toplam_adet)*100)
    b = format(b, '.2f')
    print("o oy kiraladığı emlak adedinin oranı: %" + str(b))
    print("o ay sattığı emlakların tiplerine göre toplam bedelleri;")
    print("konut satışından total:" + str(konut_satis_total))
    print("işyeri satışından total:" + str(isyeri_satis_total))
    print("arsa satışından total:" + str(arsa_satis_total))
    c = (konut_kira_bedeli/konut_kira_adeti_tek_kisi)
    c = format(c, '.2f')
    print("O ay kiraladığı konutların ortalama kira bedeli:" + str(c))
    print("o ay en yüksek bedelle kiraladığı konutun kira bedeli:" + str(konut_kira_max))
    print("O ay maaşı:" + str(maas))
    print("O ay primi:" + str((emlak_komisyon_total/100)*10))
    print("o ay kotası:" + str(kota))
    print("o ay acentaya kazandırdığı toplam komisyon tutarı:" + str(emlak_komisyon_total))
    if kota <= emlak_komisyon_total:
        print("Kotasını doldurmuştur.")
        print("Alacağı ikramiye tutarı:" + str(IKRAMIYE))
        print("o ay toplam ücreti:" + str(IKRAMIYE+maas+prim))
        toplam_ucret += IKRAMIYE+maas+prim
    else:
        print("Kota dolmamıştır. İkramiye alamaz.")
        print("o ay toplam ücreti:" + str(maas+prim))
        toplam_ucret += maas + prim
#Burada artık başka çalışan kalmayınca printlenecek şeyleri yazdım
print("Her emlak için o ay satılan ve kiralanan emlak sayıları ile satılma oranları;")
print("Satılan konut, işyeri ve arsa sayıları sırasıyla:" + str(konut_satis_sayi) +str("/")+ str(isyeri_satis_sayi) +str("/")+ str(arsa_satis_sayi))
print("Kiralanan konut, işteri ve arsa sayıları sırasıyla:"+ str(konut_kira_sayi) +str("/")+ str(isyeri_kira_sayi) +str("/")+ str(arsa_kira_sayi))
d = (konut_satis_sayi/(konut_kira_sayi+konut_satis_sayi))*100
d = format(d, '.2f')
print("konut satılma oranı: %" + str(d))
e = (isyeri_satis_sayi/(isyeri_satis_sayi+isyeri_kira_sayi))*100
e = format(e, '.2f')
print("işyeri satılma oranı: %" + str(e))
f = (arsa_satis_sayi/(+arsa_satis_sayi+arsa_kira_sayi))*100
f = format(f, '.2f')
print("Arsa satılma oranı: %" + str(f))
print("Arsa satış toplamı:" + str(arsa_satis_en_total))
g = arsa_satis_en_total/arsa_satis_sayi
g = format(g, '.2f')
print("Arsa satış fiyat ortalaması:" + str(g))
print("Konut satış toplamı:" + str(konut_satis_en_total))
h = konut_satis_en_total/konut_satis_sayi
h = format(h, '.2f')
print("konut satış fiyat ortalaması:" + str(h))
print("İşyeri satış toplamı:" + str(isyeri_satis_en_total))
j = isyeri_satis_en_total/isyeri_satis_sayi
j = format(j, '.2f')
print("İşyeri satış fiyat ortalaması:" + str(isyeri_satis_en_total/isyeri_satis_sayi))
print("O ay en yüksek bedelle satılan emlağın tipi, satış bedeli, satışı yapan danışman:" + en_yuksek_satis_rekor_tipi +str("/")+ str(en_yuksek_satis_rekor) +str("/")+ en_yuksek_satis_rekor_isim)
print("O ay en yüksek bedelle kiralanan konutun kira bedeli ve danışmanın ismi:" + str(en_yuksek_kira_rekor) + str("/") + en_yuksek_kira_rekor_isim)
print("O ay kiralanan konutlardan kirası asgari ücretten yüksek olanların sayısı:" + str(kira_asgariden_yuksek))
k = (kira_asgariden_yuksek/konut_kira_sayi)*100
k = format(k, '.2f')
print("O ay kiralanan konutlardan kirası asgari ücretten yüksek olanların yüzdesi: %" + str(k))
print("O ay hiç satış yapmayan danışmanların sayısı:"+ str(hic_satis_yapmayan_sayi))
l = (hic_satis_yapmayan_sayi/calisan_sayi)*100
l = format(l, '.2f')
print("O ay hiç satış yapmayanların tüm danışmanlar içindeki oranı: %" + str(hic_satis_yapmayan_sayi/calisan_sayi)*100)
print("O ay en çok satış adedi olarak en çok satış yapan isim ve satış adedi:" + en_cok_satis_yapanin_isim + str("/") + str(en_cok_satis_yapanin_sayi))
print("O ay en yüksek bedelle satış yapan isim ve satış bedeli:" + str(rekor_satis) + str("/") + str(rekor_satis_isim))
print("O ay kotasını dolduran danışmanların sayısı:" + str(komisyon_dolduran_sayi))
m = (komisyon_dolduran_sayi/calisan_sayi)*100
m = format(m, '.2f')
print("O ay koyasını dolduran danışmanların oranı: %" + str(m))
print("O ay primi maaşından yüksek olan danışmanların sayısı:" + str(primi_maastan_yuksek_sayi))
n = (primi_maastan_yuksek_sayi/calisan_sayi)*100
n = format(n, '.2f')
print("O ay primi maaşından yüksek olan danışmanların tüm danışmanlar içindeki oranı: %" + str(n))
print("O ay en az 10 adet veya en az 25000TL tutarında emlak kiralayan danışmanların sayısı:" + str(kira_10_veya_25000))
print("O ay en yüksek prim alan danışmanın sırası ile adı, maaşı, primi ve o ayki total ücreti:" + str(yuksek_primli_isim)+str("/")+str(max_prim)+str("/")+str(yuksek_primli_maas)+str("/")+str(yuksek_primli_tam_kazanc))
print("O ay en düşük prim alan danışmanın sırası ile adı, maaşı, primi ve o ayki total ücreti"+str(min_primli_isim)+str("/")+str(min_prim)+str("/")+str(min_primli_maas)+str("/")+str(min_primli_tam_kazanc))
print("O ay tüm danışmanlara ödenecek toplam ücret:" + str(toplam_ucret))
w = toplam_ucret/calisan_sayi
w = format(w, '.2f')
print("O ay danışmanlara ödenecek ücretin ortalaması:" + str(w))
print("O ay acentanın kazandığı toplam komisyon:" + str(toplam_komisyon))










