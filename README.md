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
```

وارد محیط cli (command line interface) ردیس شوید

برای تایید آن عبارت `ping` را وارد کنید و در صورتی که پاسخ `PONG` باشد، ردیس با موفقیت نصب شده است


# ردیس مانند دیکشنری پایتون

