<body dir="rtl" lang="fa-IR">
<h1 align="center"> تمرینات تحویلی درس طراحی و تحلیل الگوریتم ها</h1>
<h2>اعضای گروه:</h2>
<b>
    <ul>
        <li><font size = "5">کیان رضایی</font></li></font>
        <li><font size = "5">علی داداش زاده</font></li>
        <li><font size = "5">سید وحید عقیل زاده</font></li>
        <li><font size = "5">سینا پیمان</font></li>
    </ul>
</b>
<h2>مسئله کوله پشتی 0,1</h2>
<ul>
<li>
<font size = "5">مقدمه:
</font>
</li>
<font size = "4">
<p align='justify'>
        مسئله کوله پشتی 0,1 را میخواهیم به روش برنامه نویسی پویا حل کنیم. برنامه نویسی پویا یک روش قدرتمند حل مسئله به
        ویژه برای مسائل بهینه سازی میباشد. در برنامه نویسی پویا، ابتدا مسائل کوچک حل میشوند و در یک مکان ذخیره میشوند و
        سپس به تدریج به حل مسئله اصلی میرسیم. در این الگوریتم ها یک مسئله کوچک فقط یکبار محاسبه میشود.
        ابتدا به اجزایی که هر مسئله برنامه نویسی پویا احتیاج دارد، میپردازیم و سپس به کشف این اجزا در مسئله داده شده
        خواهیم پرداخت.<br>
        شباهت روش تقسیم و غلبه و برنامه نویسی پویا این است که هر دو نیاز به یک رابطه بازگشتی دارند و تفاوت آنها این است
        که روش تقسیم وغلبه مسئله را از بالا به پایین حل میکند، در صورتی که برنامه نویسی پویا آن را از پایین به بالا حل
        میکند.
        پس برای آنکه برنامه نویسی پویا بتواند مسائل را از پایین به بالا حل کند، نیاز به یک ماتریس (آرایه) دارد تا جواب
        زیر مسائل خود را داشته باشد.
        پس برای حل مسئله کوله پشتی 0,1 به روش برنامه نویسی پویا احتیاج به طرح یک فرمول بازگشتی و تعریف یک ماتریس داریم
        تا بعد از حل هر زیر مسئله مقدار آن را در ماتریس ذخیره کنیم.
</p>
</font>
<font size='5'><li>مسئله کوله پشتی:</li></font>
<font size='4'>
<p  align='justify'>
        مسئله کوله پشتی 0,1 بدین شکل مطرح میشود: <br>
        یک دزد در هنگام دزدی از یک مفازه n شی پیدا میکند.
        i امین شی ، v<sub>i</sub>  دلار ارزش و w<sub>i</sub> پوند ظرفیت دارد، که v<sub>i</sub> و w<sub>i</sub> اعداد صحیح هستند.
        او میخواهد با ارزش ترین بار ممکن را بر دارد، اما بیشترین باری را که میتواند در کوله پشتی اش حمل کند، W پوند است که که مقداری صحیح است. چه اشیایی را باید بردارد؟
</p>
</font>
<font size='5'><li>حل مسئله کوله پشتی 0,1:
</li>
</font>
<font size = "4">
<p align='justify'>
        برای حل این مسئله هر بار کوله ای به ظرفیت w=0,...,W انتخاب میکنیم و سعی میکنیم با i شی اول  کوله را به طوری پر کنیم که بیشترین سود حاصل شود.
        همانطور که در بالا گفته شد، برای حل به روش برنامه نویسی پویا به یک ماتریس نیاز داریم تا مقدار حل شده هر زیر مسئله را در آن قرار دهیم. 
        ماتریسی به ابعاد n+1 سطر و W+1 ستون ایجاد میکنیم. که n تعداد اشیا و W ظرفیت کوله است.
        به عنوان مثال K[3][2]  نشان دهنده کوله ای به ظرفیت 2 و 3 نشان دهنده ماکسیمم سود از انتخاب شی اول تا سوم است.
</p>
</font>
<br>
<font size = "4">
<p align='justify'>
    ماتریسی به ابعاد n+1 و W+1 ستون می سازیم:
</p>
</font>

<div alighn="left">

```python
K = [[0 for x in range(W + 1)] for x in range(n + 1)]
```

</div>

<hr>
<font size = "4">
    <p align='justify'>
    رابطه بازگشتی را به صورت زیر تعریف میکنیم: 
</p>
</font>
<div alighn="left">

```python
if i == 0 or w == 0:
    K[i][w] = 0
elif wt[i - 1] <= w:
    K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
else:
    K[i][w]=K[i - 1][w]
```

</div>

<font size = "4">
<p align='justify'>
    شرط پایه: در صورتی که کوله پشتی به ظرفیت صفر داشته باشیم یا با صفر شی بخواهیم کوله را پر کنیم سود برابر صفر می شود.
</p>
</font>
<div alighn="left">

```python
if i == 0 or w == 0:
    K[i][w] = 0
```

</div>
<hr>

<font size = "4">
    <p align='justify'>
    رویه بازگشتی: در صورتی که جرم شی i ام کمتر مساوی ظرفیت کوله باشد، مقدار K[i][w] را برابر با ماکسیمم (ارزش شی i ام به اضافه ماکسیمم سود کسب شده با i-1 شی و ظرفیت کوله منهای جرم شی i ام خواهد شد یا ماکسیمم سود کسب شده با i-1 شی و ظرفیت w).
    <br>
    در غیر این صورت K[i][w] برابر باماکسیمم سود کسب شده با i-1 شی و ظرفیت w خواهد شد.
</p>
    </font>
<div alighn="left">

```python
elif wt[i - 1] <= w:
    K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
else:
    K[i][w]=K[i - 1][w]
```

</div>
<hr>
<h3>
پیاده سازی نهایی الگوریتم: 
</h3>
<div alighn="left">

```python
def knapsack1():
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]
```

</div>
<font size = '5'>
توضیح ورودی های الگوریتم: 
</font>
<div align='right'>
<br>
<ul>
<li>
<font size = '4'>W : ظرفیت کوله پشتی
</font>
</li>
<li>
<font size='4'>
n : تعداد شی
</font>
</li>
<li>
<font size='4'>
wt : جرم هر شی
</font>
</li>
<li>
<font size='4'>
val : ارزش هر شی
</font>
</li>
</ul>
<br>
<font size = '5'>
مرتبه زمانی و حافظه مصرفی: 
</font>

<br>
<ul>
<li>
<font size = '4'>
مرتبه زمانی : O(nW)
</li>
<li>
مرتبه حافظه مصرفی : O(nW)
</font>
</li>
</li>
</ul>

<br>

<hr>
<h2>بهینه کردن الگوریتم ارائه شده: </h2>
<font size='4'>
<p align='justify'>
همانطور که در بالا دیدیم مرتبه زمان اجرا و مرتبه حافظه مصرفی O(nW) میباشد. اما در رویکرد جدید سعی میکنیم که 
مرتبه حافظه مصرفی را کاهش دهیم. در الگوریتم بالا برای هر  شی یک سطر در نظر میگرفتیم و برای محاسبه سطر های بعد از سطر بالایی آن استفاده میکردیم، برای بهینه سازی میتوانیم فقط سطر آخر را ‌ذخیره کنیم و سطر جدید را روی همان سطر بازنویسی کنیم. در انتها Kp برابر با K[n] در الگوریتم قبل میشود و در این روش از n-1 سطر کمتر استفاده میشود که میزان حافظه استفاده شده برابر یک ماتریس با ابعاد 1 در w استفاده میشود. 
</p>
</font>

<hr>
<h3>
پیاده سازی نهایی الگوریتم: 
</h3>
<div align='left'>

```python
def knapsack2(W, wt, val, n):
    Kp = [0 for i in range(W + 1)]

    for i in range(1, n + 1):
        for w in range(W, 0, -1):
            if wt[i - 1] <= w:
                Kp[w] = max(K[w], Kp[w - wt[i - 1]] + val[i - 1])
            else:
                break
    return Kp[W]
```

</div>


<font size = '5'>
مرتبه زمانی و حافظه مصرفی: 
</font>

<br>
<ul>
<li>
<font size = '4'>
مرتبه زمانی : O(nW)
</li>
<li>
مرتبه حافظه مصرفی : O(W)
</font>
</li>
</li>
</ul>

<hr>

</font>
<font size='5'>حل مسئله n کار بر روی m ماشین :
<br>
<ul>
<li>
صورت مسئله : 
</li>
<font size='4'>
-فرض کنید مجموعه ای از n کار را در اختیار داشته باشیم. هر کار i زمان اجرای p<sub>i</sub> را دارد. می خواهیم این کارها را بر روی
m ماشین اجرا کنیم به گونه ای که مجموع زمان اتمام کارها مینیمم شود. به عبارت دیگر تابع هدف به صورت زیر است :

اینجا اون فرموله بیاد....
که در آن c<sub>i</sub>
 زمان اتمام کار i است. همه کارها در لحظه شروع در دسترس هستند و هر ماشین در هر لحظه بیش از یک کار نمی
تواند انجام دهد.
</font>
</p>
<li>
حل مسئله به روش حریصانه : 
</li>
<p>
<font size='4'>
یک الگوریتم حریصانه، همانطور که از اسم آن مشخص است، حریص است و همیشه انتخابی که در آن لحظه بهترین به نظر می‌رسد را بر می‌گزیند. به این معنی که انتخاب را به گونه ای انجام می دهد که به صورت محلی و در همان موقعیت بهینه باشد، به امید آن که این انتخاب باعث شود جواب نهایی هم بهینه شود.
تصور کنید که شما یک تابع هدف (objective function) دارید که لازم است مقدار نهایی آن در نقطه ای بهینه شود (بیشینه یا کمینه). یک الگوریتم حریصانه در هر مرحله یک انتخاب طمع کارانه انجام می دهد تا مطمئن شود تابع هدف بهینه شده است. الگوریتم حریصانه برای به دست آوردن مقدار بهینه فقط یک شانس دارد چرا که نمی تواند به عقب برگردد و انتخاب های قبلی را تغییر دهد. پس در طراحی الگوریتم با تکنیک حریصانه، پس از مشخص و تعریف شدن تابع هدف، در هر مرحله باید سعی کرد بیشتر/کمترین مقدار را برای تابع به دست آورد.
ابتدا ایده حل مسئله داده شده را مطرح میکنیم و روی یک مثال توضیح میدهیم که چرا رویکرد ما حریصانه است.
ایده الگوریتم به شرح زیر است :
ابتدا n کار را برحسب p<sub>i</sub>ها به صورت صعودی در یک لیست مرتب میکنیم و از کوچکترین عضو لیست ایجاد شده شروع به تخصیص کار به تک تک ماشین ها میکنیم. یعنی m کار اول به m ماشین تخصیص داده میشود و کار m+1 مجدد به ماشین اول تخصیص داده میشود.
<br>
</font>
<li>
چرا الگوریتم معرفی شده حریصانه است؟
</li>
<font size='4'>
با یک مثال سعی میکنیم نشان دهیم که چرا رویکرد معرفی شده حریصانه است. فرض کنید n=5 کار و m=3 ماشین داریم. 
<br>

| i  | a | b | c | d | e
|----|---|---|---|---|---|
| p<sub>i</sub> | 1 | 2 | 3 | 4 | 5

<hr>
در گام اول تمامی هیچ کاری به ماشینی اختصاص نیافته است. با ماشین اول شروع میکنیم. میخواهیم کاری را انتخاب کنیم که در همین مرحله جواب مورد نظر ما باشد یعنی مجموع c<sub>i</sub> آن مینیمم باشد. از کارها بدیهی است که باید کار a را به ماشین اول اختصاص دهیم. زیرا c<sub>i</sub>=1 خواهد بود و در صورتی که کار دیگری انتخاب میکردیم این مقدار بیشتر میشد.
حال در مرحله بعدی برای ماشین دوم میخواهیم کاری را انتخاب کنیم که در همین مرحله کمترین مقدار c<sub>i</sub> را داشته باشد. پس کار b را به ماشین دوم میدهیم. این رویکرد نشان میدهد که ما در هر مرحله بهینه ترین جواب ممکن را صرف نظر از جواب نهایی در نظر میگیریم که همان رویکرد حریصانه است.
حال فرض کنید سه کار اول به سه ماشین اختصاص یافته است. در تخصیص کار بعدی به ماشین اول دو حالت ممکن را بررسی میکنیم : 
اگر کار d را به ماشین اول بدهیم، مجموع c<sub>i</sub> ها در این ماشین برابر 1+5=6 خواهد بود. در صورتی که اگر کار e را به ماشین اول تخصیص میدادیم این مقدار برابر 1+6=7 می بود که با رویکرد حریصانه در تضاد است. پس الگوریتم به این صورت است که کار هارا ابتدا بر حسب p<sub>i</sub> ها به صورت صعودی مرتب میکنیم و به ترتیب از ابتدا کار ها به ماشین ها میدهیم.
</p>
</font>

<hr>
<h3>
پیاده سازی نهایی الگوریتم: 
</h3>
<div align='left'>

```python
def knapsack2(W, wt, val, n):
    Kp = [0 for i in range(W + 1)]

    for i in range(1, n + 1):
        for w in range(W, 0, -1):
            if wt[i - 1] <= w:
                Kp[w] = max(K[w], Kp[w - wt[i - 1]] + val[i - 1])
            else:
                break
    return Kp[W]
```

</div>
</body>
