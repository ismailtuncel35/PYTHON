"""
    1-Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

      Müşteri adı
      Müşteri soyadı 
      Müşteri ad+soyad
      Müşteri cinsiyet
      Müşteri tc kimlik
      Müşteri doğum yılı
      Müşteri adres bilgileri
      Müşteri yaşı
      """
      musteriAdi='Ali'
      musteriSoyad = 'Yılmaz'
      musteriAdSoyad=musteriAdi + '' + musteriSoyad
      print(musteriAdSoyad)
      musteriCinsiyet=True #erkek
      musteriTckimlik='12345678901'
      musteriDogumyılı='1989'
      musteriAdresi='izmir buca'
      musteriYasi=2019-musteriDogumyılı

      """
         2-Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
           sipariş 1=>110 TL
           sipariş 2=>1100.5 TL
           siparis 3=>356.95 TL
      """

      order1=110
      order2=1100.5
      order3=356.95

      total=order1+order2+order3

      print("Total:",total)