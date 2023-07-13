# SE-LAB-1






##پرسش‌ها
1-پوشه‌ی .git چیست؟ چه اطلاعاتی در آن ذخیره می‌شود؟ با چه دستوری ساخته می‌شود؟
پاسخ:
 پوشه gitشامل تمام اطلاعات لازم برای مدیریت و ذخیره تاریخچه‌ی تغییرات پروژه است.دران اطبلاعاتی چون commit ها وکامنت های متناظر با ان همچنین branchوtag ها و نام و ایمیل نوسینده همچنین زمان تغیر در ان ذخیره میشود.
 دستور ساخت ان هم git init است

2-منظور از atomic بودن در atomic commit و atomic pull-request چیست؟
3-تفاوت دستورهای fetch و pull و merge و rebase را بیان کنید.
4-تفاوت چهار دستور reset و revert و restore را بیان کنید.
5-منظور از stage چیست؟ دستور stash چه کاری را انجام می‌دهد؟
پاسخ:
به معنای اضافه کردن تغییرات فایل‌های ویرایش شده به index است .که با دستور git add میتوانیم تغیرات فایل را به stage اضافه کنیم وبعدا ان را commit  کنیم.
تغییرهایی را که در نسخه ی کاریایجاد کردیم را به طور موقت ذخیره می کند تا بتوانیم روی ویژگی دیگری کار کنیم. سپس در آینده هر موقع لازم شد، برگردیم و دوباره  ان ها را اعمال کنیم.git stash
6-مفهوم snapshot به چه معناست؟
پاسخ: مفهوم snapshot در یک پروژه گرفتن یک تصویر از وضعیت کلی پروژه در یک زمان خاص است.به طوری که به دایرکتوری ها فایل ها و تاریخچه فایل ها دسترسی داشته باشیم همچنین در git به عنوان یک commit ثبت میشود.
