# Python Math Interpreter

Bu proje, basit matematiksel ifadeleri (örneğin, `2 + 3 * 4`) işleyebilen bir dil işlemci (interpreter) örneğidir. Proje, bir Lexer (tokenizer), Parser ve Interpreter içerir. Bu bileşenler, girdi olarak verilen matematiksel ifadeleri işleyerek sonuçları hesaplar.

## Proje Yapısı

Proje, aşağıdaki bileşenlerden oluşur:

1. **Lexer**: Girdi metnini token'lara ayırır.
2. **Parser**: Token'ları alarak bir *Abstract Syntax Tree (AST)* oluşturur.
3. **Interpreter**: AST'yi gezerek matematiksel ifadeyi değerlendirir ve sonucu hesaplar.

## Kurulum

Projeyi kullanmak için herhangi bir ek kurulum gerekmemektedir. Python 3.x yüklü bir ortamda çalıştırmanız yeterlidir.

## Kullanım

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. Terminalde proje dizinine gidin.
2. `run.py` dosyasını çalıştırın:

```bash
python3 run.py
```

3. Program `calc >` şeklinde bir girdi istemi (prompt) gösterecektir. Matematiksel ifadeleri (örneğin, `2 + 3 * 4`) girebilirsiniz.
4. Çıkmak için `q` yazıp Enter tuşuna basın.

## Testleri Çalıştırma

Testleri çalıştırmak için aşağıdaki kodu çalıştırın:

```bash
python3 -m unittest discover -s src/tests
```

### Örnek Kullanım

```bash
calc > 2 + 3 * 4
# : 14.0

calc > 10 / 2 - 1
# : 4.0

calc > q
```

## Bileşenler

### 1. Lexer

Lexer, girdi metnini alır ve bu metni token'lara ayırır. Her token, bir tür (**TokenType**) ve bir değer (**value**) içerir. Örneğin, `2 + 3` ifadesi şu token'lara ayrılır:

- **NUMBER(2)**
- **PLUS**
- **NUMBER(3)**

#### Lexer Sınıfı

- `__init__`: Lexer'ı başlatır ve girdi metnini işler.
- `advance`: Bir sonraki karaktere geçer.
- `number`: Sayıları okur ve float olarak döndürür.
- `get_next_token`: Bir sonraki token'ı döndürür.

### 2. Parser

Parser, Lexer tarafından üretilen token'ları alır ve bu token'ları kullanarak bir **Abstract Syntax Tree (AST)** oluşturur. AST, matematiksel ifadenin yapısını temsil eder.

#### Parser Sınıfı

- `factor`: Sayıları işler ve **Num** düğümü oluşturur.
- `term`: Çarpma ve bölme işlemlerini işler.
- `expr`: Toplama ve çıkarma işlemlerini işler.
- `parse`: İfadeyi ayrıştırır ve AST'nin kök düğümünü döndürür.

### 3. Interpreter

Interpreter, AST'yi gezerek matematiksel ifadeyi değerlendirir ve sonucu hesaplar.

#### Interpreter Sınıfı

- `visit_BinOp`: İkili operasyonları (+, -, *, /) değerlendirir.
- `visit_Num`: Sayı düğümlerini değerlendirir.
- `visit`: AST düğümlerini gezerek uygun **visit** metodunu çağırır.
- `interpret`: AST'yi değerlendirir ve sonucu döndürür.  

## Örnek AST Yapısı

`2 + 3 * 4` ifadesi için oluşturulan AST şu şekildedir.

```bash
 +
/ \
2  *
  / \
 3   4
```

## Hata Yönetimi

- **Invalid Character**: Lexer, geçersiz karakterlerle karşılaştığında hata fırlatır.
- **Syntax Error**: Parser, beklenen token'lar bulunmadığında hata fırlatır.
- **Division by Zero**: Interpreter, sıfıra bölme işlemi tespit ederse hata fırlatır.

## Contribution

Bu proje açık kaynaklıdır. Katkıda bulunmak için:

1. Bu depoyu forklayın.
2. Yeni bir branch oluşturun (`git checkout -b yeni-ozellik`).
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`).
4. Branch'inizi pushlayın (`git push origin yeni-ozellik`).
5. Bir Pull Request oluşturun.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için **LICENSE** dosyasına bakın.
