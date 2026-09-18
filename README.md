# محلل درجات الطلاب 📊

أداة صغيرة تقرأ ملف CSV للدرجات، تنظّفه، وتحسب المعدلات والمتفوقين.

## ما هذا؟

يقرأ ملف درجات طلاب من `data/grades.csv`، يتعامل مع القيم الفارغة،
ويطبع تقريراً فيه معدل كل طالب والمتوسط العام والوسيط والمتفوقين.

## كيف أشغّله؟

```bash
python -m venv .venv
source .venv/Scripts/activate   # على Windows
pip install -r requirements.txt
python -m src.grades_analyzer

االناتج المتوقع
========================================
تقرير درجات الطلاب
========================================
Ahmed      |  84.33
Sara       |  91.67
Omar       |  51.67
Layla      |  53.33
Khalid     |  93.00
Noor       |  57.67
----------------------------------------
عدد الطلاب: 6
المتوسط العام: 71.94
الوسيط العام: 71.00
المتفوقون (2): Sara, Khalid

كيف الاختبار 
pytest tests/ -q

هيكليه المشروع
src/                       ← منطق العمل
  └── grades_analyzer.py
tests/                     ← الاختبارات
  └── test_grades_analyzer.py
data/                      ← البيانات (غير مرفوعة)
.github/                   ← إعدادات Vibe Coding
  └── copilot-instructions.md
requirements.txt           ← المكتبات المطلوبة
README.md                  ← هذا الملف
