from project import get_posts, clean_title, tiny_url, convert_date
import pytest

def main():
    test_convert_date()
    test_type_error()
    test_get_posts()
    test_clean_title()
    test_tiny_url()

# Can convert an int to date
def test_convert_date():
    d = convert_date(1655147021)
    assert type(d) is str 
    assert d == '2022-06-13 19:03:41'

# Raies TypeError is converting string to date
def test_type_error():
    date = '1655147021'
    with pytest.raises(TypeError):
        convert_date(date)

# Test a returns a dict and matches what gets returned when nothing
# found for tag 'fooblahblahblah'
def test_get_posts():
    uri = "https://api.stackexchange.com/2.3/questions?pagesize=2&order=desc&sort=activity&tagged=fooblahblahblah&site=stackoverflow"
    r = get_posts(uri)
    assert type(r) is dict
    assert str(r).startswith("{'items': [], 'has_more': False")

# Changes the &#39;, &amp;, and &quot; to correct characters
def test_clean_title():
    assert clean_title("Copy the &#39;elemants&#39; of each") == "Copy the 'elemants' of each"
    assert clean_title("Copy the elemants &amp; foo of each") == "Copy the elemants & foo of each"
    assert clean_title("Copy the &quot;elemants&quot; of each") == 'Copy the "elemants" of each'

# Test the tiny_url function
def test_tiny_url():
    url = "https://cs50.harvard.edu/python/2022/weeks/9/"
    t = tiny_url(url)
    assert type(t) == str
    assert t == "https://tinyurl.com/229tf7hf"

if __name__ == "__main__":
    main()