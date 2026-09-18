"""محلل درجات الطلاب - مشروع تطبيقي لمفاهيم الكود النظيف."""

import csv
from pathlib import Path

# ============================================================
# الثوابت - لا أرقام سحرية
# ============================================================
DEFAULT_GRADE = 0.0
HIGH_ACHIEVER_THRESHOLD = 90.0


# ============================================================
# القراءة (I/O)
# ============================================================
def read_csv_rows(path: Path) -> tuple[list[str], list[list[str]]]:
    """يقرأ ملف CSV ويعيد (العناوين، الصفوف)."""
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = [row for row in reader if row]
    return headers, rows


# ============================================================
# التحويل (دالة نقية)
# ============================================================
def cell_as_number(value: str, default: float = DEFAULT_GRADE) -> float:
    """يحوّل خلية نصية إلى رقم، ويعيد الافتراضي عند الفشل."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


# ============================================================
# الحساب (منطق العمل)
# ============================================================
def calculate_average(numbers: list[float]) -> float:
    """يحسب المتوسط، ويعيد صفراً إن كانت القائمة فارغة."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def find_high_achievers(
    students: list[str],
    averages: list[float],
    threshold: float = HIGH_ACHIEVER_THRESHOLD,
) -> list[str]:
    """يعيد أسماء الطلاب الذين معدلهم >= الحد."""
    return [
        name for name, avg in zip(students, averages) if avg >= threshold
    ]


# ============================================================
# التقرير
# ============================================================
def build_report(students: list[str], averages: list[float]) -> str:
    """يبني تقريراً نصياً عن نتائج الطلاب."""
    lines = ["=" * 40, "تقرير درجات الطلاب", "=" * 40]
    for name, avg in zip(students, averages):
        lines.append(f"{name:<10} | {avg:6.2f}")
    lines.append("-" * 40)
    lines.append(f"عدد الطلاب: {len(students)}")
    lines.append(f"المتوسط العام: {calculate_average(averages):.2f}")
    high = find_high_achievers(students, averages)
    lines.append(f"المتفوقون ({len(high)}): {', '.join(high) or 'لا أحد'}")
    return "\n".join(lines)


# ============================================================
# خط الأنابيب الكامل
# ============================================================
def analyze_file(path: Path) -> str:
    """يقرأ الملف، يحسب المعدلات، ويعيد التقرير."""
    headers, rows = read_csv_rows(path)
    name_col = headers.index("student_name")
    grade_cols = [
        i for i, h in enumerate(headers) if h != "student_name"
    ]

    students = [row[name_col] for row in rows]
    averages = [
        calculate_average(
            [cell_as_number(row[i]) for i in grade_cols]
        )
        for row in rows
    ]
    return build_report(students, averages)


# ============================================================
# نقطة الدخول
# ============================================================
def main() -> None:
    data_path = Path("data/grades.csv")
    if not data_path.exists():
        print(f"خطأ: لم يتم العثور على الملف {data_path}")
        return
    print(analyze_file(data_path))


if __name__ == "__main__":
    main()