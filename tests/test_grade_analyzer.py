"""اختبارات محلل الدرجات - نثبّت السلوك قبل أي تعديل."""

from pathlib import Path

from src.grades_analyzer import (
    DEFAULT_GRADE,
    build_report,
    calculate_average,
    calculate_median,
    cell_as_number,
    find_high_achievers,
    read_csv_rows,
)


# ---------- cell_as_number ----------
def test_cell_as_number_valid():
    assert cell_as_number("85.5") == 85.5


def test_cell_as_number_empty_returns_default():
    assert cell_as_number("") == DEFAULT_GRADE


def test_cell_as_number_invalid_returns_default():
    assert cell_as_number("abc") == DEFAULT_GRADE


# ---------- calculate_average ----------
def test_calculate_average_normal():
    assert calculate_average([80, 90, 100]) == 90.0


def test_calculate_average_empty_returns_zero():
    assert calculate_average([]) == 0.0


# ---------- find_high_achievers ----------
def test_find_high_achievers_returns_matching():
    students = ["Ali", "Sara", "Omar"]
    averages = [95.0, 85.0, 91.0]
    assert find_high_achievers(students, averages) == ["Ali", "Omar"]


# ---------- read_csv_rows ----------
def test_read_csv_rows(tmp_path: Path):
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(
        "student_name,math\nAhmed,90\nSara,85\n", encoding="utf-8"
    )
    headers, rows = read_csv_rows(csv_file)
    assert headers == ["student_name", "math"]
    assert len(rows) == 2


# ---------- build_report ----------
def test_build_report_contains_names():
    report = build_report(["Ahmed", "Sara"], [90.0, 85.0])
    assert "Ahmed" in report
    assert "Sara" in report


# ---------- Integration ----------
def test_analyze_file_end_to_end(tmp_path: Path):
    csv_file = tmp_path / "grades.csv"
    csv_file.write_text(
        "student_name,math,science\nAhmed,90,80\nSara,95,95\n",
        encoding="utf-8",
    )
    from src.grades_analyzer import analyze_file

    report = analyze_file(csv_file)
    assert "Ahmed" in report
    assert "Sara" in report
    assert "المتفوقون" in report
# ---------- calculate_median ----------
def test_calculate_median_odd_count():
    assert calculate_median([80, 90, 100]) == 90.0


def test_calculate_median_even_count():
    assert calculate_median([80, 90, 100, 110]) == 95.0


def test_calculate_median_empty():
    assert calculate_median([]) == 0.0