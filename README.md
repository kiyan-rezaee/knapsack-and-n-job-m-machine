<style>
    html {
        background-color: rgb(18, 18, 35);
        color: rgb(255, 251, 244);
    }

    body {
        padding: 20px 50px;
    }

    li {
        font-size: 22px;
    }
    ol li{
        font-size: 18px;
        list-style-type:circle;
    }

    p {
        font-size: 20px;
        text-align:justify;
    }

    code {
        font-size: 20px;
    }
</style>

<body dir="rtl" lang="fa-IR">
    <h1 align="center"> تمرینات تحویلی درس طراحی و تحلیل الگوریتم ها</h1>
    <hr>
    <h2>اعضای گروه:</h2>
    <b>
        <ul>
            <li>کیان رضایی</li>
            <li>علی داداش زاده</li>
            <li>سید وحید عقیل زاده</li>
            <li>سینا پیمان</li>
        </ul>
    </b>
    <hr>
    <h2>مسئله کوله پشتی 0,1</h2>
    <ul>
    <li>مقدمه</li>
    <p>
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
    <li>مسئله کوله پشتی</li>
    <p>
        مسئله کوله پشتی 0,1 بدین شکل مطرح میشود: <br>
        یک دزد در هنگام دزدی از یک مفازه n شی پیدا میکند.
        i امین شی ، v<sub>i</sub>  دلار ارزش و w<sub>i</sub> پوند ظرفیت دارد، که v<sub>i</sub> و w<sub>i</sub> اعداد صحیح هستند.
        او میخواهد با ارزش ترین بار ممکن را بر دارد، اما بیشترین باری را که میتواند در کوله پشتی اش حمل کند، W پوند است که که مقداری صحیح است. چه اشیایی را باید بردارد؟
    </p>
    <li>حل مسئله کوله پشتی 0,1
    </li>
    <p>
        برای حل این مسئله هر بار کوله ای به ظرفیت w=0,...,W انتخاب میکنیم و سعی میکنیم با i شی اول  کوله را به طوری پر کنیم که بیشترین سود حاصل شود.
        همانطور که در بالا گفته شد، برای حل به روش برنامه نویسی پویا به یک ماتریس نیاز داریم تا مقدار حل شده هر زیر مسئله را در آن قرار دهیم. 
        ماتریسی به ابعاد n+1 سطر و W+1 ستون ایجاد میکنیم. که n تعداد اشیا و W ظرفیت کوله است.
        به عنوان مثال K[3][2]  نشان دهنده کوله ای به ظرفیت 2 و 3 نشان دهنده ماکسیمم سود از انتخاب شی اول تا سوم است.
    </p>
<br>
<p>
    ماتریسی به ابعاد n+1 و W+1 ستون می سازیم:
</p>

```python
K = [[0 for x in range(W + 1)] for x in range(n + 1)]
```

<hr>
<p>
    رابطه بازگشتی را به صورت زیر تعریف میکنیم: 
</p>

```python
if i == 0 or w == 0:
    K[i][w] = 0
elif wt[i - 1] <= w: 
    K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]) 
else:
    K[i][w]=K[i - 1][w] 
```

<p>
    شرط پایه: در صورتی که کوله پشتی به ظرفیت صفر داشته باشیم یا با صفر شی بخواهیم کوله را پر کنیم سود برابر صفر می شود.
</p>

```python
if i == 0 or w == 0:
    K[i][w] = 0
```

<hr>


<p>
    رویه بازگشتی: در صورتی که جرم شی i ام کمتر مساوی ظرفیت کوله باشد، مقدار K[i][w] را برابر با ماکسیمم (ارزش شی i ام به اضافه ماکسیمم سود کسب شده با i-1 شی و ظرفیت کوله منهای جرم شی i ام خواهد شد یا ماکسیمم سود کسب شده با i-1 شی و ظرفیت w).
    <br>
    در غیر این صورت K[i][w] برابر باماکسیمم سود کسب شده با i-1 شی و ظرفیت w خواهد شد.
</p>


```python
elif wt[i - 1] <= w: 
    K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]) 
else:
    K[i][w]=K[i - 1][w] 
```
<hr>
<h2>
پیاده سازی نهایی الگوریتم : 
</h2>

```python
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

توضیح ورودی های الگوریتم: <br>
<ol>
<li>
W : ظرفیت کوله پشتی
</li>
<li>
n : تعداد شی
</li>
<li>
wt : جرم هر شی
</li>
<li>
val : ارزش هر شی
</li>
</ol>
<br>

</body>