#!/usr/bin/env python3
# Сборка сайта Elefund: python3 _build.py
# Тексты — в TEXTS ниже (ru / en / kk). Файлы с «_» в начале GitHub Pages не публикует.
import html
import os

EMAIL = 'elefund.app@gmail.com'
UPDATED = {'ru': '13 ноября 2026', 'en': 'November 13, 2026', 'kk': '2026 жылғы 13 қараша'}
LANGS = ['ru', 'en', 'kk']
LANG_LABEL = {'ru': 'Рус', 'en': 'Eng', 'kk': 'Қаз'}

ICONS = {
    'qr': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><path d="M14 14h3v3M21 14v.01M17 21h4v-4M14 21v-3"/></svg>',
    'doc': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/></svg>',
    'lock': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
}

T = {
    'ru': {
        'title': 'Elefund — учёт денег, который сходится',
        'desc': 'Учёт личных финансов для iPhone: QR-чеки, выписки Kaspi и Halyk, бюджет и цели. Данные хранятся только на телефоне.',
        'h1': 'Деньги сходятся до тенге',
        'lead': 'Elefund — учёт личных финансов для iPhone. Чеки по QR, выписки Kaspi и Halyk, бюджет и цели. Всё хранится только на вашем телефоне.',
        'badge': 'Скоро в App Store',
        'badge_small': 'для iPhone',
        'note': 'Основное — бесплатно. Pro — по подписке или один раз навсегда.',
        'features': [
            ('qr', 'Чек → статьи за секунду', 'Отсканируйте QR на чеке — покупки сами разложатся по статьям: продукты отдельно, бытовая химия отдельно.'),
            ('doc', 'Выписка вместо ручного ввода', 'Загрузите PDF-выписку Kaspi Gold или Halyk — операции внесутся сами, а то, что уже записано, не задвоится.'),
            ('lock', 'Ваши данные — только ваши', 'Без регистрации, без наших серверов, без рекламы. База лежит на телефоне, копии можно зашифровать паролем.'),
        ],
        'also_h': 'А ещё',
        'also': [
            'Быстрый ввод одной строкой',
            'Бюджет по статьям и движение денег по месяцам',
            'Цели и конверты для накоплений',
            'Кредиты и долги',
            'Советник: пошаговый план — подушка, долги, накопления',
            'Несколько валют и курсы Нацбанка',
            'Тёмная тема, Face ID, русский, казахский и английский',
        ],
        'why_h': 'Почему слон',
        'why': 'Слоны ничего не забывают. Elefund тоже: каждая трата на своём месте, и в конце месяца остаток в приложении совпадает с банком. Приложение сделано в Алматы человеком, который почти 20 лет занимается финансовыми системами, — сначала для себя.',
        'nav_privacy': 'Конфиденциальность',
        'nav_support': 'Поддержка',
        'nav_home': 'Главная',
        'made': 'Сделано в Алматы',
        'privacy_title': 'Политика конфиденциальности',
        'updated': 'Обновлено',
        'privacy': [
            ('', '<p class="hi"><b>Коротко:</b> Elefund не собирает ваши данные. Нет регистрации, нет наших серверов, нет рекламы и аналитики. Всё, что вы вносите, хранится только на вашем устройстве.</p>'),
            ('Какие данные хранит приложение', '<p>Счета, операции, статьи, бюджеты, цели, чеки и настройки хранятся в базе данных внутри приложения на вашем iPhone. Разработчик не имеет к ним доступа.</p>'),
            ('Когда приложение выходит в интернет', '<ul>'
                '<li><b>Курсы валют.</b> Приложение загружает официальные курсы с сайта Национального банка Казахстана (nationalbank.kz). Ваши данные при этом не передаются.</li>'
                '<li><b>Чеки по QR.</b> Когда вы сканируете чек, его реквизиты из QR-кода (номер кассы, номер чека, дата, сумма) отправляются оператору фискальных данных, выдавшему чек, чтобы получить список покупок. Больше ничего не передаётся.</li>'
                '<li><b>PDF-выписки.</b> Выписки разбираются прямо на телефоне и никуда не отправляются.</li>'
                '<li><b>Покупки.</b> Оплату Pro обрабатывает Apple. Для проверки подписки используется сервис RevenueCat: он получает анонимный идентификатор покупки и сведения о ней от Apple, но не ваши финансовые данные, имя или почту.</li>'
                '</ul>'),
            ('Резервные копии', '<p>Копии создаются по вашей команде и автоматически — в папке приложения на телефоне. Файл копии вы можете сохранить куда угодно через меню «Поделиться». Если задан пароль, копия шифруется (AES-256), а пароль хранится в защищённом хранилище iOS (Keychain). Без пароля зашифрованную копию открыть нельзя — в том числе разработчику.</p>'),
            ('Разрешения', '<ul>'
                '<li><b>Камера</b> — только чтобы сканировать QR-код чека. Снимки не сохраняются.</li>'
                '<li><b>Face ID</b> — для блокировки приложения. Проверку выполняет iOS; приложение не получает биометрические данные.</li>'
                '<li><b>Уведомления</b> — для напоминаний, которые вы сами включили. Они создаются на телефоне.</li>'
                '<li><b>Файлы и фото</b> — только те, что вы сами выбрали: выписка, копия, скриншот для письма разработчику.</li>'
                '</ul>'),
            ('Письма разработчику', '<p>«Написать разработчику» открывает стандартное меню «Поделиться»: вы сами выбираете, куда и что отправить. К тексту добавляется служебная строка — версия приложения, версия iOS, модель телефона и язык, — чтобы было проще разобраться в проблеме.</p>'),
            ('Удаление данных', '<p>Удалите приложение — и все его данные будут удалены с телефона. Также можно стереть данные в настройках приложения. Копии, которые вы сохранили сами, остаются там, куда вы их сохранили.</p>'),
            ('Дети', '<p>Приложение не предназначено для детей младше 13 лет и не собирает данные о них.</p>'),
            ('Изменения', '<p>Если политика изменится, новая версия появится на этой странице с новой датой.</p>'),
            ('Связь', f'<p>Вопросы о конфиденциальности: <a href="mailto:{EMAIL}">{EMAIL}</a></p>'),
        ],
        'support_title': 'Поддержка',
        'support_lead': 'Ответы на частые вопросы. Не нашли свой — напишите, ответим.',
        'faq': [
            ('Где хранятся мои данные?', '<p>Только на вашем iPhone, внутри приложения. Ни регистрации, ни облака разработчика нет — поэтому важно делать резервные копии.</p>'),
            ('Как перенести данные на новый телефон?', '<ol><li>На старом телефоне: «Ещё» → «Резервная копия» → «Сохранить копию» и отправьте файл себе (AirDrop, Файлы, мессенджер).</li><li>На новом: установите Elefund, откройте «Ещё» → «Резервная копия» → «Восстановить из файла» и выберите копию.</li></ol>'),
            ('Я забыл пароль от копии', '<p>К сожалению, открыть зашифрованную копию без пароля невозможно — ни вам, ни нам. Так работает шифрование. Если приложение ещё стоит на телефоне, данные в нём на месте: снимите или смените пароль в разделе «Резервная копия» и сохраните новую копию.</p>'),
            ('Какие выписки можно загрузить?', '<p>Сейчас — PDF-выписки Kaspi Gold и Halyk Bank (в том числе валютные). Другие банки добавляем по мере поступления примеров — напишите, какой нужен вам.</p>'),
            ('Какие чеки читаются по QR?', '<p>Фискальные чеки Казахстана с QR-кодом, которые можно проверить на сайте оператора фискальных данных. Если чек не читается — пришлите нам ссылку из его QR-кода.</p>'),
            ('Что входит в Pro?', '<p>Загрузка выписок, QR-чеки, бюджет по статьям и движение денег, советник, проекты и контрагенты, цели и конверты без ограничений, копии с паролем. Счета, операции, журнал, отчёты, кредиты и копии — бесплатно навсегда.</p>'),
            ('Как восстановить покупку?', '<p>«Ещё» → «Elefund Pro» → «Восстановить покупки». Используйте тот же Apple ID, с которого покупали.</p>'),
            ('Как отменить подписку?', '<p>Настройки iPhone → ваше имя → «Подписки» → Elefund → «Отменить подписку». Pro продолжит работать до конца оплаченного периода, а все ваши данные останутся на месте.</p>'),
        ],
        'contact_h': 'Написать нам',
        'contact': f'Почта: <a href="mailto:{EMAIL}">{EMAIL}</a>. Или прямо из приложения: «Ещё» → «Написать разработчику» — так к письму сразу добавится версия приложения и модель телефона.',
    },
    'en': {
        'title': 'Elefund — money tracking that adds up',
        'desc': 'Personal finance for iPhone: QR receipts, Kaspi and Halyk statements, budgets and goals. Your data stays on your phone.',
        'h1': 'Every tenge accounted for',
        'lead': 'Elefund is a personal finance app for iPhone. QR receipts, Kaspi and Halyk statements, budgets and goals. Everything stays on your phone.',
        'badge': 'Coming to the App Store',
        'badge_small': 'for iPhone',
        'note': 'The basics are free. Pro is a subscription or a one-time purchase.',
        'features': [
            ('qr', 'Receipt to categories in a second', 'Scan the QR code on a receipt — purchases sort into categories on their own: groceries here, household goods there.'),
            ('doc', 'Statements instead of typing', 'Upload a Kaspi Gold or Halyk PDF statement — transactions add themselves, and nothing you already entered gets doubled.'),
            ('lock', 'Your data is yours', 'No sign-up, no servers of ours, no ads. The database lives on your phone, and backups can be password-encrypted.'),
        ],
        'also_h': 'Also',
        'also': [
            'Quick entry in a single line',
            'Category budgets and monthly cash flow',
            'Goals and envelopes for savings',
            'Loans and debts',
            'Advisor: a step-by-step plan — safety net, debts, savings',
            'Multiple currencies with National Bank rates',
            'Dark theme, Face ID, English, Russian and Kazakh',
        ],
        'why_h': 'Why an elephant',
        'why': 'Elephants never forget. Neither does Elefund: every expense in its place, and at the end of the month your balance matches the bank. Made in Almaty by someone who has spent almost 20 years building financial systems — first for himself.',
        'nav_privacy': 'Privacy',
        'nav_support': 'Support',
        'nav_home': 'Home',
        'made': 'Made in Almaty',
        'privacy_title': 'Privacy Policy',
        'updated': 'Updated',
        'privacy': [
            ('', '<p class="hi"><b>In short:</b> Elefund does not collect your data. No sign-up, no servers of ours, no ads, no analytics. Everything you enter stays on your device.</p>'),
            ('What the app stores', '<p>Accounts, transactions, categories, budgets, goals, receipts and settings are stored in a database inside the app on your iPhone. The developer has no access to them.</p>'),
            ('When the app goes online', '<ul>'
                '<li><b>Exchange rates.</b> The app downloads official rates from the National Bank of Kazakhstan (nationalbank.kz). None of your data is sent.</li>'
                '<li><b>QR receipts.</b> When you scan a receipt, the details from its QR code (cash register number, receipt number, date, amount) are sent to the fiscal data operator that issued it, to get the list of purchases. Nothing else is sent.</li>'
                '<li><b>PDF statements.</b> Statements are processed right on the phone and never sent anywhere.</li>'
                '<li><b>Purchases.</b> Pro payments are processed by Apple. Subscription status is checked with RevenueCat, which receives an anonymous purchase ID and purchase details from Apple — not your financial data, name or email.</li>'
                '</ul>'),
            ('Backups', '<p>Backups are created on request and automatically, in the app folder on your phone. You can save a backup file anywhere via the Share menu. If you set a password, the backup is encrypted (AES-256) and the password is kept in the iOS Keychain. An encrypted backup cannot be opened without the password — including by the developer.</p>'),
            ('Permissions', '<ul>'
                '<li><b>Camera</b> — only to scan receipt QR codes. Images are not saved.</li>'
                '<li><b>Face ID</b> — to lock the app. iOS performs the check; the app never receives biometric data.</li>'
                '<li><b>Notifications</b> — for reminders you turn on. They are scheduled on the phone.</li>'
                '<li><b>Files and photos</b> — only the ones you pick: a statement, a backup, a screenshot for a message to the developer.</li>'
                '</ul>'),
            ('Messages to the developer', '<p>“Contact the developer” opens the standard Share menu: you choose where and what to send. A technical line is added to your text — app version, iOS version, phone model and language — to make problems easier to solve.</p>'),
            ('Deleting data', '<p>Delete the app and all its data is removed from the phone. You can also erase data in the app settings. Backups you saved yourself stay wherever you saved them.</p>'),
            ('Children', '<p>The app is not intended for children under 13 and does not collect data about them.</p>'),
            ('Changes', '<p>If this policy changes, the new version will appear on this page with a new date.</p>'),
            ('Contact', f'<p>Privacy questions: <a href="mailto:{EMAIL}">{EMAIL}</a></p>'),
        ],
        'support_title': 'Support',
        'support_lead': 'Answers to common questions. Didn’t find yours? Write to us.',
        'faq': [
            ('Where is my data stored?', '<p>Only on your iPhone, inside the app. There is no sign-up and no developer cloud — which is why backups matter.</p>'),
            ('How do I move my data to a new phone?', '<ol><li>On the old phone: More → Backup → Save copy and send the file to yourself (AirDrop, Files, a messenger).</li><li>On the new one: install Elefund, open More → Backup → Restore from file and pick the backup.</li></ol>'),
            ('I forgot my backup password', '<p>Unfortunately, an encrypted backup cannot be opened without its password — not by you, not by us. That is how encryption works. If the app is still on your phone, your data is intact: remove or change the password in Backup and save a new backup.</p>'),
            ('Which statements can I upload?', '<p>Currently Kaspi Gold and Halyk Bank PDF statements (including foreign-currency ones). We add other banks as we get samples — tell us which one you need.</p>'),
            ('Which QR receipts work?', '<p>Kazakhstan fiscal receipts with a QR code that can be checked on the fiscal data operator’s website. If a receipt doesn’t work, send us the link from its QR code.</p>'),
            ('What’s in Pro?', '<p>Statement uploads, QR receipts, category budgets and cash flow, the advisor, projects and counterparties, unlimited goals and envelopes, password-protected backups. Accounts, transactions, the journal, reports, loans and backups are free forever.</p>'),
            ('How do I restore a purchase?', '<p>More → Elefund Pro → Restore purchases. Use the same Apple ID you bought with.</p>'),
            ('How do I cancel my subscription?', '<p>iPhone Settings → your name → Subscriptions → Elefund → Cancel Subscription. Pro keeps working until the end of the paid period, and all your data stays in place.</p>'),
        ],
        'contact_h': 'Contact us',
        'contact': f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a>. Or right from the app: More → Contact the developer — the app version and phone model are added automatically.',
    },
    'kk': {
        'title': 'Elefund — ақша есебі, ол дәл келеді',
        'desc': 'iPhone-ға арналған жеке қаржы есебі: QR-чектер, Kaspi және Halyk үзінділері, бюджет пен мақсаттар. Деректер тек телефонда сақталады.',
        'h1': 'Ақша теңгесіне дейін дәл',
        'lead': 'Elefund — iPhone-ға арналған жеке қаржы есебі. QR-чектер, Kaspi және Halyk үзінділері, бюджет пен мақсаттар. Барлығы тек сіздің телефоныңызда сақталады.',
        'badge': 'Жақында App Store-да',
        'badge_small': 'iPhone үшін',
        'note': 'Негізгісі — тегін. Pro — жазылыммен немесе бір рет мәңгіге.',
        'features': [
            ('qr', 'Чек → санаттар бір секундта', 'Чектегі QR-кодты сканерлеңіз — сатып алулар санаттарға өздері бөлінеді: азық-түлік бөлек, тұрмыстық химия бөлек.'),
            ('doc', 'Қолмен енгізудің орнына үзінді', 'Kaspi Gold немесе Halyk PDF-үзіндісін жүктеңіз — операциялар өздері енгізіледі, бұрын жазылғандары қайталанбайды.'),
            ('lock', 'Деректеріңіз — тек сіздікі', 'Тіркеусіз, біздің серверлерсіз, жарнамасыз. База телефонда, көшірмелерді құпиясөзбен шифрлауға болады.'),
        ],
        'also_h': 'Тағы',
        'also': [
            'Бір жолмен жылдам енгізу',
            'Санаттар бойынша бюджет және айлық ақша қозғалысы',
            'Жинаққа арналған мақсаттар мен конверттер',
            'Несиелер мен қарыздар',
            'Кеңесші: қадамдық жоспар — қор, қарыздар, жинақ',
            'Бірнеше валюта және Ұлттық банк бағамдары',
            'Қараңғы тақырып, Face ID, қазақ, орыс және ағылшын тілдері',
        ],
        'why_h': 'Неге піл',
        'why': 'Пілдер ештеңені ұмытпайды. Elefund та: әр шығын өз орнында, ай соңында қосымшадағы қалдық банкпен сәйкес келеді. Қосымшаны Алматыда қаржы жүйелерімен 20 жылға жуық айналысқан адам жасады — алдымен өзі үшін.',
        'nav_privacy': 'Құпиялылық',
        'nav_support': 'Қолдау',
        'nav_home': 'Басты бет',
        'made': 'Алматыда жасалған',
        'privacy_title': 'Құпиялылық саясаты',
        'updated': 'Жаңартылды',
        'privacy': [
            ('', '<p class="hi"><b>Қысқаша:</b> Elefund деректеріңізді жинамайды. Тіркеу жоқ, біздің серверлер жоқ, жарнама мен аналитика жоқ. Енгізгеніңіздің бәрі тек құрылғыңызда сақталады.</p>'),
            ('Қосымша қандай деректерді сақтайды', '<p>Шоттар, операциялар, баптар, бюджеттер, мақсаттар, чектер мен баптаулар iPhone-дағы қосымшаның ішіндегі дерекқорда сақталады. Әзірлеушінің оларға қолжетімділігі жоқ.</p>'),
            ('Қосымша қашан интернетке шығады', '<ul>'
                '<li><b>Валюта бағамдары.</b> Қосымша ресми бағамдарды Қазақстан Ұлттық банкінің сайтынан (nationalbank.kz) жүктейді. Сіздің деректеріңіз жіберілмейді.</li>'
                '<li><b>QR-чектер.</b> Чекті сканерлегенде QR-кодтағы деректемелер (касса нөмірі, чек нөмірі, күні, сомасы) сатып алулар тізімін алу үшін чекті берген фискалдық деректер операторына жіберіледі. Басқа ештеңе жіберілмейді.</li>'
                '<li><b>PDF-үзінділер.</b> Үзінділер телефонның өзінде өңделеді және ешқайда жіберілмейді.</li>'
                '<li><b>Сатып алулар.</b> Pro төлемін Apple өңдейді. Жазылымды тексеру үшін RevenueCat қызметі қолданылады: ол Apple-дан сатып алудың анонимді идентификаторы мен мәліметтерін алады, бірақ қаржы деректеріңізді, атыңызды немесе поштаңызды алмайды.</li>'
                '</ul>'),
            ('Сақтық көшірмелер', '<p>Көшірмелер сіздің пәрменіңізбен және автоматты түрде телефондағы қосымша қалтасында жасалады. Көшірме файлын «Бөлісу» мәзірі арқылы кез келген жерге сақтай аласыз. Құпиясөз орнатылса, көшірме шифрланады (AES-256), ал құпиясөз iOS қорғалған қоймасында (Keychain) сақталады. Шифрланған көшірмені құпиясөзсіз ешкім аша алмайды — әзірлеуші де.</p>'),
            ('Рұқсаттар', '<ul>'
                '<li><b>Камера</b> — тек чектің QR-кодын сканерлеу үшін. Суреттер сақталмайды.</li>'
                '<li><b>Face ID</b> — қосымшаны бұғаттау үшін. Тексеруді iOS жүргізеді; қосымша биометриялық деректерді алмайды.</li>'
                '<li><b>Хабарландырулар</b> — өзіңіз қосқан еске салғыштар үшін. Олар телефонда жасалады.</li>'
                '<li><b>Файлдар мен фотолар</b> — тек өзіңіз таңдағандары: үзінді, көшірме, әзірлеушіге хатқа скриншот.</li>'
                '</ul>'),
            ('Әзірлеушіге хат', '<p>«Әзірлеушіге жазу» стандартты «Бөлісу» мәзірін ашады: қайда және не жіберетініңізді өзіңіз таңдайсыз. Мәселені шешу оңай болуы үшін мәтінге қызметтік жол қосылады — қосымша нұсқасы, iOS нұсқасы, телефон моделі және тіл.</p>'),
            ('Деректерді жою', '<p>Қосымшаны жойсаңыз, оның барлық деректері телефоннан жойылады. Деректерді қосымша баптауларында да өшіруге болады. Өзіңіз сақтаған көшірмелер сақтаған жеріңізде қалады.</p>'),
            ('Балалар', '<p>Қосымша 13 жасқа толмаған балаларға арналмаған және олар туралы деректер жинамайды.</p>'),
            ('Өзгерістер', '<p>Саясат өзгерсе, жаңа нұсқасы осы бетте жаңа күнімен пайда болады.</p>'),
            ('Байланыс', f'<p>Құпиялылық туралы сұрақтар: <a href="mailto:{EMAIL}">{EMAIL}</a></p>'),
        ],
        'support_title': 'Қолдау',
        'support_lead': 'Жиі қойылатын сұрақтарға жауаптар. Өз сұрағыңызды таппасаңыз — жазыңыз.',
        'faq': [
            ('Деректерім қайда сақталады?', '<p>Тек iPhone-ыңызда, қосымшаның ішінде. Тіркеу де, әзірлеушінің бұлты да жоқ — сондықтан сақтық көшірме жасау маңызды.</p>'),
            ('Деректерді жаңа телефонға қалай көшіремін?', '<ol><li>Ескі телефонда: «Тағы» → «Сақтық көшірме» → «Көшірмені сақтау», сосын файлды өзіңізге жіберіңіз (AirDrop, Файлдар, мессенджер).</li><li>Жаңасында: Elefund орнатып, «Тағы» → «Сақтық көшірме» → «Файлдан қалпына келтіру» ашып, көшірмені таңдаңыз.</li></ol>'),
            ('Көшірменің құпиясөзін ұмыттым', '<p>Өкінішке қарай, шифрланған көшірмені құпиясөзсіз ашу мүмкін емес — сізге де, бізге де. Шифрлау осылай жұмыс істейді. Қосымша телефонда тұрса, деректер орнында: «Сақтық көшірме» бөлімінде құпиясөзді алып тастаңыз немесе өзгертіңіз де, жаңа көшірме сақтаңыз.</p>'),
            ('Қандай үзінділерді жүктеуге болады?', '<p>Қазір — Kaspi Gold және Halyk Bank PDF-үзінділері (валюталық та). Басқа банктерді үлгілер келген сайын қосамыз — сізге қайсысы керек екенін жазыңыз.</p>'),
            ('Қандай QR-чектер оқылады?', '<p>Фискалдық деректер операторының сайтында тексеруге болатын, QR-коды бар Қазақстанның фискалдық чектері. Чек оқылмаса — оның QR-кодындағы сілтемені бізге жіберіңіз.</p>'),
            ('Pro-ға не кіреді?', '<p>Үзінділерді жүктеу, QR-чектер, санаттар бойынша бюджет және ақша қозғалысы, кеңесші, жобалар мен контрагенттер, шексіз мақсаттар мен конверттер, құпиясөзі бар көшірмелер. Шоттар, операциялар, журнал, есептер, несиелер мен көшірмелер — мәңгі тегін.</p>'),
            ('Сатып алуды қалай қалпына келтіремін?', '<p>«Тағы» → «Elefund Pro» → «Сатып алуларды қалпына келтіру». Сатып алған Apple ID-ді қолданыңыз.</p>'),
            ('Жазылымды қалай тоқтатамын?', '<p>iPhone баптаулары → атыңыз → «Жазылымдар» → Elefund → «Жазылымды тоқтату». Pro төленген кезең соңына дейін жұмыс істейді, ал деректеріңіз орнында қалады.</p>'),
        ],
        'contact_h': 'Бізге жазу',
        'contact': f'Пошта: <a href="mailto:{EMAIL}">{EMAIL}</a>. Немесе қосымшаның өзінен: «Тағы» → «Әзірлеушіге жазу» — хатқа қосымша нұсқасы мен телефон моделі бірден қосылады.',
    },
}

BASE = '/elefund/'  # сайт живёт в подпапке warlockjohn.github.io/elefund


def url(lang, page):
    prefix = BASE if lang == 'ru' else f'{BASE}{lang}/'
    return prefix + ('' if page == 'index' else f'{page}.html')


def page(lang, name, title, desc, body):
    t = T[lang]
    langs = ''.join(
        f'<a href="{url(l, name)}" class="{"on" if l == lang else ""}" hreflang="{l}">{LANG_LABEL[l]}</a>' for l in LANGS
    )
    alternates = ''.join(f'<link rel="alternate" hreflang="{l}" href="https://warlockjohn.github.io{url(l, name)}">' for l in LANGS)
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://warlockjohn.github.io{BASE}assets/icon.png">
<meta name="theme-color" content="#F3EDE4" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1C1915" media="(prefers-color-scheme: dark)">
{alternates}
<link rel="icon" href="{BASE}assets/favicon.png">
<link rel="apple-touch-icon" href="{BASE}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{BASE}style.css">
</head>
<body>
<div class="wrap">
<header class="top">
  <a class="brand" href="{url(lang, 'index')}"><img src="{BASE}assets/icon.png" alt="">Elefund</a>
  <nav class="langs">{langs}</nav>
</header>
{body}
<footer>
  <span>© 2026 Elefund · {t['made']}</span>
  <a href="{url(lang, 'index')}">{t['nav_home']}</a>
  <a href="{url(lang, 'privacy')}">{t['nav_privacy']}</a>
  <a href="{url(lang, 'support')}">{t['nav_support']}</a>
  <a href="mailto:{EMAIL}">{EMAIL}</a>
</footer>
</div>
</body>
</html>
'''


def home(lang):
    t = T[lang]
    feats = ''.join(
        f'<div class="card"><div class="ico" style="color:var(--accent)">{ICONS[i]}</div><h3>{h}</h3><p>{p}</p></div>'
        for i, h, p in t['features']
    )
    also = ''.join(f'<li>{x}</li>' for x in t['also'])
    body = f'''<section class="hero">
  <div>
    <h1>{t['h1']}</h1>
    <p class="lead">{t['lead']}</p>
    <span class="badge"><span><small>{t['badge_small']}</small>{t['badge']}</span></span>
    <p class="note">{t['note']}</p>
  </div>
  <img src="{BASE}assets/elephant-hero.png" alt="" width="380">
</section>
<section class="features">{feats}</section>
<section class="also">
  <img src="{BASE}assets/think.png" alt="" width="220">
  <div><h2>{t['also_h']}</h2><ul>{also}</ul></div>
</section>
<section class="why"><h2>{t['why_h']}</h2><p>{t['why']}</p></section>'''
    return page(lang, 'index', t['title'], t['desc'], body)


def privacy(lang):
    t = T[lang]
    parts = ''.join((f'<h2>{h}</h2>' if h else '') + b for h, b in t['privacy'])
    body = f'''<article class="doc">
  <h1>{t['privacy_title']}</h1>
  <p class="date">{t['updated']}: {UPDATED[lang]}</p>
  {parts}
</article>'''
    return page(lang, 'privacy', f"{t['privacy_title']} — Elefund", t['desc'], body)


def support(lang):
    t = T[lang]
    faq = ''.join(f'<details><summary>{q}</summary>{a}</details>' for q, a in t['faq'])
    body = f'''<article class="doc">
  <h1>{t['support_title']}</h1>
  <p class="date">{t['support_lead']}</p>
  {faq}
</article>
<section class="why contact">
  <img src="{BASE}assets/wave.png" alt="" width="120">
  <div><h2>{t['contact_h']}</h2><p>{t['contact']}</p></div>
</section>'''
    return page(lang, 'support', f"{t['support_title']} — Elefund", t['desc'], body)


for lang in LANGS:
    d = '.' if lang == 'ru' else lang
    os.makedirs(d, exist_ok=True)
    for name, fn in [('index', home), ('privacy', privacy), ('support', support)]:
        with open(os.path.join(d, f'{name}.html'), 'w', encoding='utf-8') as f:
            f.write(fn(lang))
print('ok')
