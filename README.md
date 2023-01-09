# نصب ردیس

<p style="text-align: right; direction: rtl">
اگر از لینوکس یا یونیکس استفاده می کنید کار شما خیلی راحت تره و میتونید به گام بعدی برید، اما اگر شما هم مثل من از ویندوز برای کارهای روزمره و برنامه نویسی استفاده می کنید، باید بهتون بگم که ردیس برای ویندوز وجود نداره.
</p>
<p style="text-align: right; direction: rtl">
تا آموزش بعدی خدا نگه دار. خخخخ
نه صبر کن شوخی کردم.
</p>
<p style="text-align: right; direction: rtl">
برای استفاده از ردیس در ویندوز دو راحت حل دارید، استفاده از لینوکس مجازی داخل ویندوز و یا استفاده از کانتینر داکر.
</p>

<div style="display: flex; justify-content: center">


![docker](/assets/docker.png)

</div>

<p style="text-align: right; direction: rtl">
داکر در واقع یک محیط مجازی برای اجرای برنامه هاست که میتونید از طریق این محیط برنامه های خودتون رو اجرا کنید. اگر از داکر استفاده کنید، باید ابتدا داکر رو نصب کنید.
</p>

<p style="text-align: right; direction: rtl">

برای راهنمای نصب داکر به این صفحه مراجعه کنید: [داکر در ویندوز](https://docs.docker.com/docker-for-windows/install/)

</p>
<p style="text-align: right; direction: rtl">
پس از نصب داکر کد
</p>

<div style="direction: rtl; display: flex;justify-content: flex-start">

```shell
docker run --name some-redis -d redis
```

</div>
<p style="text-align: right; direction: rtl">
را در پاور شل یا CMD وارد کنید و شما آماده استفاده از ردیس هستید.
</p>

چنانچه مراحل بالا با موفقیت برای شما انجام نشد و یا دوست ندارید از داکر استفاده کنید، میتوانید با باز کردن پاورشل
با وارد کردن دستور:

```shell
    wsl -install -d ubuntu
```

چنانچه به دلیل مشکلات اینترنت از پراکسی استفاده می کنید، برای دانلود از طریق پراکسی قبل از دانلود خود لینوکس این دستور را در پاورشل وارد کنید:

```shell
    netsh winhttp import proxy source=ie
    netsh winhttp set proxy "your ip:port"
```

پس از نصب کامل در سرچ ویندوز خود عبارت `ubuntu` را سرچ کنید و روی آن کلیک کنید

به دنیای لینوکس خوش آمدید

مطابق با راهنمای رسمی ردیس با وارد کردن کد های زیر میتوانید ردیس را نصب نمایید

```shell
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```

پس از پایان عملیات میتوانید با دستور

```shell
sudo service redis-server start

redis-cli 
```

وارد محیط cli (command line interface) ردیس شوید

برای تایید آن عبارت `ping` را وارد کنید و در صورتی که پاسخ `PONG` باشد، ردیس با موفقیت نصب شده است


# ردیس مانند دیکشنری پایتون

ردیس کاربرد های متنوع و گوناگونی دارو اما در ابتدا برای اینکه اندکی با محیط و درستورات آن آشنا شویم، با ردیس مانند یک دیکشنری پایتون برخورد می کنیم، اما به زودی متوجه خواهید شد که چه مزیتی نسبت به آن دارد.

ردیس همانند دیکشنری پایتون دارای ساختار کلید و محتواست، گرچه کلید های آن از نوع متنی هستند ولی مقدار آنها میتواند به صورت های
`string` 
`hash`
`set`
`list`
باشد.

به منظور ثبت مقدار در ردیس از دستور زیر استفاده می کنیم:

```shell
SET key value
```

استفاده می شود که معادل دستور

```python
dictionary = dict()
dictionary["key"] = "value"
```
می باشد

همچنین برای خواندن اطلاعات از دستور

```shell
GET key
```

استفاده می شود که معادل دستور

```python
dictionary.get(key)
```

دلیل اینکه این عبارت برابر با 

```python
dictionary[key]
```

نمیشود این است که در صورتی که در ردیس یک کلید وجود نداشته باشد آن را `null` برمیگرداند یا بهتر است به زبان ردیس بگوییم `nil`

نکته قاب توجه در این قسمت آن است که در این ساختار کلید و مقدار در ردیس، همانند دیکشنری ها در پایتون پیچیدگی زمانی عددی دارد، یعنی یک فرمان برای آن اجرا میشود.





## پیچیدگی زمانی چیست
<p style="text-align: right; direction: rtl">
فرض کنید در داخل دیتابیس لیست اسم و شماره تماس تمام آدم های کره زمین رو داشته باشیم، برای اینکه از بین همه آدم های کره زمین،‌سید سینا صادق اصفهانی رو در بیاریم، باید روی تک تک ردیف های دیتابیس حرکت کنیم و اسم رو با سید سینا صادق اصفهانی مقایسه کنیم.
</p>
<p style="text-align: right; direction: rtl">
اگر فرض کنیم که این اسم در خانه آخر دیتابیس باشه برای انجام این عملیات به اندازه ادم های کره زمین عملیات باید انجام بشه. یا به عبارت ساده تر میزان عملیاتی که باید انجام بشه وابسطه به ورودی داده ما (در اینجا افراد کره زمین) است. 
این وابستگی به ورودی داده پیچیدگی زمانیه که در این مثال برابر O(n) است.
</p>

حالا فرض کنید اگر ما این لیست رو یک بار بر اساس حروف الفبا مرتب سازی کنیم.

![docker](/assets/binary-3.png)

در این حالت ابتدا لیست رو نصف می کنیم، اسم وسطی رو با اسمی که میخواییم مقایسه می کنیم، اگر اسم ما از نظر الفبایی قبل از اون داده وسطی بود، داده های بعدی اون رو میذاریم کنار، این کار رو به مدت محدودی انجام میدیم و به داده مورد نظرمون میرسیم. در این مثال میبینید که تعداد عملیات همچنان به تعداد ورودی وابسطه است اما به گونه ای دیگر. اگر فرض کنیم که ۶ میلیارد ادم داشته باشیم:

```shell
6,000,000,000 / 2 = 3,000,000,000
3,000,000,000 / 2 = 1,500,000,000
1,500,000,000 / 2 = 750,000,000
750,000,000 / 2 = 375,000,000
375,000,000 / 2 = 187,500,000
187,500,000 / 2 = 93,750,000
93,750,000 / 2 = 46,875,000
46,875,000 / 2 = 23,437,500
23,437,500 / 2 = 11,718,750
11,718,750 / 2 = 5,859,375
5,859,375 / 2 = 2,929,687
2,929,687 / 2 = 1,464,843
1,464,843 / 2 = 732,421
732,421 / 2 = 366,210
366,210 / 2 = 183,105
183,105 / 2 = 91,552
91,552 / 2 = 45,776
45,776 / 2 = 22,888
22,888 / 2 = 11,444
11,444 / 2 = 5,722
5,722 / 2 = 2,861
2,861 / 2 = 1,430
1,430 / 2 = 715
715 / 2 = 357
357 / 2 = 178
178 / 2 = 89
89 / 2 = 44
44 / 2 = 22
22 / 2 = 11
11 / 2 = 5
5 / 2 = 2
2 / 2 = 1
```

در بد ترین شرایط با ۳۲ عملیات به نتیجه میرسیم. این مقدار به این دلیل کمتر از ۳۲ است که این لیست رو مرتب کردیم. اگر این لیست رو مرتب نکردیم، باید تعداد عملیات بیشتری انجام بدیم. این مثال رو میتونید در این لینک ببینید:

برای مطالعه بیشتر در خصوص جست و جوی باینری به این لینک مراجعه کنید:

[https://www.youtube.com/watch?v=JQhciTuD3E8](https://www.youtube.com/watch?v=JQhciTuD3E8)


به طور کلی تمامی الگوریتم ها رو میشه با این شیوه توصیف کرد

![docker](/assets/all.png)

### نکته قابل توجه اینکه اکثر دستورات ردیس O(1) هستند
یکی از دلایل جذابیت ردیس برای ما همینه.


## Hash tables

صبر کنید پنیک نکنید، این هش تیبل اصلا چیز نا آشنایی نیست و تا حالا کلی باهاش کار کردید، هش تیبل در زبان های برنامه نویسی مختلف اسم های مختلفی دارن. توی پایتون به اون دیکشنری میگیم.

برای ساخت یک هش تیبل در ردیس از دستور `hset(name,key,value)`استفاده می کنیم.

```python
import redis

r = redis.Redis(db=1)

# inserting with hset
r.hset("newHashTable", "key1", "value1")
r.hset("newHashTable", "key2", "value2")

print(r.hget("newHashTable", "key1"))
print(r.hgetall("newHashTable"))

# inserting with hmset
r.hmset("anotherHashTable", {"key-1": "value-1", "key-2": "value-2"}) # note that this function is deprecated
print(r.hgetall("anotherHashTable"))

```

فرض کنید یک دیکشنری پایتونی داریم و میخواییم تمامی اطلاعات اون رو وارد یک دیکشنری ردیسی کنیم. 

به این مثال توجه کنید:

```python
import redis
import random

random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
        }

r = redis.Redis(db=1)  # we choose db = 1 to work on a separate database than 1-simple-test.py

[r.hmset(h_id, hat) for h_id, hat in hats.items()]
```


ما در این کد، سه بار به سمت ردیس درخواست ارسال کردیم. برای اینکه این رفت و برگشت و ارسال چندین باره دستورات به سمت سرور ردیس صورت نگیره ردیس از مفهومی به نام `pip` یا خط لوله استفاده می کنه.

این مفهوم یعنی ما یک خط لوله رو آغاز می کنیم، هر اتفاقی که میخواییم توی ردیس بی افته رو توی این لوله کپسول بندی می کنیم و سپس کل لوله رو برای ردیس ارسال می کنیم. البته توجه داشته باشید که در این صورت امکان دسترسی به داده ها با استفاده از `get`و استفاده از آن در داخل لوله وجود ندارد.

<p style="text-align: right; direction: rtl">
برای ایجاد خط لوله در پایتون از دستور with r.pipeline() as pipe استفاده میشود.
</p>

```python
import redis
import random

random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
        }

r = redis.Redis(db=1)  # we choose db = 1 to work on a separate database than 1-simple-test.py

# bad practice
# [r.hmset(h_id, hat) for h_id, hat in hats.items()]


with r.pipeline() as pip:
    [pip.hmset(h_id, hat) for h_id, hat in hats.items()]  # note that hmset is deprecated
    pip.execute()
```


# Race condition

تصور کنید که من و شما میخواییم یک آیفون ۱۴ پرومکس ۲۵۶ گیگ بخریم. آقا تصور کن دیگه حالا مثلا ما پولداریم دیگه. به دلیل مشکلات تحریمی و قیمت بالا و ممنوعیت فروش دیجیکالا فقط یکی از این گوشی رو موجود داره. جفت ما وارد اکانتمون میشیم، این گوشی رو وارد کیفمون می کنیم. تا یکی از ما دوتا پرداخت رو انجام نده، دیجیکالا موجودی اون رو صفر نمی کنه. فرض کنید به طور هم زمان ما شروع به پرداخت می کنیم. پرداخت های ما همزمان انجام میشه. عملیات کم کردن تعداد گوشی بعد از پرداخت برای ما اجرا میشه. همزمان ما وارد این فانگشن شدیم، اول خرید من انجام میشه و میرم و موجودی این گوشی رو صفر می کنم، حالا نوبت شماست که برید و موجودی گوشی رو صفر کنید ولی قبلا صفر شده، اصلا نمیتونه برای شما این سفارش رو ثبت کنه. با اینکه شما پرداخت رو انجام دادید ولی واقعا گوشی ای نمونده که شما بخرید. به این حالت میگن ریس کاندیشن.

برای جلوگیری از ریس کاندیشن ها در مواقعی مثل همین خرید کالا،‌ ما از مفهومی استفاده می کنیم به نام atomicity. خلاصه این مفهوم یعنی یا همه یا هیچکس، به طور مثال، فرض کنید در مثال بالا خرید شما که به دلیل عدم موجودی کامل نشده، طبق این مفهوم باید برگشت بخوره و پول به حساب شما برگرده، این خرید که به لیست خرید های شما در دیتابیس اضافه شده باید بازگشت بخوره، امتیازی که از این خرید دریافت کردید باید بازگشت بخوره و و و. یعنی چون عملیات شما با خطا مواجه شده تمام تغییراتی که تا اون جای کد رخ داده باید رول بک (بازگشت) بخورن.

این مفهوم در جنگو رست فریمورک رفتار پیشفرض جنگو است، یعنی اگر دی حین کار روی یک ویو کلی تغییر ایجاد کرده باشید، کلی چیز توی دیتابیس ساخته باشید، اگر جایی از کد به خطا بخوره تمام تغییرات به قبل بازگشت میخورن.

برای اینکه یک ویوو رو اتمیک بکنیم به صورت زیر عمل می کنیم.

```python
from django.db import transaction

@transaction.atomic
def viewfunc(request):
    # This code executes inside a transaction.
    do_stuff()
```

برای مطالعه کامل این مفهوم در جنگو از این لینک استفاده کنید
https://docs.djangoproject.com/en/4.1/topics/db/transactions/

ردیس هم مانند هر دیتابیس دیگری با این ریس کاندیشن مواجه میشه که باید قابلیت اتمیک بودن رو برای اون داشته باشیم که داریم.

در ردیس برای نمایش اینکه یا همه یا هیچکدوم باید اجرا بشه از دستور multi و بعدش exec استفاده می کنیم.

```redis
127.0.0.1:6379> MULTI
127.0.0.1:6379> HINCRBY hashTableName quantity -1   # HINCRBY will increase a hashtable value for a specific field
127.0.0.1:6379> HINCRBY hashTableName npurchased 1  # like HINCRBY hashTableName field howMuchShouldIncrease
127.0.0.1:6379> EXEC
```

در دستور بالا اگر خطایی در یکی از دو خط به وجود بیاد، تغییر ایجاد شده روی آن یکی به حالت قبل بر میگرده.

در حالتی هم میتونیم به ردیس بگیم اگر در هنگام عملیاتی بودیم و برای اون فیلدی که ما نیاز داریم تغییری ایجاد شد، عملیات رو متوقف کن، همه تغییرات رو رول بک کن و عملیات رو از اول انجام بده.
این عملیات در ردیس با استفاده از مفهومی به نام فقل کردن خوش بینانه انجام میشه که برای اطلاعات بیشتر میتونید به این لینک مراجعه کنید:
https://en.wikipedia.org/wiki/Optimistic_concurrency_control

این رفتار در redis-py با استفاده از دستور watch() قابل پیاده سازیست.

به این مثال دقت کنید

```python
import logging
import redis

logging.basicConfig()


class OutOfStockError(Exception):
    """Raised when PyHats.com is all out of today's hottest hat"""


def buy_item(r: redis.Redis, itemid: str) -> None:
    with r.pipeline() as pipe:
        error_count = 0
        while True:
            try:
                # Get available inventory, watching for changes
                # related to this itemid before the transaction
                pipe.watch(itemid)
                number_left: bytes = r.hget(itemid, "quantity")
                if number_left > b"0":
                    pipe.multi()
                    pipe.hincrby(itemid, "quantity", -1)
                    pipe.hincrby(itemid, "npurchased", 1)
                    pipe.execute()
                    break
                else:
                    # Stop watching the itemid and raise to break out
                    pipe.unwatch()
                    raise OutOfStockError(
                        f"Sorry, {itemid} is out of stock!"
                    )
            except redis.WatchError:
                # Log total num. of errors by this user to buy this item,
                # then try the same process again of WATCH/HGET/MULTI/EXEC
                error_count += 1
                logging.warning(
                    "WatchError #%d: %s; retrying",
                    error_count, itemid
                )
    return None

```

# کاربردها

## کش کردن
یکی از کاربردهای مهم ردیس در کش کردن داده هاست. این کش کردن در اپلیکیشن های غیر جنگویی میتونه مانند همین ساختن هش تیبیل و ست و گت ساده صورت بگیره، اما در جنگو کار برای ما ساده تر شده.
برای استفاده از سیستم کشینگ ردیس لازمه ابتدا روی تنظیمات جنگومون این خطوط رو اضافه کنیم:

```python

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1", # this is gonna be diffrent based on using redis on docker or on system
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "example"  # this is a prefix will be used for assigning keys to redis
    }
}
```
و پکیج های زیر رو نصب کنیم:
```text
redis
django-redis
```

و حالا جنگو ما آماده استفاده از سیستم کشینگ ردیسه.

### کش کردن مقدار

در حالت هایی که خروجی ما وابستگی به پارامتر های ورودی کاربر دارد،‌ مثلا پارامتر های گت و یا پست که به سمت سرور ارسال می شود، میتونیم با استفاده از ترکیب این کلیدها با هم عباراتی رو تولید کنیم و اون هارو کش کنیم

به مثال زیر دقت کنید:

```python
from django.core.cache import cache
from rest_framework import viewsets
from .model import Country

class CountryView(viewsets.ViewSet):
    def get_country(self, request):
        language = request.GET.get("lang")
        countries = Country.objects.all()
        cached_result = cache.get(f"countries-{language}")
        if cached_result:
            return cached_result
        
        translated_countries = self.__translate_country_names(countries,language)
        cache.set(f"countries-{language}", translated_countries, timeout=60 * 60 * 24)
        return translated_countries


    @staticmethod
    def __translate_country_names(countries, language):
        pass  # do the translation logic here
```

اگر پارامتر های ورودی کاربر تاثیری در محاسبات ما نداره اما همچنان محاسبات ما سنگین و زمانبر هستند میتونیم از دستور دیگه ای برای کش کردن کل صفحه استفاده کنیم:

به مثال زیر دقت کنید:

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def my_view(request):
    ...
```

برای مطالعه تکمیلی به آدرس زیر مراجعه کنید:
https://docs.djangoproject.com/en/4.1/topics/cache/