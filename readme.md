## Authentication

Bu API, HTTP Authorization başlığı kullanarak yetkilendirme sağlar. "bearer" tipi kullanarak, "token" anahtarında kullanıcının token değerini alır.

## Card

Bu özellik grubu, kullanıcının kaydedilmiş kredi kartlarını yönetmek için kullanılır.

### Save Card

Bu istek, belirtilen bir kullanıcının kredi kartı bilgilerini kaydeder.

* Endpoint: POST /save-card
* Body: JSON formatında kullanıcı numarası (`userNo`) ve kredi kartı numarası (`cardNumber`) alanlarını içerir.

### Cards

Bu istek, belirtilen bir kullanıcının kaydedilmiş kredi kartlarını listeler.

* Endpoint: GET /saved-list
* Body: JSON formatında kullanıcı numarası (`userNo`) alanını içerir.

## Payment

Bu özellik grubu, kullanıcının ödemelerini yönetmek için kullanılır.

### Payment

Bu istek, belirtilen bir kullanıcının belirtilen tutarda ödeme yapmasını sağlar.

* Endpoint: POST /saved-payment
* Body: JSON formatında kullanıcı numarası (`userNo`) ve ödeme tutarı (`payment`) alanlarını içerir.
* Response: Boş bir yanıt döndürür.

### Cancel

Bu istek, belirtilen bir kullanıcının belirtilen ödemeyi iptal etmesini sağlar.

* Endpoint: POST /cancel-payment
* Body: JSON formatında kullanıcı numarası (`userNo`) ve ödeme tutarı (`payment`) alanlarını içerir.
