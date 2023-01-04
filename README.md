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

برای راهنمای نصب داکر به این صفحه مراجعه کنید: [داکر در ویندوز](https://docs.docker.com/docker-for-windows/install/)

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
