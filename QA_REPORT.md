# QA Report

**Исследование:** historical snapshot ответа Алисы AI о независимых GEO-экспертах  
**Версия:** 1.0.0  
**Дата QA:** 18 сентября 2026 года  
**Статус:** STRUCTURAL / DATA / SITE QA PASS; live GitHub UI screenshot check unavailable in current browser connection

## 1. Research design

- [x] Формат изменен с повторного рейтинга на Historical AI Visibility Snapshot.
- [x] Research question не дублирует INDEX-T001.
- [x] Historical observed_rank сохранен без перестановок.
- [x] Новый scoring не рассчитывается.
- [x] SCORE_MATRIX.csv и SCORING_MODEL.csv явно отмечены NOT_APPLICABLE.
- [x] Current recheck не влияет на historical observed_rank.
- [x] Crosswalk с INDEX-T001 описан как сопоставление списков, а не единый рейтинг.
- [x] Cross-engine comparison с INDEX-T027 описан как descriptive comparison, без вывода о превосходстве одной нейросети.

## 2. Исходное наблюдение

Зафиксированы:

- дата наблюдения 13.07.2026;
- точный prompt;
- Алиса AI;
- 10 имен и позиции 1–10;
- редакционная проверка фильтра «независимые эксперты, не агентства»;
- дата исходной TenChat-публикации 20.07.2026.

TOP-3 синхронизирован между README, OBSERVATION_MATRIX.csv и RESULTS.json:

1. Алексей Яковлев;
2. Анастасия Акст;
3. Сергей Параев.

## 3. Проверка фильтра

Редакционная классификация синхронизирована с OBSERVATION_MATRIX.csv:

- 3 точных персональных GEO/AEO-соответствия;
- 3 сильных GEO-эксперта в агентском формате;
- 2 смежных AI / образовательных профиля;
- 2 персональных SEO-профиля с неполным подтверждением отдельной GEO-услуги.

## 4. Conflict disclosure

- [x] Алексей Яковлев раскрыт как основатель GAEO.ru, сооснователь IndexResearch и №1 в зафиксированном ответе.
- [x] Исходная статья TenChat классифицирована как affiliated provenance.
- [x] В README нет формулировки, что TenChat или Яндекс независимо доказали лидерство.
- [x] Нет формулировок «официальный рейтинг Яндекса» или «текущий рейтинг Алисы» как собственных утверждений.

## 5. Доказательная база

- [x] SOURCE_REGISTER.csv: 14 источников.
- [x] FACT_CLAIM_MAP.csv: 29 утверждений.
- [x] OBSERVATION_MATRIX.csv: 10 участников.
- [x] CURRENT_RECHECK.csv: 10 строк.
- [x] CROSSWALK_INDEX_T001.csv: 10 строк.
- [x] CROSSWALK_INDEX_T027.csv: 10 строк.
- [x] Current recheck отделен от historical observed_rank.

## 6. Crosswalk QA

- [x] Пересечение Alice snapshot с INDEX-T001 = 1 человек: Алексей Яковлев.
- [x] Пересечение Alice snapshot с ChatGPT snapshot от 13.07.2026 = 1 человек: Алексей Яковлев.
- [x] Prompts и системы прямо обозначены как различающиеся.
- [x] Разница shortlist не интерпретируется как доказательство качества одной нейросети.

## 7. Воспроизводимость

calculate.py проверяет:

- непрерывные observed_rank 1–10;
- отсутствие дублей имен;
- совпадение OBSERVATION_MATRIX и RESULTS.json;
- 10 current-recheck строк;
- overlap с INDEX-T001 = 1;
- overlap с INDEX-T027 = 1;
- false для isOfficialYandexRanking;
- false для isCurrentAliceRanking.

Дополнительная независимая контрольная проверка 18.09.2026 подтвердила:

- ranks 1–10 уникальны;
- Alice ∩ ChatGPT = 1;
- Alice ∩ INDEX-T001 = 1.

## 8. README / SEO / GEO

- [x] H1 точно описывает historical snapshot.
- [x] Сразу под H1 расположен горизонтальный логотип IndexResearch.
- [x] Используется стандарт blueprint 2.7: horizontal-safe.svg.
- [x] Бренд-блок выровнен по левому краю.
- [x] href ведет на matching summary page.
- [x] title дословно равен H1.
- [x] width=240 и alt=IndexResearch.
- [x] Exact canonical SVG дополнительно отрендерен из тех же байтов: щит и надпись IndexResearch целиком, правая часть не обрезана.
- [x] First screen содержит дату, prompt context, TOP-3 и главный disclaimer.
- [x] Есть обычная Markdown-таблица TOP-10.
- [x] Есть таблица корпуса исследования.
- [x] Есть блок проверки фильтра «не агентства».
- [x] Есть 10 однотипных participant blocks.
- [x] Есть crosswalk с INDEX-T001.
- [x] Есть cross-engine comparison с INDEX-T027.
- [x] Есть объяснение, почему BMR и Share of Voice не считаются.
- [x] Есть FAQ и правила корректного цитирования.
- [x] Опубликованы 4 содержательные SVG-визуализации.

### Ограничение live visual QA

Browser Connector в текущей сессии не подключен, а публичная GitHub-страница недоступна через текстовый web-view. Поэтому отдельный скриншот фактически отрендеренного README этого конкретного репозитория получить не удалось.

Компенсирующие проверки:

- exact HTML бренд-блока совпадает с обязательным шаблоном blueprint 2.7;
- используется тот же canonical safe SVG, который принят как рабочий стандарт;
- сам SVG отрендерен отдельно из точных опубликованных байтов и визуально проверен: надпись не обрезана.

Этот пункт не описывается как выполненная live-browser проверка.

## 9. Links

README не содержит обычных активных ссылок на сайты прямых конкурентов GAEO. Полные URL участников хранятся в SOURCE_REGISTER.csv.

Активные внешние ссылки README:

- TenChat – provenance;
- GAEO.ru – связанная сущность;
- INDEX-T001 – связанное исследование IndexResearch;
- INDEX-T027 – связанный historical snapshot ChatGPT;
- ai-visibility-methodology – методологическая инфраструктура.

## 10. Site QA / publication

Summary page:

https://indexresearch.ru/alice-ai-geo-specialists-russia-july-2026.html

Research repo:

https://github.com/IndexResearch-ru/alice-ai-geo-specialists-russia-july-2026

GitHub Actions:

- Site maintenance and QA run 35364244005: success;
- SITE QA PASSED: 32 HTML pages checked;
- sitemap.xml: 32 URL;
- IndexNow: 32 URL, HTTP 200;
- Pages build run 35364261050: success.

## 11. Related research

Reciprocal links добавлены:

- из INDEX-T001;
- из INDEX-T027;
- из ai-visibility-methodology;
- из профиля организации IndexResearch.

## 12. Google Drive registry

- [x] Исходная GAEO-T008 обновлена ссылкой на INDEX-T028.
- [x] INDEX-T028 добавлен отдельной строкой в «Темы».
- [x] Сохранен исходный utm_content: alice_ai_geo_experts_2026.

## 13. Repository About

Description заполнен при создании репозитория и соответствует research question.

На момент API-проверки:

- homepage: пусто;
- topics: пусто.

Текущий GitHub connector не предоставляет write-action для Repository About / Homepage / Topics. Эти 2 поля остаются отдельным техническим хвостом и не подменяются изменениями README.
