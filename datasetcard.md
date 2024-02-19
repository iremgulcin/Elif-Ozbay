---
# Dataset Card
---

# Fer2013

## Dataset Details

### Dataset Description

Fer2013 veri seti, çeşitli duyguları içeren yüz ifadelerinin bulunduğu bir koleksiyondur. 
Toplamda 35.887 siyah-beyaz görüntü içerir ve yedi duygu sınıfına ayrılmıştır.


- **Curated by:** {{ curators | default("[More Information Needed]", true)}}
- **License:** {{ license | default("[More Information Needed]", true)}}

## Uses

### Direct Use

Bu veri seti, duygu tanıma yeteneklerini geliştirmek için kullanılabilir. 
Otizm spektrum bozukluğu teşhisi konmuş bireyler için duygu analiz yeteneklerini geliştirmeye yönelik uygulamalar için kullanılmıştır.


## Dataset Structure

Veri seti, her bir görüntünün etiketlenmiş olduğu ve yedi farklı duygu sınıfına (kızgın, iğrenmiş, korku, mutlu, üzgün, şaşırmış, normal) ayrılmış bir yapıya sahiptir.

## Dataset Creation

### Source Data

Veri seti, Kaggle üzerinden elde edilmiştir.

#### Data Collection and Processing

Veri toplama süreci, Kaggle üzerinden Fer2013 veri setinin indirilmesiyle başlamıştır. Bu veri seti, çeşitli duyguları içeren yüz ifadelerini içermektedir. Toplamda 35.887 siyah-beyaz görüntü bulunmaktadır ve her bir görüntü belirli bir duygu sınıfına ayrılmıştır.

Veri işleme sürecinde, öncelikle görüntülerin etiketleri ve dosya yolları toplanmıştır. Bu adım, her duygu sınıfı için ilgili klasörlerdeki görüntülerin yollarının belirlenmesini içerir. Ardından, bu bilgiler bir DataFrame'e dönüştürülmüştür.

DataFrame oluşturulduktan sonra, veri setinin dağılımını görselleştirmek için etiket sayıları çubuk grafik ile incelenmiştir. Bu adım, veri setinin dengeli mi yoksa dengesiz mi olduğunu anlamak için önemlidir.

Veri seti daha sonra eğitim ve test kümelerine ayrılmıştır. Görüntülerin boyutlarının uygun hale getirilmesi ve piksel değerlerinin 0 ile 1 arasında ölçeklenmesi gibi ön işleme adımları yapılmıştır.

Son olarak, veri seti ImageDataGenerator kullanılarak akışlara dönüştürülmüş ve model eğitimi için hazır hale getirilmiştir.

#### Features and the target

Veri seti, duygusal ifadeleri temsil eden siyah-beyaz görüntüler içermektedir. Her bir görüntü, yüz ifadesinin görsel temsili olarak hizmet eder.

Bu projenin temel amacı, otizm spektrum bozukluğu (OSB) tanısı konmuş bireyler için duygu analizi yeteneklerini geliştirmeye yardımcı olmaktır. Duygu analizi, bireylerin duygusal ifadeleri tanıma, yorumlama ve tepki verme becerilerini içerir. Bu beceriler, sosyal etkileşimlerde ve günlük yaşamda önemli rol oynar.

Proje, Fer2013 veri setini kullanarak derin öğrenme tekniklerini uygulayarak gerçekleştirilmiştir. Bu derin öğrenme modeli, yüz ifadelerini tanıyıp sınıflandırmak için eğitilmiştir. Sonuç olarak, OSB tanısı konmuş bireyler, duygusal ifadeleri daha doğru bir şekilde tanıma ve anlama becerilerini geliştirebilirler. Bu da onların sosyal etkileşimlerde daha başarılı olmalarına ve yaşam kalitelerinin artmasına yardımcı olabilir.


## Bias, Risks, and Limitations

Teknik Kısıtlar:

•Veri Kalitesi: Modelin doğruluğunu etkileyen temel bir faktör veri kalitesidir. Eğer veri setinde gürültülü veya yanlış etiketlenmiş veriler bulunuyorsa, modelin doğruluğu düşebilir.
•Veri Dengesizliği: Veri setindeki sınıflar arasında dengesizlik varsa, model bazı duyguları diğerlerine göre daha az doğru tahmin edebilir. Özellikle, "iğrenme" duygusunun az verisi olması, bu duygunun tahmininde zorluk yaşanmasına neden oluyor.
•Model Karmaşıklığı: Kullanılan modelin karmaşıklığı, eğitim süresi ve hesaplama gücünü etkiler. Daha karmaşık modeller, daha fazla eğitim verisine ve hesaplama kaynağına ihtiyaç duyabilir.

Sosyoteknik Kısıtlar:

•Algoritmik Adaletsizlik: Modelin, farklı gruplara karşı adil davranıp davranmadığına dikkat edilmelidir. Eğitim verisi veya modelin tasarımı, bazı gruplara karşı önyargılı olabilir ve bu da algoritmik adaletsizliğe yol açabilir.
•Gizlilik ve Güvenlik Endişeleri: Hassas verilerin işlenmesi, bireylerin gizlilik ve güvenlik endişelerine neden olabilir. Özellikle duygusal verilerin işlenmesi, kullanıcıların gizliliğinin korunması için dikkatle ele alınmalıdır.




