# SE-LAB-1

## Team members
* Alireza Ziaee
* ?

## مراحل ساخت این مخزن

1- ابتدا یک مخزن Git جدید را با استفاده از دستور `git init` در ماشین محلی خود ایجاد کردیم

2- یک مخزن جدید در GitHub ایجاد کردیم و مخزن محلی خود را به این مخزن remote متصل کردیم و فایل `REAME.md` را به این مخزن remote ارسال کردیم

3- فایل `.gitignore` را ایجاد کرده و فایل‌هایی را که نمی‌خواستیم به مخزن github ارسال‌ کنیم را در آن قرار دادیم. برای ایم کار از [gitignore.io](https://www.toptal.com/developers/gitignore) استفاده کردیم



## پرسش‌ها

### 1-پوشه‌ی .git چیست؟ چه اطلاعاتی در آن ذخیره می‌شود؟ با چه دستوری ساخته می‌شود؟

 ‌پوشه‌ی `git.‍‍` شامل تمام اطلاعات لازم برای مدیریت و ذخیره تاریخچه‌ی تغییرات پروژه است.در آن اطلاعاتی چون commit ها و کامنت‌های متناظر با ان همچنین branch و tag ها و نام و ایمیل نویسنده همچنین زمان تغیر در ان ذخیره می‌شود.
 دستور ساخت ان هم `git init` است.
 

### 2-منظور از atomic بودن در atomic commit و atomic pull-request چیست؟

منظور از atomic بودن کامیت این است که در هر کامیت تنها یک کار مجزا باید انجام شود. همچنین commit های مربوط به bugfix یا refactoring یا features باید از یکدگیر جدا شوند. باید از کامیت کردن تغییرات متعدد به صورت یکجا پرهیز گردد و هر کامیت باید تنها یک گام ما را به حالت مورد انتظار نزدیک کند. با توجه به اینکه هر کامیت ‌به‌معنی یک snapshot از پروژه می‌باشد؛ باید کد را در یک موقعیت valid نگه دارد. Atomic pull request بدین معنی است که حتی الامکان باید pull requestها به کارهای کوچکتر شکسته شوند و review کردن آن‌ها نباید چندین ساعت طول بکشد و به جای یک تسک بزرگ، کارها به تعداد بیشتری task یا issueی کوچک شکسته شوند که هر یک در یک PR قابل انجام باشند.


### 3-تفاوت دستورهای fetch و pull و merge و rebase را بیان کنید.

دستور `fetch` صرفا اطلاعات موجود در مخزن را نسبت به یکی از مخازن remote به‌روز می‌کند. یعنی اشیاء و branch های پروژه را از یک مخزن remote دریافت کرده و در پوشه `.git` ذخیره می‌کند. اما دستور `pull` هم تغییرات را از مخازن remote می‌گیرد، هم آن‌ها را با نسخه‌ی کنونی ادغام می‌کند. عملیات `merge` نیز یکی از راه‌های ادغام دو نسخه است بدین صورت که فایل‌های تغییر یافته در یک نسخه که در نسخه‌ی دیگر تغییر پیدا نکرده‌اند در نسخه‌ی نهایی تغییر می‌کنند و قسمت‌هایی که در هر دو نسخه تغییر کرده‌اند دچار تعارض (conflict) می‌شوند و که این conflict ها باید برطرف شوند و کد اصلاح‌شده حاصل از رفع conflict ها جایگزین شود.

### 4-تفاوت چهار دستور `reset` و `revert` و `restore` و `rebase` را بیان کنید.

#### دستور `reset`

دستور `git reset` برای بازگرداندن فایل‌ها به حالت قبل استفاده می‌شود. مثلا فایل‌هایی که با دستور `git add` به استیج رفته‌اند، با استفاده از `git reset` از استیج خارج می‌شوند.

#### دستور `revert`

دستور `git revert` یک عملیات خنثی‌سازی رو به جلو است که روشی امن برای لغو تغییرات ارائه می‌دهد. به جای حذف  commit ها در تاریخچه commit، یک revert یک commit جدید ایجاد می‌کند که تغییرات مشخص شده را معکوس می‌کند.

#### دستور `restore`

دستور `git restore` برای بازیابی تغییرات فایل‌ها به وضعیت قبلی استفاده می‌شود. با این دستور، می‌توان فایل‌هایی را که تغییر کرده‌اند، به وضعیت قبلی بازگرداند و تغییرات آن‌ها را برطرف کرد.

#### دستور `rebase`

دستور `git rebase` برای تغییر تاریخچه کامیت‌ها و merge استفاده می‌شود. با این دستور می‌توان تاریخچه کامیت‌های بر روی یک برنچ را به روز کرد و با برنچ دیگری ادغام کرد. در واقع اتفاقی که می‌افتد این است که کامیت‌های یک برنچ به برنچ دیگه می‌روند و تاریخچه‌ی کامیت‌های برنچ تغییر می‌کند.

### 5-منظور از stage چیست؟ دستور stash چه کاری را انجام می‌دهد؟

به معنای اضافه کردن تغییرات فایل‌های ویرایش شده به index است .که با دستور `git add` میتوانیم تغیرات فایل را به stage اضافه کنیم وبعدا ان را commit کنیم.

دستور `git stash` تغییراتی را که در نسخه‌ی فعلی ایجاد کردیم را به طور موقت ذخیره می‌کند تا بتوانیم روی ویژگی دیگری کار کنیم. سپس در آینده هر موقع لازم شد، برگردیم و دوباره آن‌ها را اعمال کنیم.

### 6-مفهوم snapshot به چه معناست؟

مفهوم snapshot در یک پروژه گرفتن یک تصویر از وضعیت کلی پروژه در یک زمان خاص است.به طوری که به دایرکتوری‌ها، فایل‌ها و تاریخچه فایل‌ها دسترسی داشته‌باشیم. همچنین در git به عنوان یک commit ثبت می‌شود‌.
