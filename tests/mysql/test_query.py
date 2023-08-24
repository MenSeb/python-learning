"""Tests MySQL query."""


from mysql.query import (
    query_columns,
    query_condition,
    query_ignore,
    query_limit,
    query_order,
    query_priority,
)


def test_query_condition() -> None:
    """Test query_condition."""
    assert query_condition(None) == ""
    assert query_condition("test") == "WHERE test"


def test_query_columns() -> None:
    """Test query_columns."""
    assert query_columns(None) == "*"
    assert query_columns("test") == "test"


def test_query_ignore() -> None:
    """Test query_ignore."""
    assert query_ignore(None) == ""
    assert query_ignore(ignore=False) == ""
    assert query_ignore(ignore=True) == "IGNORE"


def test_query_limit() -> None:
    """Test query_limit."""
    assert query_limit(None) == ""
    assert query_limit(5) == "LIMIT 5"


def test_query_order() -> None:
    """Test query_order."""
    assert query_order(None) == ""
    assert query_order("test") == "ORDER BY test"


def test_query_priority() -> None:
    """Test query_priority."""
    assert query_priority(None) == ""
    assert query_priority(priority=False) == ""
    assert query_priority(priority=True) == "LOW_PRIORITY"
