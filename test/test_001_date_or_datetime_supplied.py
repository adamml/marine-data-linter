def test_001_date_or_datetime_supplied(date, dattim):
    """Test to ensure that at least one of a date or datetime flag has been
    passed and is set"""
    _pass = False
    if date is not None or dattim is not None:
        _pass = True
    assert _pass is True